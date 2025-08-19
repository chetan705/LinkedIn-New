LinkedIn Profile Scraper
This project is a Python-based web scraper implemented in a python file (app.py) that extracts data from a LinkedIn profile for 3 users at the same time, including full name, job title, company, location, bio, skills, recent activity, job history, and company growth signals. The scraped data is displayed in the terminal and saved as JSON (linkedin_profile.json) and CSV (linkedin_profile.csv) files in the project folder.


Setup Instructions
Follow these steps to set up and run the project:
1. Clone or Download the Project

Download the project files (app.py and requirements.txt) to a local directory.



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
Create .env file 
Enter your LinkedIn Email and password
LINKEDIN_EMAIL= "youremail@gmail.com"
LINKEDIN_PASSWORD= "your password here"


Open app.py and update the configuration cell with your LinkedIn credentials and target profile URL:
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
(Add 3 linkedin user profile address)
PROFILE_URL = "https://www.linkedin.com/in/harsh-o4/"
"https://www.linkedin.com/in/harsh-o4/"
"https://www.linkedin.com/in/harsh-o4/"



7. Usage
Run the scraper with the following command:

bash
python app.py
Security Validation Handling
When you run the script, LinkedIn may display a CAPTCHA or 2FA prompt. The script will pause and display:

text
Security validation (CAPTCHA/2FA) detected. Please complete it manually in the browser and press Enter here...
Complete the CAPTCHA or 2FA in the browser window that opens

Press Enter in the terminal to continue the scraping process

Proxy Configuration (Optional)
To avoid security validation prompts, you can use proxies. The code currently doesn't include proxy support, but you can modify it to add this functionality.

Free proxy sources:

https://proxyscrape.com/free-proxy-list

Paid proxy services:

Bright Data ($7-15 per GB)

Oxylabs ($7-15 per GB)

Smartproxy ($7-15 per GB)



Expected Output
Upon successful execution, the script:

Displays in Terminal Output:

Shows login status (e.g., " Login successful!" or " Login failed").

Prints the scraped data as JSON, formatted like:

[
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
      "followers": "154K  followers",
      "employees_on_linkedin": null
    },
    "profile_url": "https://www.linkedin.com/in/harsh-o4/"
  },
  {
    "Full name": "Mohit Sharma",
    "Job title": "Software Engineer",
    "Company": "Create a Company Page",
    "Location": "Toronto, Ontario, Canada",
    "Professional Insights": [],
    "LinkedIn bio": "Since joining Upwork as a Software Engineer, my focus has been on leveraging Azure DevOps Services to enhance the accessibility of software systems. With a solid foundation in Electrical and Electronics Engineering from Punjab Technical University, I apply rigorous engineering principles to every project. Our team's efforts in software systems engineering have led to improved user experiences and robust solutions. My previous role as a Business System Analyst at Net Solutions instilled a keen understanding of how to balance technical prowess with user needs, ensuring that every solution is not only functional but also user-friendly. Since joining Upwork as a Software Engineer, my focus has been on leveraging Azure DevOps Services to enhance the accessibility of software systems. With a solid foundation in Electrical and Electronics Engineering from Punjab Technical University, I apply rigorous engineering principles to every project.\n\nOur team's efforts in software systems engineering have led to improved user experiences and robust solutions. My previous role as a Business System Analyst at Net Solutions instilled a keen understanding of how to balance technical prowess with user needs, ensuring that every solution is not only functional but also user-friendly.",
    "Tech stack": [],
    "Recent LinkedIn activity": [
      "Hi everyone - I am looking for a new role and would appreciate your support. Thank you in advance for any connections, advice, or opportunities you can offer.hashtag#OpenToWork",
      "With a heavy heart, I bid goodbye to theNet Solutionsfamily.I've had a fantastic working time, building relationships, learning, and sharing knowledge. Working with the team ofNet Solutionsbecame an enriching experience. Thank you to all those involved! We built some great things together!Now it's time to move forward and looking more learning opportunities.Please don't hesitate to reach out.Thank you and I appreciate your assistance! 🙂",
      "Special Thanks to \"Google\" and \"Meta\".... I have obtained a \"Front End Development\" Certificatehashtag#googlehashtag#metahashtag#frontenddeveloperhashtag#canadajobshashtag#itcompanyhashtag#canadarecruitmenthashtag#googlecareercertificateshashtag#newcareeropportunitieshashtag#newbeginnings",
      "I’m happy to share that I’ve obtained a new certification: Verified International Academic Qualifications fromWorld Education Services!",
      "View my verified achievement from World Education Services."
    ],
    "Job history changes": [
      {
        "raw": "Software Engineer | Software Engineer | Upwork | Upwork | Aug 2023 - Present · 2 yrs 1 mo | Aug 2023 to Present · 2 yrs 1 mo | Canada · Remote | Canada · Remote | Skills: | Selenium WebDriver · Mobile Applications · User Acceptance Testing · Azure DevOps Services · Agile Testing | Skills: | Selenium",
        "title": "Software Engineer",
        "company": "Upwork",
        "dates": "Aug 2023 to Present · 2 yrs 1 mo",
        "location": "Canada · Remote"
      },
      {
        "raw": "Business System Analyst | Business System Analyst | Net Solutions · Full-time | Net Solutions · Full-time | Jun 2019 - May 2023 · 4 yrs | Jun 2019 to May 2023 · 4 yrs | Chandigarh, India | Chandigarh, India | Skills: | Quality Management · Software Systems Engineering · Selenium WebDriver | Skills: ",
        "title": "Business System Analyst",
        "company": "Net Solutions · Full-time",
        "dates": "Jun 2019 to May 2023 · 4 yrs",
        "location": "Chandigarh, India"
      },
      {
        "raw": "Software Quality Assurance Analyst | Software Quality Assurance Analyst | Software Quality Assurance Analyst | Technocrats Horizons Compusoft Pvt Ltd - Web/Mobile Development and Design | Technocrats Horizons Compusoft Pvt Ltd - Web/Mobile Development and Design | Mar 2019 - Jun 2019 · 4 mos | Mar 2",
        "title": "Software Quality Assurance Analyst",
        "company": "Technocrats Horizons Compusoft Pvt Ltd - Web/Mobile Development and Design",
        "dates": "Mar 2019 to Jun 2019 · 4 mos",
        "location": "Mohali, Punjab, India · Hybrid"
      },
      {
        "raw": "Associate Software QA Engineer | Associate Software QA Engineer | Vertex Infosoft Solutions Pvt. Ltd · Permanent Full-time | Vertex Infosoft Solutions Pvt. Ltd · Permanent Full-time | Jan 2015 - Feb 2019 · 4 yrs 2 mos | Jan 2015 to Feb 2019 · 4 yrs 2 mos | Sahibzada Ajit Singh Nagar, Punjab, India ·",
        "title": "Associate Software QA Engineer",
        "company": "Vertex Infosoft Solutions Pvt. Ltd · Permanent Full-time",
        "dates": "Jan 2015 to Feb 2019 · 4 yrs 2 mos",
        "location": "Sahibzada Ajit Singh Nagar, Punjab, India · On-site"
      }
    ],
    "Company growth signals": {
      "company_page": "https://www.linkedin.com/company/4827017/",
      "followers": "3M  followers",
      "employees_on_linkedin": null
    },
    "profile_url": "https://www.linkedin.com/in/mohit-sharma-m1313/"
  },
  {
    "Full name": "Mayank Gupta",
    "Job title": "Laravel Developer | PHP Programmer | Backend developer",
    "Company": "Create a Company Page",
    "Location": "Kanpur, Uttar Pradesh, India",
    "Professional Insights": [],
    "LinkedIn bio": "Curious Learner | Innovator in Software & Systems | Aspiring DBA A passionate and curious learner in innovating software designs, system design, and coding, as well as debugging, troubleshooting, and augmenting programs. I thrive on exploring how technology works, breaking down complex problems, and building creative solutions that are both functional and future-ready. Currently growing as a backend developer, with the aim of transitioning into a Database Administrator (DBA) role — combining my programming expertise with database management skills to create secure, optimized, and high-performing data systems. I believe in learning by doing — whether it’s building small projects, dissecting new technologies, or collaborating with others to solve real-world challenges. Curious Learner | Innovator in Software & Systems | Aspiring DBA\nA passionate and curious learner in innovating software designs, system design, and coding, as well as debugging, troubleshooting, and augmenting programs. I thrive on exploring how technology works, breaking down complex problems, and building creative solutions that are both functional and future-ready.\n\nCurrently growing as a backend developer, with the aim of transitioning into a Database Administrator (DBA) role — combining my programming expertise with database management skills to create secure, optimized, and high-performing data systems. I believe in learning by doing — whether it’s building small projects, dissecting new technologies, or collaborating with others to solve real-world challenges.",
    "Tech stack": [],
    "Recent LinkedIn activity": [
      "I’m happy to share that I’m starting a new position as Software Engineer atThe Smart Cube!",
      "Hi everyone! I’m seeking a new role and would appreciate your support. If you hear of any opportunities or just want to catch up, please send me a message or comment below. I’d love to reconnect.hashtag#OpenToWorkAbout me & what I’m looking for:💼 I’m looking for Back End Developer, Senior PHP Developer, PHP Programmer, Software Engineer, and Laravel Developer roles.🌎 I’m open to roles in Kanpur, Noida, Lucknow, Gurugram, and Delhi.⭐ I’ve previously worked at Sportsmatik.",
      "Hi everyone! I’m seeking a new role and would appreciate your support. If you hear of any opportunities or just want to catch up, please send me a message or comment below. I’d love to reconnect.hashtag#OpenToWorkAbout me & what I’m looking for:💼 I’m looking for Laravel Developer, PHP Developer, Back End Developer, Senior PHP Developer, and PHP Programmer roles.🌎 I’m open to roles in Kanpur, Noida, Lucknow, Gurugram, and Delhi.⭐ I’ve previously worked at Sportsmatik.",
      "Wordpress, Squarespace and Webflow didn’t displace developers.Canva didn’t turn everyone into a world class designer.Don’t let new tools and technology worry you.Leverage them!hashtag#designerhashtag#canvadesignhashtag#wordpresshashtag#squarespacehashtag#chatgpthashtag#webflow",
      "Hi everyone - I am looking for a new role and would appreciate your support. Thank you in advance for any connections, advice, or opportunities you can offer.hashtag#OpenToWork"
    ],
    "Job history changes": [
      {
        "raw": "Software Engineer | Software Engineer | WNS · Full-time | WNS · Full-time | May 2025 - Present · 4 mos | May 2025 to Present · 4 mos | Noida, Uttar Pradesh, India · Hybrid | Noida, Uttar Pradesh, India · Hybrid | Working on client organisation The Smart Cube acquired by WNS. | and my payroll company",
        "title": "Software Engineer",
        "company": "WNS · Full-time",
        "dates": "May 2025 to Present · 4 mos",
        "location": "Noida, Uttar Pradesh, India · Hybrid"
      },
      {
        "raw": "PHP Developer | PHP Developer | Sportsmatik · Full-time | Sportsmatik · Full-time | Sep 2021 - Apr 2025 · 3 yrs 8 mos | Sep 2021 to Apr 2025 · 3 yrs 8 mos | Kanpur, Uttar Pradesh, India · On-site | Kanpur, Uttar Pradesh, India · On-site | Here I worked as a backend developer in advance php. | Here I",
        "title": "PHP Developer",
        "company": "Sportsmatik · Full-time",
        "dates": "Sep 2021 to Apr 2025 · 3 yrs 8 mos",
        "location": "Kanpur, Uttar Pradesh, India · On-site"
      },
      {
        "raw": "Web Developer | Web Developer | Magic web services · Freelance | Magic web services · Freelance | Jan 2024 - Jul 2024 · 7 mos | Jan 2024 to Jul 2024 · 7 mos | Noida, Uttar Pradesh, India · Remote | Noida, Uttar Pradesh, India · Remote | Skills: | CodeIgniter · HTML Emails · HTML5 · PHP | Skills: | C",
        "title": "Web Developer",
        "company": "Magic web services · Freelance",
        "dates": "Jan 2024 to Jul 2024 · 7 mos",
        "location": "Noida, Uttar Pradesh, India · Remote"
      },
      {
        "raw": "Freelance Web Developer | Freelance Web Developer | Freelance Web Developer | HP Consultant · Freelance | HP Consultant · Freelance | May 2021 - Aug 2021 · 4 mos | May 2021 to Aug 2021 · 4 mos | Kanpur Nagar, Uttar Pradesh, India | Kanpur Nagar, Uttar Pradesh, India | working as a freelance web deve",
        "title": "Freelance Web Developer",
        "company": "HP Consultant · Freelance",
        "dates": "May 2021 to Aug 2021 · 4 mos",
        "location": "Kanpur Nagar, Uttar Pradesh, India"
      },
      {
        "raw": "Web Developer | Web Developer | Web Developer | Skyline web solutionss · Full-time | Skyline web solutionss · Full-time | Dec 2020 - May 2021 · 6 mos | Dec 2020 to May 2021 · 6 mos | Kanpur, Uttar Pradesh, India | Kanpur, Uttar Pradesh, India",
        "title": "Web Developer",
        "company": "Skyline web solutionss · Full-time",
        "dates": "Dec 2020 to May 2021 · 6 mos",
        "location": "Kanpur, Uttar Pradesh, India"
      }
    ],
    "Company growth signals": {
      "company_page": "https://www.linkedin.com/company/5464/",
      "followers": "2M  followers",
      "employees_on_linkedin": null
    },
    "profile_url": "https://www.linkedin.com/in/mayank-gupta-offical/"
  }
]

Confirms file save: "✅ Saved: linkedin_profile.json, linkedin_profile.csv".





