# Phishing Campaign Investigation: A 5-Week Case Study

> **Disclaimer:** This investigation was conducted independently as a learning exercise. All findings were reported to the appropriate authorities. This document has been sanitized—all identifying details have been replaced with placeholders while preserving the methodology and findings.

---

## How This Started

I received my first phishing email on January 12, 2026. Instead of deleting it, I got curious. I was bored, honestly, and that combination led me down a rabbit hole.

I started saving every suspicious email instead of reporting them. Over the next month, I watched the pattern build: different senders, different names, but the same infrastructure underneath.

On the night of February 17–18, I sat down and asked: *What's actually happening here?*

Two hours later, I had mapped the entire campaign. This document is what I found.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Timeline Overview](#timeline-overview)
3. [Critical Finding: Dormant Alumni Accounts](#critical-finding-dormant-alumni-accounts)
4. [Fabricated Identities](#fabricated-identities)
5. [Infrastructure Analysis](#infrastructure-analysis)
6. [Phone Number Analysis](#phone-number-analysis)
7. [Potential Actor Identification](#potential-actor-identification)
8. [Key Security Gaps](#key-security-gaps)
9. [Recommended Actions](#recommended-actions)
10. [Why This Toolkit Exists](#why-this-toolkit-exists)

---

## Executive Summary

Beginning in January 2026, an educational institution experienced a sustained phishing campaign targeting students, with particular focus on the Math and Technology departments. The attacks used compromised internal accounts, including dormant alumni accounts dating back to 2015. Sending phishing emails that bypassed normal filtering by appearing to come from internal senders.

**Key Findings:**
- Attackers accessed a pool of compromised alumni accounts spanning 2015–2024
- Accounts remained active years after graduation, a critical account lifecycle management gap
- Attackers rotated through accounts to avoid pattern detection
- Fabricated display names were used to hide the real account owners
- Infrastructure traced to Brazil, Canada, and the United States
- Campaign expanded from email to SMS in February 2026
- A real individual was linked to an attacker-controlled domain

---

## Timeline Overview

| Date | Event |
|------|-------|
| Jan 6, 2026 | Attacker domain owner contact updated |
| Jan 11, 2026 | Current phishing campaign begins |
| Jan 12, 2026 | First phishing email received (fabricated identity) |
| Jan 15, 2026 | Phishing received from compromised alumni account (Class of 2020) |
| Jan 15, 2026 | Institution-wide alert about phishing surge |
| Jan 26, 2026 | Phishing received from attacker-owned domain |
| Jan 28, 2026 | Phishing received from compromised alumni account (Class of 2015) |
| Feb 2, 2026 | Campaign expands to SMS (new attack vector) |
| Feb 11, 2026 | Phishing received from compromised alumni account (Class of 2017) |
| Feb 17, 2026 | Phishing received from compromised alumni account (Class of 2024) |

The 4-5 day gap between infrastructure updates and attack launch indicated premeditated planning.

---

## Critical Finding: Dormant Alumni Accounts

The email accounts sending phishing emails belonged to former students dating back to 2015. Only one sender used an attacker-owned domain; all others were legitimate institutional accounts belonging to graduates.

**Compromised Accounts Identified:**

| Date | Display Name | Class Year | Account Type |
|------|--------------|-----------|--------------|
| Jan 12 | Fabricated Identity | N/A | Fake display name on compromised account |
| Jan 15 | Student 2020 | 2020 | Compromised alumni |
| Jan 28 | Student 2015 | 2015 | Compromised alumni |
| Feb 11 | Student 2017 | 2017 | Compromised alumni |
| Feb 17 | Student 2024 | 2024 | Compromised alumni |

**Why This Matters:**
- These accounts were still active years after graduation
- Original owners were unaware the accounts were being used
- Attackers gained long-term, undetectable access
- The campaign continued for over five weeks without detection

**Root Cause:** The institution lacked an account offboarding process for graduates.

---

## Fabricated Identities

The first phishing email came from a display name that left no digital footprint. Searches across Google, LinkedIn, yearbook archives, and public records returned zero results: no social media, no university history, no obituaries, no news articles.

**What This Confirms:**
- The display name was completely fabricated
- Attackers used fake display names on top of real compromised accounts
- This allowed them to avoid name-based searches while keeping the underlying account active

**Security Implication:** If IT searched for the fabricated name alone, they would find nothing. The underlying compromised account must be investigated.

---

## Infrastructure Analysis

### Domains Identified
| Domain | Purpose |
|--------|---------|
| attacker-domain-1.com.br | Attacker-controlled domain |
| attacker-domain-2.com.br | Hosting infrastructure |
| third-party.com.br | Brazilian hosting provider (potentially compromised) |

### Nameserver Infrastructure
All nameservers remained active throughout the investigation period.

| Name Server | Hosting Provider | Location | Abuse Contact |
|-------------|-----------------|----------|---------------|
| ns1 | Provider A (Brazil) | Brazil | security@providerA.com.br |
| ns2 | Provider B (Brazil) | Brazil | abuse@providerB.com.br |
| ns3 | Provider C (US) | United States | abuse@providerC.us |
| ns4 | Provider D (Canada) | Canada | abuse@providerD.ca |

### WHOIS Evidence
Attacker-controlled domain WHOIS showed:
- Domain registered since 2008
- Owner contact updated on **January 6, 2026** - five days before the campaign launched
- Nameservers matched the infrastructure identified above

---

## Phone Number Analysis

Faculty names were used in phishing lures to increase credibility. Associated phone numbers traced to Amazon Web Services (AWS) — disposable VoIP infrastructure.

| Faculty Name (Impersonated) | Phone Number |
|----------------------------|--------------|
| Professor A | [AWS VoIP] |
| Professor B | [AWS VoIP] |
| Professor C | [AWS VoIP] |
| Professor D | [AWS VoIP] |
| Professor E | [AWS VoIP] |

**Pattern:** All numbers traced to AWS, indicating the attackers built their communication infrastructure on cloud VoIP services.

---

## Potential Actor Identification

The email address used in one phishing attempt appeared to belong to a real individual.

**Publicly Available Information:**
- Professional portfolio belonging to an individual with matching name
- Location: São Paulo, Brazil
- Technical expertise: AWS, Docker, Python/Django, cloud infrastructure
- Age: Approximately 30 years old

**Possible Explanations:**
1. Direct involvement of this individual in the phishing operation
2. Identity theft: the name and email being used without knowledge
3. Compromised account or stolen credentials

> **Note:** The individual was not contacted. Investigation of this lead should be handled by the appropriate authorities.

---

## Key Security Gaps

| Gap | Impact |
|-----|--------|
| **No account offboarding** | Dormant alumni accounts from 2015–2024 remained active |
| **Display name spoofing allowed** | Fabricated names could be used on compromised accounts |
| **No dormant account monitoring** | Attackers rotated through accounts for weeks undetected |
| **No MFA enforcement** | Compromised accounts remained accessible |
| **No faculty notification** | Faculty names were used in lures without their knowledge |

---

## Recommended Actions

| Priority | Action |
|----------|--------|
| Critical | Immediately disable all former student accounts not needed for legitimate services |
| Critical | Audit every compromised account identified in this report |
| High | Report all IPs to abuse contacts at hosting providers |
| High | Report phone numbers to AWS Abuse |
| High | Force MFA on all active accounts, especially in targeted departments |
| High | Block identified infrastructure at the firewall |
| Medium | Report findings to national CERT |
| Medium | Report to law enforcement (IC3) given cross-border nature |
| Medium | Notify faculty members whose names were used |

---

## Why This Toolkit Exists

Here's what mattered: While I could piece the investigation together quickly because I had been saving emails and observing patterns, doing this manually isn't scalable. If I had to investigate a larger campaign with hundreds of emails, those two hours would become days.

That's why I built the toolkit. It automates the entire process:

- Parses email headers from '.eml' files
- Extracts sender information, IP addresses, and authentication results
- Performs WHOIS lookups on attacker domains
- Detects compromised account patterns and fabricated identities
- Correlates timelines and account rotation
- Generates professional HTML reports

**Impact:** What I did in two hours of focused analysis can now be done in seconds—and scaled to any number of emails.

---

## Conclusion

This was not random spam. It was a targeted, professionally managed campaign exploiting a fundamental gap in account lifecycle management. The attackers established a permanent beachhead using dormant alumni accounts and rotated through them to avoid detection. The campaign ran for over five weeks, expanded to SMS, and used real faculty names to increase credibility.

All findings were reported to the appropriate university authorities and hosting provider abuse contacts. This document is shared to demonstrate the investigation methodology and the real-world problem that inspired the Phishing Investigation Toolkit.

---

## Related Resources

- **Phishing Investigation Toolkit:** [GitHub Repository](https://github.com/KiaRae994/Phishing-Investigation-Toolkit)
- **Toolkit README:** Features, installation, and usage instructions

---

*Document sanitized for public release. All identifying details replaced with placeholders. Methodology and findings preserved in full.*
