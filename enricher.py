import subprocess
import requests
import json
import platform

class ArtifactEnricher:
    def __init__(self):
        self.whois_cache = {}
        self.ip_cache = {}
    
    def whois_lookup(self, domain):
        """Run WHOIS lookup on a domain"""
        # This checks the cache first
        if domain in self.whois_cache:
            return self.whois_cache[domain]
        
        try:
            # Adding different commands for Windows vs Mac
            if platform.system() == 'Windows':
                cmd = ['whois.exe', domain]
            else:
                cmd = ['whois', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            # Parsing out key information
            parsed = {}
            important = ['Domain Name:', 'Registrant:', 'Creation Date:', 'Expiry Date:', 'Name Server:']
            
            for line in result.stdout.split('\n'):
                for key in important:
                    if line.startswith(key):
                        parsed[key] = line.split(':', 1)[1].strip() if ':' in line else ''
            
            # Cache it
            self.whois_cache[domain] = parsed
            return parsed
            
        except Exception as e:
            print(f"WHOIS lookup failed for {domain}: {e}")
            return {'error': str(e)}
    
    def ip_geolocate(self, ip):
        """Get location info for an IP using free API"""
        if ip in self.ip_cache:
            return self.ip_cache[ip]
        
        try:
            # Using free ip-api.com (no API key needed)
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            data = response.json()
            
            result = {
                'ip': ip,
                'country': data.get('country', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'isp': data.get('isp', 'Unknown'),
                'org': data.get('org', 'Unknown'),
                'as': data.get('as', 'Unknown')
            }
            
            self.ip_cache[ip] = result
            return result
            
        except Exception as e:
            print(f"IP lookup failed for {ip}: {e}")
            return {'ip': ip, 'error': str(e)}

# This is quick test to see if it if runs directly
if __name__ == '__main__':
    test = ArtifactEnricher()
    print("Testing WHOIS on google.com...")
    result = test.whois_lookup('google.com')
    print(json.dumps(result, indent=2))