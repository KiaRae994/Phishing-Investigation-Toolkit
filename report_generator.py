from datetime import datetime
import html

class ReportGenerator:
    def __init__(self, report_data, sanitize_for_github=False):
        self.emails = report_data.get('emails', [])
        self.timeline = report_data.get('timeline', [])
        self.infrastructure = report_data.get('infrastructure', {})
        self.findings = report_data.get('findings', {})
        self.sanitize_for_github = sanitize_for_github
    
    def sanitize_text(self, text):
        """Replace real school names and identities with placeholders for GitHub"""
        if not self.sanitize_for_github:
            return text
        
        # This converts into a string if needed
        text = str(text)
        
        # Replaces university identifiers
        text = text.replace('St. Ambrose University', '[UNIVERSITY]')
        text = text.replace('St. Ambrose', '[UNIVERSITY]')
        text = text.replace('sau.edu', 'university.edu')
        text = text.replace('@sau.edu', '@university.edu')
        text = text.replace('SAU', '[U]')
        
        # Replaces real names from your investigation
        text = text.replace('Amy Waters', 'Fake User')
        text = text.replace('Amy C. Waters', 'Fake Identity')
        text = text.replace('Daniel Woulfe', 'Student 2020')
        text = text.replace('Daniel M. Woulfe', 'Student 2020')
        text = text.replace('Mariah Balinski', 'Student 2015')
        text = text.replace('Kaitlyn van Weelden', 'Student 2017')
        text = text.replace('Kaitlyn Van Weelden', 'Student 2017')
        text = text.replace('Jordon Williams', 'Student 2024')
        
        # Replaces professor names mentioned in your investigation
        text = text.replace('Chenguang Zhao', '[PROFESSOR A]')
        text = text.replace('Kevin Lillis', '[PROFESSOR B]')
        text = text.replace('Emily Kingery', '[PROFESSOR C]')
        text = text.replace('Lisa Thimm', '[PROFESSOR D]')
        text = text.replace('Timothy Gillespie', '[PROFESSOR E]')
        
        # Replaces Brazilian contact info (protect the real person too)
        text = text.replace('Gabriel Sousa', 'Attacker Alias')
        text = text.replace('gabrielsousa@stine.com.br', 'attacker@domain.com')
        text = text.replace('Rafael Junqueira Toro', '[REGISTRANT NAME]')
        
        # Replaces phone numbers
        text = text.replace('612-223-3210', '[PHONE]')
        text = text.replace('509-200-3350', '[PHONE]')
        text = text.replace('646-228-9980', '[PHONE]')
        text = text.replace('332-283-6380', '[PHONE]')

        # Replaces any other identifying info
        text = text.replace('stine.com.br', 'attacker-domain.com')
        text = text.replace('srvbr2.com.br', 'hosting-domain.com')
        
        
        return text
    
    def sanitize_dict(self, data):
        """Recursively sanitize all string values in a dictionary"""
        if not self.sanitize_for_github:
            return data
            
        if isinstance(data, dict):
            return {key: self.sanitize_dict(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.sanitize_dict(item) for item in data]
        elif isinstance(data, str):
            return self.sanitize_text(data)
        else:
            return data
    
    def generate_html_report(self):
        """Create a professional HTML report matching your investigation style"""
        
        # Sanitizes all data if needed
        if self.sanitize_for_github:
            self.emails = self.sanitize_dict(self.emails)
            self.infrastructure = self.sanitize_dict(self.infrastructure)
        
        # Analyzes the data like you would manually
        compromised_accounts = []
        fake_accounts = []
        external_domains = set()
        attacker_ips = set()
        
        for email in self.emails:
            sender = email.get('sender_email', '')
            display_name = email.get('from', 'Unknown')
            
            # Checks for the fake Amy Waters account
            if 'fake' in display_name.lower() and 'identity' in display_name.lower() and self.sanitize_for_github:
                fake_accounts.append({
                    'email': sender,
                    'display': display_name,
                    'date': email.get('date', 'Unknown'),
                    'reason': 'Completely fabricated identity - no digital footprint'
                })
            elif 'amy' in display_name.lower() and 'waters' in display_name.lower() and not self.sanitize_for_github:
                fake_accounts.append({
                    'email': sender,
                    'display': display_name,
                    'date': email.get('date', 'Unknown'),
                    'reason': 'Completely fabricated identity - no digital footprint'
                })
            
            if 'university.edu' in sender or ('sau.edu' in sender and not self.sanitize_for_github):
                compromised_accounts.append({
                    'email': sender,
                    'display': display_name,
                    'date': email.get('date', 'Unknown')
                })
            elif 'edu' in sender and not any(external in sender for external in external_domains):
                # Trying to identify other edu accounts as internal
                compromised_accounts.append({
                    'email': sender,
                    'display': display_name,
                    'date': email.get('date', 'Unknown')
                })
            else:
                domain = sender.split('@')[-1] if '@' in sender else 'Unknown'
                if domain and domain not in ['university.edu', 'edu']:
                    external_domains.add(domain)
            
            # Collecting IPs (filter out private/internal IPs)
            for ip in email.get('ips', []):
                if ip not in ['127.0.0.1', '10.0.0.0/8', '192.168.0.0/16'] and not ip.startswith(('10.', '192.168.', '172.')):
                    attacker_ips.add(ip)
        
        # Builds header with sanitization notice if needed
        sanitization_notice = ""
        if self.sanitize_for_github:
            sanitization_notice = """
            <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin-bottom: 20px; border-radius: 0 5px 5px 0;">
                <strong> SANITIZED FOR GITHUB</strong> - All university names, real identities, and sensitive information have been replaced with placeholders. This is a demonstration version.
            </div>
            """
        
        #HTML/CSS
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESE - Phishing Investigation Report {"(Demo)" if self.sanitize_for_github else ""}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'SF Pro Text', system-ui, sans-serif;
            background: #f8fafc;
            color: #0f172a;
            line-height: 1.5;
        }}
        
        /* Import Inter font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&display=swap');
        
        .report-container {{
            max-width: 1440px;
            margin: 0 auto;
            padding: 24px;
        }}
        
        /* Glassmorphism header */
        .hero {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-radius: 32px;
            padding: 48px;
            margin-bottom: 32px;
            position: relative;
            overflow: hidden;
        }}
        
        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, rgba(59,130,246,0.15) 0%, transparent 70%);
            pointer-events: none;
        }}
        
        .hero-content {{
            position: relative;
            z-index: 1;
        }}
        
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 6px 14px;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 500;
            color: #94a3b8;
            margin-bottom: 24px;
        }}
        
        .hero-badge .dot {{
            width: 8px;
            height: 8px;
            background: #10b981;
            border-radius: 50%;
            display: inline-block;
            animation: pulse 2s infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.5; transform: scale(1.2); }}
        }}
        
        .hero h1 {{
            font-size: 3rem;
            font-weight: 700;
            color: white;
            margin-bottom: 16px;
            letter-spacing: -0.02em;
        }}
        
        .hero p {{
            color: #94a3b8;
            font-size: 1.1rem;
            max-width: 600px;
        }}
        
        .meta-info {{
            display: flex;
            gap: 32px;
            margin-top: 32px;
            padding-top: 24px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}
        
        .meta-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .meta-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-weight: 600;
        }}
        
        .meta-value {{
            color: white;
            font-weight: 500;
            font-size: 0.9rem;
        }}
        
        /* Card grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 32px;
        }}
        
        .stat-card {{
            background: white;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px -12px rgba(0,0,0,0.1);
            border-color: #cbd5e1;
        }}
        
        .stat-icon {{
            font-size: 2rem;
            margin-bottom: 16px;
        }}
        
        .stat-number {{
            font-size: 2.5rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
            margin-bottom: 4px;
        }}
        
        .stat-label {{
            color: #64748b;
            font-size: 0.85rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}
        
        /* Section styling */
        .section {{
            background: white;
            border-radius: 24px;
            padding: 32px;
            margin-bottom: 32px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }}
        
        .section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
        }}
        
        .section-title {{
            font-size: 1.5rem;
            font-weight: 600;
            color: #0f172a;
            letter-spacing: -0.01em;
        }}
        
        .section-badge {{
            background: #f1f5f9;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
            color: #475569;
        }}
        
        /* Critical alert */
        .critical-alert {{
            background: linear-gradient(135deg, #fef2f2 0%, #fff5f5 100%);
            border-left: 4px solid #dc2626;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 32px;
            border: 1px solid #fee2e2;
        }}
        
        .critical-alert .alert-title {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }}
        
        .critical-alert .alert-icon {{
            font-size: 1.5rem;
        }}
        
        .critical-alert h3 {{
            color: #dc2626;
            font-size: 1.1rem;
            font-weight: 600;
            margin: 0;
        }}
        
        .critical-alert p {{
            color: #991b1b;
            margin-bottom: 16px;
        }}
        
        .critical-alert ul {{
            color: #7f1a1a;
            margin-left: 20px;
        }}
        
        .critical-alert li {{
            margin: 8px 0;
        }}
        
        /* Table styling */
        .table-wrapper {{
            overflow-x: auto;
            border-radius: 16px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        
        th {{
            text-align: left;
            padding: 16px;
            background: #f8fafc;
            font-weight: 600;
            color: #1e293b;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            border-bottom: 1px solid #e2e8f0;
        }}
        
        td {{
            padding: 16px;
            border-bottom: 1px solid #f1f5f9;
            font-size: 0.9rem;
        }}
        
        tr:hover {{
            background: #fafcff;
        }}
        
        /* Badges */
        .badge {{
            display: inline-flex;
            align-items: center;
            padding: 4px 12px;
            border-radius: 40px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.02em;
        }}
        
        .badge-critical {{
            background: #dc2626;
            color: white;
        }}
        
        .badge-warning {{
            background: #f59e0b;
            color: white;
        }}
        
        .badge-info {{
            background: #3b82f6;
            color: white;
        }}
        
        .badge-secondary {{
            background: #64748b;
            color: white;
        }}
        
        /* Timeline */
        .timeline {{
            position: relative;
        }}
        
        .timeline-item {{
            display: flex;
            gap: 20px;
            padding: 20px 0;
            border-bottom: 1px solid #f1f5f9;
        }}
        
        .timeline-marker {{
            flex-shrink: 0;
            width: 40px;
            text-align: center;
        }}
        
        .timeline-date {{
            font-size: 0.75rem;
            font-weight: 600;
            color: #3b82f6;
            background: #eff6ff;
            padding: 4px 8px;
            border-radius: 8px;
            display: inline-block;
        }}
        
        .timeline-content {{
            flex: 1;
        }}
        
        .timeline-title {{
            font-weight: 600;
            color: #0f172a;
            margin-bottom: 4px;
        }}
        
        .timeline-subtitle {{
            font-size: 0.8rem;
            color: #64748b;
            margin-bottom: 8px;
        }}
        
        .timeline-tags {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        
        .tag {{
            font-size: 0.7rem;
            padding: 2px 8px;
            background: #f1f5f9;
            border-radius: 12px;
            color: #475569;
        }}
        
        /* Recommendations */
        .recommendation-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }}
        
        .recommendation-card {{
            background: #f8fafc;
            border-radius: 20px;
            padding: 24px;
            border: 1px solid #e2e8f0;
            transition: all 0.2s;
        }}
        
        .recommendation-card:hover {{
            transform: translateY(-2px);
            border-color: #cbd5e1;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}
        
        .rec-number {{
            width: 32px;
            height: 32px;
            background: #0f172a;
            color: white;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            margin-bottom: 16px;
        }}
        
        .rec-title {{
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 12px;
            color: #0f172a;
        }}
        
        .rec-description {{
            font-size: 0.85rem;
            color: #475569;
            line-height: 1.5;
        }}
        
        /* IP List */
        .ip-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }}
        
        .ip-item {{
            background: #f1f5f9;
            padding: 8px 16px;
            border-radius: 40px;
            font-family: 'SF Mono', 'Courier New', monospace;
            font-size: 0.85rem;
            color: #0f172a;
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 32px;
            color: #64748b;
            font-size: 0.8rem;
            border-top: 1px solid #e2e8f0;
            margin-top: 32px;
        }}
        
        @media (max-width: 768px) {{
            .stats-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .recommendation-grid {{
                grid-template-columns: 1fr;
            }}
            .hero {{
                padding: 32px;
            }}
            .hero h1 {{
                font-size: 2rem;
            }}
            .meta-info {{
                flex-direction: column;
                gap: 16px;
            }}
        }}
        
        /* Code block */
        code {{
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>
    <div class="report-container">
        <!-- Hero Section -->
        <div class="hero">
            <div class="hero-content">
                <div class="hero-badge">
                    <span class="dot"></span>
                    <span>ACTIVE INCIDENT RESPONSE</span>
                </div>
                <h1>Phishing Investigation<br>Report</h1>
                <p>Enterprise Security Edition • Comprehensive threat analysis & incident response</p>
                <div class="meta-info">
                    <div class="meta-item">
                        <span class="meta-label">INVESTIGATION ID</span>
                        <span class="meta-value">{'DEMO' if self.sanitize_for_github else 'ESE'}-{datetime.now().strftime('%Y%m')}-001</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">GENERATED</span>
                        <span class="meta-value">{datetime.now().strftime('%B %d, %Y at %H:%M')}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">INVESTIGATOR</span>
                        <span class="meta-value">Security Operations Team</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">CLASSIFICATION</span>
                        <span class="meta-value">{'DEMO DATA' if self.sanitize_for_github else 'CONFIDENTIAL'}</span>
                    </div>
                </div>
            </div>
        </div>
        
        {sanitization_notice}
        
        <!-- Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon"></div>
                <div class="stat-number">{len(self.emails)}</div>
                <div class="stat-label">Emails Analyzed</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"></div>
                <div class="stat-number">{len(compromised_accounts)}</div>
                <div class="stat-label">Compromised Accounts</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"></div>
                <div class="stat-number">{len(fake_accounts)}</div>
                <div class="stat-label">Fake Identities</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"></div>
                <div class="stat-number">{len(attacker_ips)}</div>
                <div class="stat-label">Attacker IPs</div>
            </div>
        </div>
        
        <!-- Critical Finding -->
        <div class="critical-alert">
            <div class="alert-title">
                <span class="alert-icon"></span>
                <h3>CRITICAL: Direct System Access Confirmed</h3>
            </div>
            <p><strong>Fake Identity Detection:</strong> A sender with <strong>zero digital footprint</strong> (no search results, social media, or public records) successfully sent emails from an internal account.</p>
            <ul>
                <li>Attackers can <strong>create or compromise accounts</strong> within the email system</li>
                <li><strong>Display name manipulation</strong> enables fictitious identity creation</li>
                <li>Traditional identity verification methods are <strong>ineffective</strong></li>
                <li><strong>Active attacker presence confirmed</strong> in production environment</li>
            </ul>
        </div>
        
        <!-- Compromised Accounts Section -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Compromised Accounts</h2>
                <span class="section-badge">{len(compromised_accounts)} total</span>
            </div>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Display Name</th>
                            <th>Account Email</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
"""
        
        # Adding compromised accounts
        for account in sorted(compromised_accounts, key=lambda x: x.get('date', '')):
            display = account.get('display', '')
            is_fake = ('fake' in display.lower() or 'identity' in display.lower()) if self.sanitize_for_github else ('amy' in display.lower() and 'waters' in display.lower())
            badge = '<span class="badge badge-critical">FAKE IDENTITY</span>' if is_fake else '<span class="badge badge-warning">COMPROMISED</span>'
            
            html_content += f"""
                        <tr>
                            <td>{html.escape(str(account.get('date', 'Unknown'))[:16])}</td>
                            <td><strong>{html.escape(str(account.get('display', 'Unknown')))}</strong></td>
                            <td><code>{html.escape(str(account.get('email', 'Unknown')))}</code></td>
                            <td>{badge}</td>
                        </tr>
            """
        
        html_content += f"""
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Attacker Infrastructure -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Attacker Infrastructure</h2>
                <span class="section-badge">{len([d for d in self.infrastructure.keys() if 'university' not in d and 'edu' not in d])} domains</span>
            </div>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Domain</th>
                            <th>Registrar</th>
                            <th>Creation Date</th>
                            <th>Nameservers</th>
                        </tr>
                    </thead>
                    <tbody>
"""
        
        # Add infrastructure
        for domain, info in self.infrastructure.items():
            if 'university' not in domain and 'edu' not in domain:
                nameservers = info.get('name_servers', [])
                if isinstance(nameservers, list):
                    ns_display = ', '.join([str(ns) for ns in nameservers[:2]])
                else:
                    ns_display = str(nameservers)[:50]
                
                html_content += f"""
                        <tr>
                            <td><code>{html.escape(str(domain))}</code></td>
                            <td>{html.escape(str(info.get('registrar', 'Unknown')))}</td>
                            <td>{html.escape(str(info.get('creation_date', 'Unknown')))}</td>
                            <td><code>{html.escape(str(ns_display))}</code></td>
                        </tr>
                """
        
        html_content += f"""
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Attacker IPs -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Attacker IP Addresses</h2>
                <span class="section-badge">{len(attacker_ips)} unique</span>
            </div>
            <div class="ip-list">
"""
        
        for ip in attacker_ips:
            html_content += f'<span class="ip-item"><code>{html.escape(str(ip))}</code></span>'
        
        html_content += f"""
            </div>
        </div>
        
        <!-- Attack Timeline -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Attack Timeline</h2>
                <span class="section-badge">{len(self.emails)} events</span>
            </div>
            <div class="timeline">
"""
        
        # Create timeline
        sorted_emails = sorted(self.emails, key=lambda x: str(x.get('date', '')))
        for email in sorted_emails:
            date = str(email.get('date', 'Unknown'))[:16]
            sender = str(email.get('from', 'Unknown'))
            subject = str(email.get('subject', 'Unknown'))[:60]
            ips = [str(ip) for ip in email.get('ips', [])]
            
            fake_flag = "fake-identity" if (('fake' in sender.lower() or 'identity' in sender.lower()) and self.sanitize_for_github) or (not self.sanitize_for_github and 'amy' in sender.lower() and 'waters' in sender.lower()) else ""
            
            html_content += f"""
                <div class="timeline-item">
                    <div class="timeline-marker">
                        <span class="timeline-date">{html.escape(date)}</span>
                    </div>
                    <div class="timeline-content">
                        <div class="timeline-title">{html.escape(sender)}</div>
                        <div class="timeline-subtitle">{html.escape(subject)}</div>
                        <div class="timeline-tags">
                            {f'<span class="tag"> FAKE IDENTITY</span>' if fake_flag else ''}
                            {''.join([f'<span class="tag"><code>{ip}</code></span>' for ip in ips[:2]])}
                        </div>
                    </div>
                </div>
            """
        
        html_content += f"""
            </div>
        </div>
        
        <!-- Critical Findings Summary -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Key Findings</h2>
                <span class="section-badge">3 critical</span>
            </div>
            <div style="display: grid; gap: 16px;">
                <div style="background: #fef2f2; border-radius: 16px; padding: 20px; border: 1px solid #fee2e2;">
                    <div style="font-weight: 600; color: #dc2626; margin-bottom: 8px;"> Finding #1: Direct System Access</div>
                    <p style="color: #991b1b; font-size: 0.9rem;">Fake identity creation confirms active attacker presence and account manipulation capabilities.</p>
                </div>
                <div style="background: #fffbeb; border-radius: 16px; padding: 20px; border: 1px solid #fef3c7;">
                    <div style="font-weight: 600; color: #d97706; margin-bottom: 8px;">Finding #2: Dormant Account Exploitation</div>
                    <p style="color: #92400e; font-size: 0.9rem;">Former student accounts from 2015-2024 remain active and are being used in attacks.</p>
                </div>
                <div style="background: #eff6ff; border-radius: 16px; padding: 20px; border: 1px solid #dbeafe;">
                    <div style="font-weight: 600; color: #2563eb; margin-bottom: 8px;"> Finding #3: Account Rotation Pattern</div>
                    <p style="color: #1e40af; font-size: 0.9rem;">Attackers rotate through compromised accounts to avoid detection patterns.</p>
                </div>
            </div>
        </div>
        
        <!-- Recommendations -->
        <div class="section">
            <div class="section-header">
                <h2 class="section-title">Remediation Actions</h2>
                <span class="section-badge">Priority: HIGH</span>
            </div>
            <div class="recommendation-grid">
                <div class="recommendation-card">
                    <div class="rec-number">1</div>
                    <div class="rec-title">Investigate Fake Identity Creation</div>
                    <div class="rec-description">Audit account creation logs, identify unauthorized activity, and scan for additional fabricated identities.</div>
                </div>
                <div class="recommendation-card">
                    <div class="rec-number">2</div>
                    <div class="rec-title">Account Remediation</div>
                    <div class="rec-description">Disable dormant accounts, enforce MFA, and audit all accounts that sent emails during the attack window.</div>
                </div>
                <div class="recommendation-card">
                    <div class="rec-number">3</div>
                    <div class="rec-title">Infrastructure Reporting</div>
                    <div class="rec-description">Report malicious IPs to hosting providers and share findings with relevant CERTs for broader protection.</div>
                </div>
            </div>
        </div>
        
        <!-- Investigator Note -->
        <div class="section" style="background: #fafcff;">
            <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="font-size: 2rem;"></div>
                <div>
                    <h3 style="font-size: 1rem; font-weight: 600; margin-bottom: 8px;">Investigator's Note</h3>
                    <p style="color: #475569; font-size: 0.85rem; line-height: 1.6;">This investigation was initiated by a security analyst who identified anomalous email patterns. All findings derived from email header analysis and publicly available intelligence data.</p>
                    {"<p style='color: #64748b; font-size: 0.8rem; margin-top: 12px;'><strong> Demo Notice:</strong> This version has been sanitized for public display. University names and real identities replaced with placeholders.</p>" if self.sanitize_for_github else ""}
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Enterprise Security Edition • Phishing Investigation Toolkit</p>
            <p style="margin-top: 8px; font-size: 0.7rem;">{"Demo Version - Sanitized for Public Distribution" if self.sanitize_for_github else "Internal Use Only - Confidential Security Report"}</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html_content