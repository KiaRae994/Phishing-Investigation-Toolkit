from report_generator import ReportGenerator

# Minimal test data
test_data = {
    'emails': [
        {'from': 'test@example.com', 'sender_email': 'test@example.com', 'date': 'Jan 12', 'subject': 'Test', 'ips': ['1.2.3.4']}
    ],
    'timeline': [],
    'infrastructure': {},
    'findings': {}
}

print("[*] Testing report generator...")
generator = ReportGenerator(test_data)
html = generator.generate_html_report()
print(f"[*] HTML generated, length: {len(html)} characters")

with open('test_report.html', 'w') as f:
    f.write(html)
print("[+] Test report saved to: test_report.html")