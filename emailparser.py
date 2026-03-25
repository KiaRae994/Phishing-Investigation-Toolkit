import re
from email import policy
from email.parser import BytesParser
from datetime import datetime

class PhishingInvestigator:
    def __init__(self):
        self.emails = []  # This will store all parsed emails
    
    def parse_email_file(self, filepath):
        """Read and extract info from an email file"""
        try:
            with open(filepath, 'rb') as f:
                msg = BytesParser(policy=policy.default).parse(f)
            
            # Get the 'From' field
            from_field = msg.get('From', 'Unknown')
            
            # Extract email address using regex
            email_match = re.search(r'<(.+?)>', from_field)
            if email_match:
                sender_email = email_match.group(1)
            else:
                sender_email = from_field
            
            # Get received headers (this hides the IPs)
            received = msg.get_all('Received', [])
            ips = []
            ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
            
            for header in received:
                found_ips = re.findall(ip_pattern, str(header))
                ips.extend(found_ips)
            
            # This builds the email data dictionary
            email_data = {
                'date': msg.get('Date', 'Unknown'),
                'from': from_field,
                'sender_email': sender_email,
                'subject': msg.get('Subject', 'No Subject'),
                'return_path': msg.get('Return-Path', 'Unknown'),
                'message_id': msg.get('Message-ID', 'Unknown'),
                'ips': list(set(ips))  
            } # Removes duplicates
            
            # Reminder, this adds to our collection 
            self.emails.append(email_data)
            return email_data
            
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return None

# This is to test to see if it runs directly
if __name__ == '__main__':
    test = PhishingInvestigator()
    print("Email parser ready!")