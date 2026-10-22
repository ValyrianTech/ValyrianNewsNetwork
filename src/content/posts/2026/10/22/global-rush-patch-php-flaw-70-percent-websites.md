---
story_id: story_8c25f951
title: Global rush to patch PHP flaw affecting 70% of websites
date: '2026-10-22T18:38:00Z'
meta_description: A critical PHP vulnerability nicknamed PHP2Shell, found with AI's
  help, triggered a global scramble to patch systems powering 70% of websites.
slug: global-rush-patch-php-flaw-70-percent-websites
read_time_minutes: 6
word_count: 1083
tags:
- PHP
- cybersecurity
- software vulnerability
- AI
- open source
- United States
categories:
- Technology
style: formal_news
draft: false
---
# Global rush to patch PHP flaw affecting 70% of websites

Governments and corporations worked through the night on emergency security updates after the AI-assisted discovery of critical vulnerabilities in PHP, the programming language that underpins roughly 70% of websites worldwide. The FBI's cyber division warned that the flaws could let attackers remotely execute malicious code, and recommended that operators take sites offline if they cannot update immediately, according to [AP News](https://apnews.com/article/php-websites-fbi-europe-vulnerability-a0af9576808a0963efca8df14d4b5183).

The two flaws, collectively nicknamed "PHP2Shell," were rated 9.2 out of 10 in severity by the PHP security team. They are notable not only for their reach but for how they were found — by AI models that appeared to identify the bugs before attackers did — and for the two-year gap in which the underlying weaknesses went unfixed.

## What went wrong

PHP is the server-side language behind WordPress, Drupal, Joomla, Magento, Laravel, Symfony and Wikimedia, among countless other systems. Because the flaws exist in the interpreter itself — triggered during early request parsing before any application code runs — no application-layer login check or framework firewall can stop them. That is what elevates the issue toward the class of landmark internet bugs such as Heartbleed and Log4Shell.

One flaw corrupts a system's memory, so it can no longer track its own data reliably, potentially letting an attacker run their own code. The other leaves user data stored on the system instead of cleared, letting a bad actor access it — including downloading or wiping it, James Sullivan, director of cyber and technology at the Royal United Services Institute in London, told AP.

## The response

Many government sites appeared to be functioning normally by Thursday, but outages and limited service continued while the security work was under way. In Britain, Prime Minister Keir Starmer's office said some "limited" government services might temporarily go offline. "Work has already taken place across Government to identify and fix potential exposures to our systems, and our experts are continuing to work closely with both OpenAI and international partners on this issue," a spokeswoman said.

France, the Netherlands and Finland took services down as a precaution. Finland's government website said the disruption had been resolved but that "some content is still missing and is currently being restored." In Japan, Osaka prefecture's site reported its machine-translation service was "unavailable due to a system failure." Japanese Prime Minister Sanae Takaichi advised administrators to check whether they use PHP and to install the patch promptly. "If it is difficult to apply the fix patch promptly, temporarily suspending websites and similar measures can be considered an effective way to reduce risk," she said.

On the defensive side, the PHP Foundation said late Wednesday that it had released fixes for the vulnerabilities, along with instructions on how to update systems, per its own [announcement](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). The coordinated release covered PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, with minimal source backports for older branches, per the official [php.net security archive](https://www.php.net/archive/2026.php).

## The AI inflection point

Artificial intelligence agents helped uncover the vulnerabilities. In a blog post, OpenAI said it had led a coalition of researchers and security providers over the past two months, calling the flaws "one of the most impactful security issues in recent memory" and saying AI appeared to find them before any attackers did.

The scale of exposure is enormous. Security researcher Silas Cutler estimated more than 1.3 million internet-exposed hosts could be vulnerable, while an analysis by Veridion mapped affected PHP versions to roughly 7.07 million companies, most of them small businesses. [Wiz](https://www.wiz.io/blog/php2shell-php-rce), an Alphabet-owned cloud security firm that independently discovered additional attack vectors, compared the severity to Heartbleed.

The discovery marks a landmark moment in AI-assisted vulnerability research: a single researcher armed with AI reportedly completed in about a week what would previously have taken a team months. But it also cuts both ways. "There's good news and bad news to this," Sullivan said, noting that AI can help attackers identify new vulnerabilities just as it helps defenders uncover and fix them. "We shouldn't turn this into a futuristic scenario where we're all doomed."

## A structural failure

The delay in patching was not for lack of warning. According to the PHP Foundation, the vulnerability has been known about since at least 2024, and one root cause traces back further still. "We won't pretend otherwise: the delay was a structural failure, caused by both the security team's decision process and its lack of resources," the foundation said.

Sullivan called it "staggering" that some of the flaws are more than a decade old. The disclosure was also marred by an early leak: the flaw was reported under a coordinated embargo that broke roughly 36 hours before the official patch landed, with CVE identifiers and an inflated CVSS score circulating on social media. That compressed the window defenders had to prepare and let attackers study the fix before most users had an update path.

On October 21, the U.S. National Security Agency issued an advisory warning that cyber actors are "likely to weaponize PHP2Shell vulnerabilities" and that the risks are "serious enough to require immediate patching across United States Government departments and agencies," per the [NSA advisory](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/). The European Union's cybersecurity agency, ENISA, similarly advised organizations to "take immediate action."

## What to watch

As of late Wednesday, the flaws had not been added to the U.S. Cybersecurity and Infrastructure Security Agency's catalog of known exploited vulnerabilities, and CISA said it had not yet observed exploitation. But Cloudflare reported seeing early attack attempts and deployed web-application firewall rules as a stopgap, and one researcher said he observed a PHP2Shell exploitation attempt against a honeypot on October 17 — days before public disclosure. No confirmed compromise of a named victim has been reported.

The larger lesson may lie in the funding gap for open-source infrastructure. The PHP Foundation, which relies on donations and a small staff, is now handling a surge of AI-generated vulnerability reports and has publicly appealed for sponsorship from companies, hosting providers and governments. Meanwhile, the vast long tail of the internet still runs end-of-life PHP versions that will never receive official fixes — a risk that both the foundation and the NSA have flagged.

For now, the race is patching. Administrators who cannot update quickly are being urged to isolate or take systems offline, test the fixes carefully, and enable two-factor authentication where possible. The episode is a reminder that the software quietly holding up the web is only as secure as the will — and the resources — behind its upkeep.
