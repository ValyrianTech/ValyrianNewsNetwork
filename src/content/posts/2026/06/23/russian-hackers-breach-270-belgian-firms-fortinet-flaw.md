---
story_id: story_d37f05f0
title: Russian Hackers Breach 270 Belgian Firms via Fortinet Flaw
date: '2026-06-23T15:30:00Z'
meta_description: Russian hackers compromised 270 Belgian companies by exploiting
  a Fortinet vulnerability in the FortiBleed campaign, with over 100 still vulnerable.
slug: russian-hackers-breach-270-belgian-firms-fortinet-flaw
read_time_minutes: 4
word_count: 674
tags:
- Cybersecurity
- Fortinet
- Belgium
- Russian Hackers
- Supply Chain Attack
categories:
- Cybersecurity
- Technology
style: formal_news
draft: false
---
# Russian Hackers Breach 270 Belgian Firms via Fortinet Flaw

At least 270 Belgian companies and organizations have been compromised in a massive Russian cyberattack that exploited a vulnerability at cybersecurity giant Fortinet, according to a new analysis by Belgian cybersecurity firm [Secutec](https://secutec.com/nl/nieuws/secutec-en-socradar-brengen-belgische-impact-kaart-van-grootschalige-aanval-op). More than 100 of those organizations remain actively vulnerable, with hackers still holding administrator-level access to their networks as of June 22, 2026.

## The FortiBleed Campaign

The operation, dubbed "FortiBleed," began in early 2026 when hackers exploited a vulnerability in Fortinet's partner portal — the system IT service providers use to manage their clients' firewalls. By breaching this single point of access, attackers obtained login credentials for tens of thousands of organizations worldwide. [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/06/22/belgische-bedrijven-gehackt/), the Belgian public broadcaster, first reported the story on June 22.

Globally, over 75,000 compromised Fortinet firewalls have been identified, with more than 110 million login credentials intercepted. The attack is linked to a Russian hacker collective described by researchers as "strikingly well-organized and orchestrated" and of "unprecedented scale."

## Weak Security Practices Exposed

Secutec's investigation revealed alarming security deficiencies among affected organizations. None of the firewalls examined had multi-factor authentication (MFA) activated. IT partners frequently used identical passwords across multiple clients, and 85 percent of affected systems were not running the latest firmware, leaving known vulnerabilities unpatched.

"We've already found 1,300 cases of firewalls accessible with username 'admin' and password 'admin'. That simply cannot be," said Geert Baudewijns, CEO of Secutec, in an interview with VRT NWS.

## A New Model of Cybercrime

The FortiBleed campaign represents a fundamental shift in cybercriminal tactics. Rather than encrypting data and demanding ransom — the traditional ransomware model — attackers are now focused on stealing access and data for sale on the dark web, a practice known as "Initial Access Brokerage."

"Where ransomware attacks were previously mainly focused on encrypting data, the focus is now shifting to stealing and trading access and data," Baudewijns explained. "We describe this as Initial Access Brokerage."

In Belgium alone, hackers have already created new accounts on at least 45 systems, preparing access for sale on dark web marketplaces. The attackers installed a tool called "FortigateSniffer" to monitor network traffic and intercept credentials across dozens of protocols. Stolen data is then cracked, enriched, and used to penetrate deeper into internal systems.

## Ongoing Risk and Response

The attackers' infrastructure remains operational, with daily new compromises reported. The affected Belgian organizations span multiple sectors, including transport companies, law firms, school groups, government agencies, and small-to-medium enterprises.

Secutec has informed the Centre for Cybersecurity Belgium (CCB) and European national Computer Emergency Response Teams (CERTs) about the breach. The company is urging all organizations using Fortinet solutions to take immediate action, including updating systems, activating multi-factor authentication, and auditing access credentials.

## Implications for the Cybersecurity Landscape

"FortiBleed illustrates how vulnerable the current IT service ecosystem has become, where a single weak link can lead to access to hundreds of organizations at once," Baudewijns warned. "We expect this kind of large-scale supply chain attack to only increase in the coming years."

The breach carries significant implications. Affected organizations may face regulatory penalties under GDPR and the EU's NIS2 Directive for inadequate security measures. Cyber insurance premiums are expected to rise, with underwriting criteria tightening substantially. The incident also raises urgent questions about the security practices of major cybersecurity vendors themselves.

## What to Watch For

As the investigation continues, several key questions remain unanswered. Fortinet has yet to issue a public statement detailing the specific vulnerability exploited in its partner portal. The full global scale of the breach may extend well beyond the 75,000 firewalls already identified, and it remains unclear how many of the 270 affected Belgian organizations have been individually notified. The CCB is expected to issue specific guidance for Belgian organizations in the coming days.

For now, the message from cybersecurity experts is clear: organizations must treat their network security as an active, ongoing responsibility — not a one-time setup. With supply chain attacks on the rise, a single weak password can open the door to hundreds of victims.