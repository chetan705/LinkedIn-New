import os
import time
import json
import csv
from typing import List, Dict, Any, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

EMAIL = "your email id"          
PASSWORD = "your password"   
PROFILE_URL = "https://www.linkedin.com/in/harsh-o4/"  

HEADLESS = False

def build_driver() -> webdriver.Chrome:
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    return webdriver.Chrome(options=chrome_options)

def wait_css(drv, selector, timeout=10):
    return WebDriverWait(drv, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

def safe_text(el) -> str:
    try:
        return el.text.strip()
    except Exception:
        return ""

def get_soup(drv) -> BeautifulSoup:
    return BeautifulSoup(drv.page_source, "lxml")

def click_if_present(drv, by, value, timeout=3) -> bool:
    try:
        el = WebDriverWait(drv, timeout).until(EC.element_to_be_clickable((by, value)))
        drv.execute_script("arguments[0].click();", el)
        time.sleep(1)
        return True
    except TimeoutException:
        return False

def click_all_see_more(drv):
    
    patterns = [
        (By.CLASS_NAME, "inline-show-more-text__button"),
        (By.XPATH, "//button[contains(., 'See more')]"),
        (By.XPATH, "//button[contains(., 'Show all')]"),
        (By.CSS_SELECTOR, "button[aria-expanded='false']"),
    ]
    clicked_any = True

    for _ in range(3):
        if not clicked_any:
            break
        clicked_any = False
        for by, sel in patterns:
            try:
                buttons = drv.find_elements(by, sel)
            except Exception:
                buttons = []
            for b in buttons:
                try:
                    if b.is_displayed():
                        drv.execute_script("arguments[0].click();", b)
                        time.sleep(0.5)
                        clicked_any = True
                except Exception:
                    pass


# Login with manual security validation

def linkedin_login(drv, email: str, password: str):
    try:
        drv.get("https://www.linkedin.com/login")
        wait_css(drv, "#username", timeout=15)
        drv.find_element(By.ID, "username").send_keys(email)
        drv.find_element(By.ID, "password").send_keys(password)
        drv.find_element(By.ID, "password").send_keys(Keys.RETURN)
        time.sleep(3)  

        # Check for security validation (CAPTCHA)
        try:
            WebDriverWait(drv, 10).until(
                EC.any_of(
                    EC.presence_of_element_located((By.ID, "input__email_verification_pin")),
                    EC.url_contains("checkpoint/challenge")
                )
            )
            print(" Security validation (CAPTCHA/2FA) detected. Please complete it manually in the browser and press Enter here...")
            input("Press Enter after completing the security validation...")
            time.sleep(2)  
        except TimeoutException:
            print("ℹ No security validation detected.")

        # Verify login success
        current_url = drv.current_url
        if "feed" in current_url or "home" in current_url:
            print(" Login successful!")
            return True
        else:
            print(f" Login failed. Current URL: {current_url}")
            return False
    except Exception as e:
        print(f" Login error: {e}")
        return False


def scrape_top_card(drv) -> Dict[str, Any]:
    data = {
        "Full name": "Not found",
        "Job title": "Not found",
        "Company": "Not found",
        "Location": "Not found",
    }
    try:
        wait_css(drv, "main", timeout=15)
    except TimeoutException:
        return data

    click_all_see_more(drv)
    soup = get_soup(drv)

    # Full name
    name = ""
    for sel in [
        "h1.text-heading-xlarge",
        "h1",
    ]:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            name = el.get_text(strip=True)
            break
    if name:
        data["Full name"] = name

    # Job title (headline under name)
    headline = ""
    for sel in [
        "div.text-body-medium.break-words",
        "div[data-view-name='profile-card'] div.inline-show-more-text",
    ]:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            headline = el.get_text(strip=True)
            break
    if headline:
        data["Job title"] = headline

    # Location
    location = ""
    for sel in [
        "span.text-body-small.inline.t-black--light.break-words",
        "span.inline.t-black--light",
    ]:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            location = el.get_text(strip=True)
            break
    if location:
        data["Location"] = location

    # Company 
    company = ""
    top_card = soup.select_one("div.pv-text-details__right-panel")
    if top_card:
        a_tags = top_card.select("a[href*='/company/']")
        if a_tags:
            company = a_tags[0].get_text(strip=True)
    if not company:
        a_tags = soup.select("a[href*='/company/']")
        if a_tags:
            company = a_tags[0].get_text(strip=True)
    if company:
        data["Company"] = company

    return data


# About section

def scrape_about(drv) -> str:
    try:
        drv.get(drv.current_url.split("?")[0])  
        time.sleep(1)
        drv.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.35);")
        time.sleep(1)
        click_all_see_more(drv)
        soup = get_soup(drv)
        about_block = None
        for sel in [
            "section[id='about'] div.inline-show-more-text",
            "section[id='about']",
            "div.display-flex.ph5.pv3",
        ]:
            about_block = soup.select_one(sel)
            if about_block:
                break
        if about_block:
            text = about_block.get_text(separator=" ", strip=True)
            return text if text else "Not found"
    except Exception:
        pass
    return "Not found"

# Professional Insights
def scrape_professional_insights(drv) -> List[str]:
    insights = []
    try:
        drv.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        soup = get_soup(drv)
        selectors = [
            "section.pv-highlights-section",
            "section[id='highlight-container']",
            "div.pvs-highlight__container",
            "div.pv-profile-card--feature",
        ]
        for sel in selectors:
            for sec in soup.select(sel):
                txt = sec.get_text(separator=" ", strip=True)
                if txt and txt not in insights:
                    insights.append(txt)
        return insights[:10]
    except Exception:
        return insights


# Skills

def scrape_skills(drv, profile_url: str) -> List[str]:
    skills = []
    try:
        drv.get(profile_url.rstrip("/") + "/details/skills/")
        wait_css(drv, "main", timeout=10)
        click_all_see_more(drv)
        soup = get_soup(drv)
        for sel in [
            "span.mr1.t-bold",
            "span.pvs-list__item--one-column span[aria-hidden='true']",
            "div.pvs-list__outer-container li span.mr1.t-bold",
        ]:
            for el in soup.select(sel):
                text = el.get_text(strip=True)
                if text and text not in skills:
                    skills.append(text)
        return skills[:50]
    except Exception:
        return skills


# Recent activity

def scrape_recent_activity(drv, profile_url: str) -> List[str]:
    items = []
    try:
        drv.get(profile_url.rstrip("/") + "/recent-activity/all/")
        wait_css(drv, "main", timeout=10)
        time.sleep(2)
        soup = get_soup(drv)
        selectors = [
            "div.update-components-text.relative span[dir='ltr']",
            "div.feed-shared-update-v2__description-wrapper span[dir='ltr']",
            "a.app-aware-link[aria-label]",
        ]
        for sel in selectors:
            for el in soup.select(sel):
                txt = el.get_text(strip=True)
                if txt and txt not in items:
                    items.append(txt)
        return items[:10]
    except Exception:
        return items


# Experience

def scrape_experience(drv, profile_url: str) -> List[Dict[str, str]]:
    jobs: List[Dict[str, str]] = []
    try:
        drv.get(profile_url.rstrip("/") + "/details/experience/")
        wait_css(drv, "main", timeout=10)
        click_all_see_more(drv)
        soup = get_soup(drv)
        cards = soup.select("li.pvs-list__paged-list-item, li.pvs-list__item--line-separated")
        if not cards:
            cards = soup.select("div.pvs-entity")
        for card in cards:
            spans = [s.get_text(strip=True) for s in card.select("span.visually-hidden")]
            text = card.get_text(separator=" | ", strip=True)
            role = {
                "raw": text[:300] if text else "",
                "title": "",
                "company": "",
                "dates": "",
                "location": "",
            }
            if spans:
                role["title"] = spans[0] if len(spans) >= 1 else ""
                role["company"] = spans[1] if len(spans) >= 2 else ""
                role["dates"] = spans[2] if len(spans) >= 3 else ""
                role["location"] = spans[3] if len(spans) >= 4 else ""
            jobs.append(role)
        return jobs[:30]
    except Exception:
        return jobs


# Company growth signals

def scrape_company_growth(drv) -> Dict[str, Any]:
    result = {"company_page": None, "followers": None, "employees_on_linkedin": None}
    try:
        soup = get_soup(drv)
        a_tags = soup.select("a[href*='/company/']")
        if not a_tags:
            return result
        href = a_tags[0].get("href")
        if not href:
            return result
        if href.startswith("/"):
            href = "https://www.linkedin.com" + href
        result["company_page"] = href
        drv.get(href)
        wait_css(drv, "main", timeout=10)
        time.sleep(2)
        soup = get_soup(drv)
        possible = [
            "div.org-top-card-summary-info-list__info-item",
            "span.t-normal.t-14.t-black--light",
            "p.org-top-card__metrics-item",
        ]
        text_blobs = []
        for sel in possible:
            for el in soup.select(sel):
                t = el.get_text(" ", strip=True)
                if t:
                    text_blobs.append(t)
        for t in text_blobs:
            if "followers" in t.lower() and result["followers"] is None:
                result["followers"] = t
            if ("employees" in t.lower() or "people on linkedin" in t.lower()) and result["employees_on_linkedin"] is None:
                result["employees_on_linkedin"] = t
        return result
    except Exception:
        return result


def scrape_profile_all(drv, profile_url: str) -> Dict[str, Any]:
    try:
        drv.get(profile_url)
        wait_css(drv, "main", timeout=15)
        time.sleep(2)
        top = scrape_top_card(drv)
        about = scrape_about(drv)
        insights = scrape_professional_insights(drv)
        skills = scrape_skills(drv, profile_url)
        activity = scrape_recent_activity(drv, profile_url)
        experience = scrape_experience(drv, profile_url)
        company_growth = scrape_company_growth(drv)
        out = {
            "Full name": top.get("Full name", "Not found"),
            "Job title": top.get("Job title", "Not found"),
            "Company": top.get("Company", "Not found"),
            "Location": top.get("Location", "Not found"),
            "Professional Insights": insights,
            "LinkedIn bio": about,
            "Tech stack": skills,
            "Recent LinkedIn activity": activity,
            "Job history changes": experience,
            "Company growth signals": company_growth,
            "profile_url": profile_url,
        }
        return out
    except Exception as e:
        print(f" Error scraping profile: {e}")
        return {
            "Full name": "Not found",
            "Job title": "Not found",
            "Company": "Not found",
            "Location": "Not found",
            "Professional Insights": [],
            "LinkedIn bio": "Not found",
            "Tech stack": [],
            "Recent LinkedIn activity": [],
            "Job history changes": [],
            "Company growth signals": {"company_page": None, "followers": None, "employees_on_linkedin": None},
            "profile_url": profile_url,
        }


def save_json(data: Dict[str, Any], path: str = "linkedin_profile.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_csv_flat(data: Dict[str, Any], path: str = "linkedin_profile.csv"):
    row = {
        "Full name": data.get("Full name", ""),
        "Job title": data.get("Job title", ""),
        "Company": data.get("Company", ""),
        "Location": data.get("Location", ""),
        "LinkedIn bio": data.get("LinkedIn bio", ""),
        "Professional Insights": "; ".join(data.get("Professional Insights", []) or []),
        "Tech stack": "; ".join(data.get("Tech stack", []) or []),
        "Recent LinkedIn activity": "; ".join(data.get("Recent LinkedIn activity", []) or []),
        "Job history changes": json.dumps(data.get("Job history changes", []), ensure_ascii=False),
        "Company growth signals": json.dumps(data.get("Company growth signals", {}), ensure_ascii=False),
        "profile_url": data.get("profile_url", ""),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)


# Main

if __name__ == "__main__":
    driver = None
    try:
        driver = build_driver()
        if linkedin_login(driver, EMAIL, PASSWORD):
            result = scrape_profile_all(driver, PROFILE_URL)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            save_json(result, "linkedin_profile.json")
            save_csv_flat(result, "linkedin_profile.csv")
            print("\n Saved: linkedin_profile.json, linkedin_profile.csv")
        else:
            print(" Scraping aborted due to login failure.")
    except Exception as e:
        print(f" Main execution error: {e}")
    finally:
        if driver:
            driver.quit()

