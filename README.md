LinkedIn Profile Scraper
This project is a Python-based web scraper implemented in a Jupyter notebook (Linkedin.ipynb) that extracts data from a LinkedIn profile, including full name, job title, company, location, bio, skills, recent activity, job history, and company growth signals. The scraped data is displayed in the terminal (or Jupyter output cell) and saved as JSON (linkedin_profile.json) and CSV (linkedin_profile.csv) files in the project folder.


Setup Instructions
Follow these steps to set up and run the project:
1. Clone or Download the Project

Download the project files (Linkedin.ipynb and requirements.txt) to a local directory.



2. Create a Virtual Environment
To avoid conflicts with other Python projects, use a virtual environment:
python -m venv venv

Activate the virtual environment:

Windows:venv\Scripts\activate


Mac/Linux:source venv/bin/activate


You should see (venv) in your terminal prompt.

3. Install Dependencies
Install the required Python libraries listed in requirements.txt:
pip install -r requirements.txt

The requirements.txt should contain:
selenium==4.15.2
beautifulsoup4==4.12.3
lxml==5.2.2
jupyter==1.0.0


5. Configure the Notebook
Open Linkedin.ipynb in Jupyter Notebook or JupyterLab and update the configuration cell with your LinkedIn credentials and target profile URL:
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
PROFILE_URL = "https://www.linkedin.com/in/harsh-o4/"



6. Run the Notebook

Start Jupyter:In the terminal, with the virtual environment activated, run:
jupyter notebook



Handle Security Validation (if prompted):If LinkedIn displays a CAPTCHA or 2FA prompt, the script will pause and display in the terminal/output cell:
Security validation (CAPTCHA/2FA) detected. Please complete it manually in the browser and press Enter here...


Complete the CAPTCHA or 2FA in the browser.
Press Enter in the terminal (or a separate terminal window if Jupyter is running) to continue.



Expected Output
Upon successful execution, the script:

Displays in Terminal/Jupyter Output:

Shows login status (e.g., " Login successful!" or " Login failed").

Prints the scraped data as JSON, formatted like:

{
  "Full name": "Harsh Singh",
  "Job title": "Contributor @GSSoC'24 extd. | Codechef 1300+ | 5⭐ - C, Problem Solving | 4⭐ - C++ | MPGI'27 | Code-o-Fiesta 2.0 Runner-up",
  "Company": "Codolio",
  "Location": "Kanpur, Uttar Pradesh, India",
  "Professional Insights": [],
  "LinkedIn bio": "Eager to gain experience, and open to challenges. Eager to gain experience, and open to challenges.",
  "Tech stack": [],
  "Recent LinkedIn activity": [
    "Tadaa!! 𝟱𝟬𝟬 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀 𝘀𝗼𝗹𝘃𝗲𝗱 across all platforms😤.This is a big milestone for me. Along the way, I’ve learned so much — from basic data structures to complex algorithms and clever shortcuts. More importantly, I’ve learned how to approach problems I’ve never seen before. Also,Codoliocard looks better now.Already looking forward to hitting 𝟭𝟬𝟬𝟬!",
    "Just received the 𝟱𝟬 𝗱𝗮𝘆𝘀 𝗯𝗮𝗱𝗴𝗲 inLeetCode.It hasn't been my primary focus over the past few months, but as they say, better late than never. 😅hashtag#leetcodehashtag#50days",
    "𝗣𝗿𝗼𝗯𝗹𝗲𝗺-𝘀𝗼𝗹𝘃𝗶𝗻𝗴 𝗶𝘀 𝗮𝗹𝗹 𝗮𝗯𝗼𝘂𝘁 𝗹𝗲𝗮𝗿𝗻𝗶𝗻𝗴 𝗻𝗲𝘄 𝘁𝗵𝗶𝗻𝗴𝘀. Here are some things that I've learnt over the past few days:",
    "Was revising DSA and got a rather pleasant surprise: 𝟱⭐ 𝗶𝗻 𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝗦𝗼𝗹𝘃𝗶𝗻𝗴 onHackerRank.hashtag#HackerRankhashtag#problemsolving",
    "Just earned the 𝗗𝗶𝗮𝗺𝗼𝗻𝗱 𝗦𝘁𝗿𝗲𝗮𝗸 𝗕𝗮𝗱𝗴𝗲 atCodeChef."
  ],
  "Job history changes": [
    {
      "raw": "Contributor | Contributor | GirlScript Summer of Code · Internship | GirlScript Summer of Code · Internship | Oct 2024 - Oct 2024 · 1 mo | Oct 2024 to Oct 2024 · 1 mo | Kanpur, Uttar Pradesh, India · Remote | Kanpur, Uttar Pradesh, India · Remote | Skills: | GitHub | Skills: | GitHub",
      "title": "Contributor",
      "company": "GirlScript Summer of Code · Internship",
      "dates": "Oct 2024 to Oct 2024 · 1 mo",
      "location": "Kanpur, Uttar Pradesh, India · Remote"
    }
  ],
  "Company growth signals": {
    "company_page": "https://www.linkedin.com/company/14488336/",
    "followers": "154K followers",
    "employees_on_linkedin": null
  },
  "profile_url": "https://www.linkedin.com/in/harsh-o4/"
}


Confirms file save: "✅ Saved: linkedin_profile.json, linkedin_profile.csv".


