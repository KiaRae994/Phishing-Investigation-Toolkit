# Phishing Investigation Toolkit

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![Project](https://img.shields.io/badge/Project-Cybersecurity%20Toolkit-orange.svg)

A Python toolkit that automates phishing email investigation. Parses email headers, extracts artifacts, performs WHOIS lookups, detects anomalous patterns, and generates professional HTML reports.

## Background

While studying cybersecurity, I became interested in how phishing emails are structured and how investigators analyze them manually. To better understand the process, I collected email samples (with all sensitive information removed) and manually traced their headers, origins, and patterns.

The manual process was educational but slow, taking up to an hour per email. To scale this analysis and make it repeatable, I built a Python toolkit that automates the investigation workflow, reducing analysis time from hours to seconds.

*Note: All email samples used in development were sanitized of any personally identifiable information. No live systems were accessed without authorization.*

## What This Toolkit Does

- **Email Parsing** – Extracts headers, sender info, and IP addresses from `.eml` files
- **Anomalous Account Detection** – Identifies patterns consistent with suspicious accounts
- **Fake Identity Detection** – Flags sender patterns with no legitimate digital footprint
- **WHOIS Enrichment** – Looks up domain registration details for attacker infrastructure
- **Pattern Correlation** – Detects account rotation and attack timelines
- **HTML Reports** – Generates formatted investigation reports ready for sharing

## How I Built It

**What I wrote:**
- Email header parsing logic using Python's `email` module
- Pattern matching algorithms for account detection
- HTML report generation and data formatting
- Integration with WHOIS and DNS lookup services

**Resources I used:**
- Python standard library documentation
- `python-whois` and `requests` library documentation
- Stack Overflow for specific debugging questions

Every function was written by me, tested on sanitized email samples, and refined through iterative debugging.

## Privacy Notice

All sensitive information has been sanitized for public release:
- University name → `[UNIVERSITY]` (placeholder only)
- Real names → `Student 2015`, `Fake User`, etc.
- Email domains → `example.edu`
- Personal contact info → `[PROFESSOR A]`, `[PHONE]`

These placeholders are for structural demonstration only and do not refer to any real institution, person, or organization.

## Responsible Use

This toolkit is for educational and authorized security testing only. Users are responsible for complying with all applicable laws and organizational policies.

## Quick Start

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
## Run the toolkit on sample data
python main_github.py --folder emails --output investigation_report.html

## Don't have suspicious emails to test with? Create sample data:

Create sample data to test with
 python main_github.py --create-sample

## Run the toolkit on sample data
 
 python main_github.py --output my_first_report.html

## Open the report

 start my_first_report.html  # On Windows

 open my_first_report.html    # On Mac
 
## Example
Phishing Campaign Investigation Report
Generated: March 20, 2026

Executive Summary
- 3 emails analyzed
- 2 compromised internal accounts found
- 1 completely fabricated identity discovered
- 5 unique attacker IPs identified






### Clone the repository
```bash
git clone https://github.com/KiaRae994/Phishing-Investigation-Toolkit.git
cd Phishing-Investigation-Toolkit994/Phishing-Investigation-Toolkit.git
cd Phishing-Investigation-Toolkit





