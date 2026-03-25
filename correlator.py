from collections import Counter
from datetime import datetime
import re

class PatternCorrelator:
    def __init__(self, emails_data):
        self.emails = emails_data
    
    def find_common_domains(self):
        """Find which sender domains appear most"""
        domains = []
        for email in self.emails:
            if 'sender_email' in email and '@' in email['sender_email']:
                domain = email['sender_email'].split('@')[-1]
                domains.append(domain)
        
        return Counter(domains).most_common()
    
    def find_account_rotation_pattern(self):
        """Build timeline of senders to spot rotations"""
        timeline = []
        
        for email in self.emails:
            if 'sender_email' in email:
                domain = email['sender_email'].split('@')[-1]
                
                # Try to parse date
                date_str = email.get('date', '')
                try:
                    # This is simplified - real date parsing is trickier
                    date_obj = datetime.now()
                except:
                    date_obj = None
                
                timeline.append({
                    'date': date_str,
                    'sender': email['sender_email'],
                    'domain': domain,
                    'type': 'internal' if 'sau.edu' in domain else 'external'
                })
        
        # Sort by date if possible
        return timeline
    
    def calculate_attack_gaps(self):
        """Find time gaps between emails"""
        # Extract dates (simplified - you'd need proper date parsing)
        dates = []
        for email in self.emails:
            if email.get('date') and email['date'] != 'Unknown':
                dates.append(email['date'])
        
        # Just return the sequence for now
        return {'email_sequence': dates}

# Test
if __name__ == '__main__':
    test_data = [
        {'sender_email': 'attacker@gmail.com', 'date': 'Mon, 12 Jan 2026'},
        {'sender_email': 'hacker@yahoo.com', 'date': 'Wed, 14 Jan 2026'},
        
    ]
    test = PatternCorrelator(test_data)
    print("Common domains:", test.find_common_domains())