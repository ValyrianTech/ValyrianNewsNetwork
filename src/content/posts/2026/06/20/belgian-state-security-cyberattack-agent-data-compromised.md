---
story_id: story_8dc4896f
title: Belgian State Security Hit by Cyberattack, Agent Data Leaked
date: '2026-06-20T10:10:00Z'
meta_description: Belgium's VSSE intelligence service suffered a year-long cyberattack
  via Ivanti software, exposing agent names, phone numbers, and emails.
slug: belgian-state-security-cyberattack-agent-data-compromised
read_time_minutes: 5
word_count: 853
tags:
- Belgium
- VSSE
- cyberattack
- Ivanti
- state security
- data breach
categories:
- Security & Cyber
- Europe
style: formal_news
draft: false
---
# Belgian State Security Hit by Cyberattack, Agent Data Leaked

Belgium's State Security service (VSSE) has been targeted in a sophisticated cyberattack that may have compromised sensitive personal data belonging to its intelligence agents, according to reports from [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/06/20/staatsveiligheid-cyberaanval/) and [RTBF](https://www.rtbf.be/article/des-cybercriminels-ont-pirate-les-donnees-gsm-des-agents-de-la-surete-de-l-etat-11743607). The breach, which went undetected for approximately 12 months, exploited vulnerabilities in third-party security software used to protect the agency's mobile communications.

## The Breach

The attack did not originate within VSSE itself but through Ivanti, an American cybersecurity company whose Endpoint Manager Mobile (EPMM) software the agency used to secure its agents' mobile devices. Between May 2025 and spring 2026 — a period of approximately 12 months — attackers exploited two critical zero-day vulnerabilities: CVE-2026-1281 and CVE-2026-1340, both rated CVSS 9.8, the highest severity level. These flaws allow unauthenticated remote code execution, meaning attackers could run malicious code on affected systems without any credentials.

During an inspection of its IT infrastructure, VSSE discovered that cybercriminals had gained access to the mobile device management system, exposing names, surnames, phone numbers, and email addresses of agency personnel. Data belonging to individuals contacted by agents through their work phones may also have been compromised. The attackers reportedly erased logging data and implemented in-memory backdoors to cover their tracks.

Ivanti disclosed the vulnerabilities and released patches on January 29, 2026, but threat actors had already been exploiting them as zero-days. The CCB warned that patching alone is insufficient — organizations must also investigate for potential backdoors and compromised data.

## Classified Data Preserved

Crucially, the [Centre for Cybersecurity Belgium (CCB)](https://ccb.belgium.be/advisories/warning-remote-code-execution-ivanti-epmm-endpoint-manager-mobile-patch-immediately) confirmed that hackers never gained access to VSSE's internal classified network, where the most sensitive and confidential intelligence is exchanged. Human intelligence sources and classified information remain secure.

"The leak was not at the State Security itself, but at the American cybersecurity company Ivanti," reported Hanne Decré of VRT NWS. A source cited by VRT called the incident "bad" but emphasized it was "not a matter of state."

RTBF's Sébastien Georis noted: "While intelligence services make discretion one of the foundations of their work, the exposure of such information raises concerns."

## Part of a Wider European Campaign

The VSSE attack is not an isolated incident. It forms part of a broader campaign targeting European government institutions through the same Ivanti vulnerabilities. The [Hacker News](https://thehackernews.com/2026/02/dutch-authorities-confirm-ivanti-zero.html) reported that the Dutch Data Protection Authority and the Council for the Judiciary confirmed their systems were breached, exposing employee contact data. Finland's Valtori disclosed a breach affecting up to 50,000 government employees, and the European Commission detected attack traces on its central mobile device management infrastructure.

SecurityWeek [reported](https://www.securityweek.com/chinese-spies-exploit-ivanti-vulnerabilities-against-critical-sectors/) that cybersecurity firm EclecticIQ has assessed with high confidence that the broader Ivanti exploitation campaign is linked to UNC5221, a China-nexus cyberespionage group known for targeting zero-day flaws in edge devices since at least 2023. However, definitive attribution for the specific VSSE attack has not been confirmed.

## A Pattern of Supply Chain Vulnerabilities

This marks the second major cyber incident to hit the Belgian intelligence service in recent years. Between February 2021 and May 2023, Chinese hackers exploited a vulnerability in Barracuda security software to intercept approximately 10% of VSSE's incoming and outgoing email traffic. As with the current incident, classified data remained secure, but personal data may have been stolen. No formal link has been established between the two attacks.

Both attacks exploited vulnerabilities in American security software — Barracuda in the first incident and Ivanti in the second — highlighting the risks of supply chain dependencies in sensitive government operations. The pattern raises questions about the reliance of European intelligence agencies on a small number of foreign cybersecurity vendors.

## Analysis: Implications for European Security

The exposure of agent identities, phone numbers, and email addresses allows hostile actors to map VSSE's organizational structure and potentially target individual agents for surveillance or recruitment. The breach also puts at risk individuals contacted by agents through their work phones, potentially exposing sources or sensitive contacts.

Beyond Belgium, the coordinated nature of attacks across multiple European governments — including the Netherlands, Finland, and the European Commission itself — underscores a systemic vulnerability in how European institutions secure their mobile communications. Cybersecurity experts have noted that the campaign displays the hallmarks of a highly skilled, well-resourced state actor.

## Response and Outlook

VSSE has declined to comment on the breach, and the Federal Prosecutor's Office has not responded to inquiries about whether an investigation has been opened. The CCB has recommended that organizations using Ivanti EPMM patch all vulnerable appliances, change all passwords, renew private keys, and conduct forensic analysis to rule out compromise.

The CCB advisory warned that "threat actors have been observed erasing logging data on Ivanti systems and implementing a backdoor in memory," adding that patching alone is insufficient — organizations must investigate for potential backdoors and compromised data.

As watchTowr CEO Benjamin Harris told The Hacker News: "Attackers are targeting your most trusted, deeply embedded enterprise systems. Anything assumed to be 'internal' or 'safe' should now be viewed with suspicion."

The incident is likely to accelerate calls for greater European autonomy in cybersecurity technology and more rigorous supply chain security requirements for sensitive government agencies.