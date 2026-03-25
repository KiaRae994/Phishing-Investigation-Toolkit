Phishing Investigation Toolkit

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Student Project](https://img.shields.io/badge/Project-Student%20Portfolio-orange.svg)]()
[![Built During](https://img.shields.io/badge/Built%20During-Spring%20Break%202026-ff69b4.svg)]()
[![AI Assisted](https://img.shields.io/badge/AI-Assisted%20Learning-blueviolet.svg)]()
[![Based on Real Findings](https://img.shields.io/badge/Based%20on-Real%20Investigation-purple.svg)]()
[![Sanitized](https://img.shields.io/badge/Sanitized-For%20GitHub-green.svg)]()

A Python toolkit for investigating phishing campaigns, developed as a cybersecurity personal project based on a real-world phishing investigation.

About This Project

This started as a personal project that became a spring break mission.

In January 2026, while studying cybersecurity, I noticed a phishing email in my inbox. Instead of deleting it, I got curious and started investigating. Over several weeks, I discovered an active phishing campaign targeting my university.

During Spring Break 2026, I decided to take what I learned from my manual investigation and build something bigger. I challenged myself to create a Python toolkit that could automate the entire investigation process.

How This Was Built

I'm a cybersecurity student still strengthening my Python skills. This project was a collaborative learning experience:

I provided:
  - The initial idea and vision
  - The real phishing email data (sanitized for GitHub)
  - The investigation methodology and findings
  - Testing and debugging feedback
  - The passion to see it through

I learned from:
  - AI assistance (like Deepseek and Claude) to help with code structure
  - Python documentation and examples
  - Trial and error (lots of debugging!)
  - Stack Overflow and online resources

This reflects how real development works: knowing what to build, leveraging resources, and continuously learning. Every line of code taught me something new about Python, file handling, APIs, and security forensics.

Privacy Note

All sensitive information has been sanitized for public release.

The original investigation contained real university data, names, and email addresses. For this public version:
- University name → `[UNIVERSITY]`
- Real names → `Student 2015`, `Fake User`, etc.
- Email domains → `university.edu`
- Personal contact info → `[PROFESSOR A]`, `[PHONE]`

The methodology remains intact, but all identifying details have been replaced with placeholders.

 Features

- Email Parsing - Extract headers, sender info, IPs from '.eml' files
- Compromised Account Detection - Identify internal accounts used in attacks
- Fake Identity Detection - Flag accounts with no digital footprint
- WHOIS Enrichment  - Look up attacker domain registration details
- Pattern Correlation - Detect account rotation and attack timeline
- Professional HTML Reports  - Generate formatted investigation reports
- Sanitization Mode - Safe for sharing on GitHub


Project Structure


Project Timeline

- January 2026  - Discovered phishing emails, started manual investigation
- February 2026 - Completed manual investigation with detailed findings
- End of February 2026 thru March 20, 2026 - Built this Python toolkit (with AI assistance)
- Present - Sanitized and published to GitHub as a learning portfolio




 Quick Start


# Clone the repository
git clone https://github.com/yourusername/phishing-investigation-toolkit.git
cd phishing-investigation-toolkit

# Install dependencies (This must be installed to work)
pip install requests python-whois


How to Get Emails for Analysis
This toolkit analyzes emails saved as .eml files. Here's how to save emails from common providers:

Gmail / Google Workspace

- Open the suspicious email

- Click the three dots (⋯) in the top-right corner

- Select "Download message"

- Save the .eml file to your analysis folder

Outlook Web (Office 365 / Outlook.com)
- Open the email

- Click the three dots (⋯) in the email toolbar

- Select "Download" → "Download as .eml"

- Save to your analysis folder

Alternative Method (Always Works):

- Open a new blank email draft

- Drag the suspicious email from your inbox into the draft

- The email appears as an attachment

- Click the attachment dropdown and select "Download"

Outlook Desktop (Windows)
- Open the email

- Click File → Save As

- Change "Save as type" to "Outlook Message Format (.msg)"

Note: .msg files may require conversion—recommend using Outlook Web instead

Apple Mail (Mac)
- Select the email

- Click File → Save As...

- Choose "Raw Message Source" format

Save to your analysis folder

Organizing your emails

Once saved, place your .eml files in a folder:


your-project/
├── emails/              ← Create this folder
│   ├── suspicious1.eml
│   ├── suspicious2.eml
│   └── suspicious3.eml
├── main_github.py
└── ...
# Run the toolkit on sample data
python main_github.py --folder emails --output investigation_report.html

Don't have suspicious emails to test with? Create sample data:

# Create sample data to test with
python main_github.py --create-sample

# Run the toolkit on sample data
python main_github.py --output my_first_report.html

# Open the report
start my_first_report.html  # On Windows
open my_first_report.html    # On Mac

Phishing Campaign Investigation Report
Generated: March 20, 2026

Executive Summary
- 3 emails analyzed
- 2 compromised internal accounts found
- 1 completely fabricated identity discovered
- 5 unique attacker IPs identified


