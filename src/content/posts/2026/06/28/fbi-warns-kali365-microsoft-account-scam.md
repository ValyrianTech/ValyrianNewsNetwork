---
story_id: story_ba596852
title: Kali365 Scam Hijacks Microsoft Accounts, FBI Warns
date: '2026-06-28T17:09:00Z'
meta_description: The FBI warns of Kali365, a phishing platform that hijacks Microsoft
  365 accounts by stealing OAuth tokens, bypassing passwords and MFA.
slug: fbi-warns-kali365-microsoft-account-scam
read_time_minutes: 4
word_count: 735
tags:
- Kali365
- Microsoft 365
- phishing
- cybersecurity
- FBI
- United States
categories:
- Cybersecurity
- Technology
style: formal_news
draft: false
---
# FBI Warns of Kali365 Scam That Hijacks Microsoft Accounts Without a Password

The FBI has issued an urgent warning about a sophisticated new phishing platform called Kali365 that can take over Microsoft 365 accounts without ever stealing a password — and it bypasses multi-factor authentication (MFA) entirely.

First detected in April 2026, Kali365 is a phishing-as-a-service (PhaaS) platform distributed primarily through Telegram. According to the [FBI's Public Service Announcement](https://www.ic3.gov/PSA/2026/PSA260521) (Alert I-052126-PSA), the platform enables cybercriminals to capture OAuth tokens and gain persistent access to Microsoft 365 environments, including Outlook, Teams, and OneDrive.

## How the Attack Works

Unlike traditional phishing attacks that trick users into handing over their passwords, Kali365 exploits a legitimate Microsoft feature: the device code authentication flow. This flow was designed for devices that cannot display a web browser, such as smart TVs and gaming consoles.

The attack unfolds in four stages. First, the victim receives a phishing email impersonating a trusted cloud service or document-sharing platform. The email contains a device code and instructions to visit a legitimate Microsoft verification page. Second, the victim navigates to the real Microsoft page and enters the code, unknowingly authorizing the attacker's device. Third, the attacker captures OAuth access and refresh tokens. Finally, the attacker gains persistent access to the victim's Microsoft 365 services without needing a password or facing additional MFA challenges.

As [Fox News reported](https://www.foxnews.com/tech/fbi-warns-microsoft-users-passwordless-scam), Kurt "CyberGuy" Knutsson described the scam as one that "can fool smart people because it uses a real Microsoft sign-in page to pull off something criminal."

## Why This Is Particularly Dangerous

Kali365 represents a significant evolution in phishing tactics for several reasons. By targeting OAuth tokens rather than passwords, it renders MFA — widely considered the gold standard of account security — completely ineffective. The attack operates entirely within Microsoft's own infrastructure, making detection by password managers and traditional security tools extremely difficult.

"Although early reporting focuses on attacks against organizations, the underlying technique works just as easily against individual Microsoft 365 users who are tricked into entering a short code on a real Microsoft website," wrote Pieter Arntz, Malware Intelligence Researcher at [Malwarebytes](https://www.malwarebytes.com/blog/scams/2026/05/kali365-phishing-kit-bypasses-mfa-and-steals-microsoft-logins). "In other words, this is not just a business or IT department problem."

The PhaaS subscription model further amplifies the threat. Kali365 provides even low-skilled attackers with AI-generated phishing lures, automated campaign templates, real-time tracking dashboards, and OAuth token capture capabilities — dramatically lowering the barrier to entry for large-scale attacks.

## Who Is at Risk

Anyone with a Microsoft 365 account is potentially vulnerable. This includes individuals using Outlook, OneDrive, or Xbox accounts, as well as small businesses and large organizations relying on Microsoft 365 for email, collaboration, and file storage. Once compromised, attackers can read emails, access files, monitor Teams communications, and send convincing phishing messages to colleagues and contacts.

## Protection and Mitigation

The FBI and cybersecurity experts recommend several measures to protect against Kali365 attacks. For individuals, the most critical step is to never enter a Microsoft device code unless you personally initiated the sign-in. Users should also review account activity regularly at account.microsoft.com and revoke any suspicious sessions.

For organizations, the FBI recommends creating conditional access policies to block device code flow for all users, with limited exceptions for legitimate business needs. IT teams should audit current device code usage before implementing restrictions and block authentication transfer policies to prevent users from transferring authentication between devices.

Microsoft has directed users to follow the FBI's recommendations and its own published best practices. The company noted that its Digital Crimes Unit has taken action against similar PhaaS platforms, including Fake ONNX, RaccoonO365, and Tycoon 2FA.

## What to Do If Compromised

If you suspect your account has been compromised, sign out of Microsoft 365 on all devices immediately, change your password, and check your recovery email and phone number. Review Outlook forwarding rules for unauthorized redirects and look for suspicious inbox rules that hide, delete, or redirect emails. Report the incident to the FBI's Internet Crime Complaint Center at ic3.gov.

## The Broader Implications

Kali365 is part of a growing trend of commoditized cybercrime tools that make sophisticated attacks accessible to criminals with minimal technical skill. As token-based attacks become more prevalent, the cybersecurity community faces an urgent challenge: adapting defenses to protect against threats that exploit legitimate authentication infrastructure rather than attacking it directly. The FBI's warning serves as a reminder that even the most trusted security measures can be turned into vectors for compromise.