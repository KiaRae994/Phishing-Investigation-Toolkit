# This toolkit was developed based on a real phishing investigation 
# conducted in January-February 2026. All sensitive data from the 
# original investigation has been sanitized for public release.
# The methodology reflects techniques used in the actual case.

import argparse
from emailparser import PhishingInvestigator
from enricher import ArtifactEnricher
from correlator import PatternCorrelator
from report_generator import ReportGenerator
import glob
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Phishing Investigation Toolkit (Demo Version)')
    parser.add_argument('--emails', '-e', nargs='+', help='Email files to analyze')
    parser.add_argument('--output', '-o', default='demo_report.html', help='Output report file')
    parser.add_argument('--create-sample', '-c', action='store_true', help='Create sample data folder')
    args = parser.parse_args()
    
    # Creating sample data if requested
    if args.create_sample:
        create_sample_data()
        print("[+] Created sample_data folder with example .eml files")
        return
    
    # This finds all the email files
    email_files = []
    
    # If the files are specified, use them
    if args.emails:
        for pattern in args.emails:
            email_files.extend(glob.glob(pattern))
        print(f"[*] Found {len(email_files)} email files from command line")
    
    # If no files are specified, look in sample_data folder
    if not email_files and os.path.exists('sample_data'):
        email_files = glob.glob("sample_data/*.eml")
        print(f"[*] Using sample data from sample_data/ folder: {len(email_files)} files found")
    
    # If still no files, show help
    if not email_files:
        print("[!] No email files found.")
        print("\n Options:")
        print("    1. Create sample data: python main_github.py --create-sample")
        print("    2. Specify your own files: python main_github.py --emails yourfile.eml")
        print("    3. Create a 'sample_data' folder with .eml files")
        return
    
    print(f"[*] Processing {len(email_files)} sample email files...")
    
    # Parse emails
    print("[*] Parsing email files...")
    investigator = PhishingInvestigator()
    successful_parses = 0
    
    for email_file in email_files:
        try:
            print(f"Processing: {os.path.basename(email_file)}")
            data = investigator.parse_email_file(email_file)
            if data:
                successful_parses += 1
                print(f"Parsed: {data.get('from', 'Unknown')[:50]}")
            else:
                print(f"Failed to parse: {os.path.basename(email_file)}")
        except Exception as e:
            print(f"Error parsing {os.path.basename(email_file)}: {e}")
    
    print(f"[*] Successfully parsed: {successful_parses}/{len(email_files)} emails")
    
    if successful_parses == 0:
        print("[!] No emails were successfully parsed. Exiting.")
        return
    
    print("[*] Preparing data for sanitized report...")
    
    report_data = {
        'emails': investigator.emails,
        'timeline': [],
        'infrastructure': {},
        'findings': {}
    }
    
    print("[*] Generating sanitized report for GitHub...")
    print("All university names will be replaced with [UNIVERSITY]")
    print("All real names will be replaced with placeholders")
    print("Email addresses will be anonymized")
    
    try:
        generator = ReportGenerator(report_data, sanitize_for_github=True)
        html_report = generator.generate_html_report()
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(html_report)
        
        # This creates a simple text version for quick viewing
        with open('demo_summary.txt', 'w', encoding='utf-8') as f:
            f.write("PHISHING INVESTIGATION TOOLKIT - DEMO SUMMARY\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Total emails analyzed: {len(investigator.emails)}\n")
            f.write(f"Sanitized for GitHub: YES\n")
            f.write(f"Report generated: {args.output}\n\n")
            f.write("All sensitive information has been replaced with placeholders.\n")
            f.write("This demonstrates the methodology without exposing real data.\n")
        
        print(f"\n[+]  Demo report saved to: {args.output}")
        print(f"[+]  Summary saved to: demo_summary.txt")
        print("\n" + "="*50)
        print("\n FYI: Never commit your real 'emails' folder!")
        
    except Exception as e:
        print(f"[!] ERROR generating report: {e}")
        import traceback
        traceback.print_exc()

def create_sample_data():
    """Create sample email files for demonstration"""
    
    # This creates the sample_data folder
    if not os.path.exists('sample_data'):
        os.makedirs('sample_data')
    
    # Sample email 1 - Fake identity
    sample1 = """From: "Fake Identity" <fake@university.edu>
Date: Mon, 12 Jan 2026 10:00:00 -0600
Subject: Important: Account Verification Required
Message-ID: <sample1@demo.local>
Received: from mail.university.edu (192.0.2.1)
Received: from proxy.attacker.net (198.51.100.50)

This is a sample phishing email for demonstration purposes.
All names and addresses are fictional.
"""
    
    # Sample email 2 - Compromised student account
    sample2 = """From: "Student 2020" <student2020@university.edu>
Date: Wed, 14 Jan 2026 14:30:00 -0600
Subject: Remote Job Opportunity
Message-ID: <sample2@demo.local>
Received: from mail.university.edu (192.0.2.1)
Received: from mail.attacker-domain.com (203.0.113.100)

This demonstrates a compromised student account.
"""
    
    # Sample email 3 - External attacker domain
    sample3 = """From: "Attacker Alias" <attacker@domain.com>
Date: Fri, 16 Jan 2026 09:15:00 -0600
Subject: Research Assistant Position
Message-ID: <sample3@demo.local>
Received: from mail.domain.com (203.0.113.200)
Received: from proxy.attacker.net (198.51.100.75)

This demonstrates an external attacker domain.
"""
    
    # This writes the files
    with open('sample_data/fake_identity.eml', 'w', encoding='utf-8') as f:
        f.write(sample1)
    
    with open('sample_data/compromised_student.eml', 'w', encoding='utf-8') as f:
        f.write(sample2)
    
    with open('sample_data/external_domain.eml', 'w', encoding='utf-8') as f:
        f.write(sample3)
    
    print("[+] Created 3 sample email files in 'sample_data/' folder:")
    print("fake_identity.eml - Demonstrates fake identity detection")
    print("compromised_student.eml - Demonstrates compromised account")
    print("external_domain.eml - Demonstrates external attacker domain")

if __name__ == '__main__':
    main()