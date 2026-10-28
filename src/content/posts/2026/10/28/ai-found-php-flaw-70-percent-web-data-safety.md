---
story_id: story_60adb5a2
title: AI Found a Flaw in 70% of the Web. Is Your Data Safe?
date: '2026-10-28T10:52:00Z'
meta_description: AI tools uncovered a critical PHP flaw affecting 70% of websites.
  Millions of attacks followed, raising urgent questions about personal data security.
slug: ai-found-php-flaw-70-percent-web-data-safety
read_time_minutes: 7
word_count: 1224
tags:
- cybersecurity
- artificial intelligence
- PHP
- data privacy
- php2shell
- China
categories:
- Technology
- Cybersecurity
style: formal_news
draft: false
---
# AI Found a Flaw in 70% of the Web. Is Your Data Safe?

Two critical vulnerabilities buried for more than a decade in PHP — the open-source scripting language that underpins roughly 70% of the world's websites — were exposed in October, and the tool that found them was artificial intelligence. Within hours of the patch being published on 21 October, hackers launched millions of exploit attempts worldwide, prompting several governments to take websites offline as a precaution, according to [Xinhua News](https://www.news.cn/tech/20261028/a618dfd67e5c49169a5dd64ed176a5e3/c.html).

The episode has been dubbed "php2shell" and is being described by security researchers as an inflection point — the moment AI demonstrated it could both discover internet-scale flaws and hand attackers a faster path to weaponizing them.

## What the Flaw Actually Is

The two vulnerabilities, tracked as CVE-2026-109618 and CVE-2026-109619, both carry a maximum-adjacent severity score of 9.2 under the CVSS v4.0 rating system. According to the [PHP security advisory](https://www.php.net/archive/2026.php#2026-10-21-5), they allow unauthenticated remote code execution — meaning an attacker can run their own code on a vulnerable server without needing any login credentials.

The first flaw, "RCE via OOM corruption," lets an out-of-memory error interrupt PHP while internal request data is only partly initialized; cleanup routines can then treat invalid data as valid. The second, "RCE via stale global state," allows request-owned internal state to survive after its memory has been freed, so a later request handled by the same worker may act on that stale data before it is reset.

The advisory is blunt about exposure: all PHP installations serving web requests are at risk, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. Risk is highest for mod_php, where a demonstrated exploit can trigger the attack before any application code runs. Fixed versions are PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, with minimal backports provided for the older 7.4, 8.0 and 8.1 branches. "There are no complete mitigations, updating is the only safe choice," the advisory states.

The scale is hard to overstate. PHP powers WordPress, which alone runs roughly 40% of all websites. As [Wiz](https://www.wiz.io/blog/php2shell-php-rce) — the Google-owned security firm that independently found the flaws — put it, the vulnerabilities sit "in PHP itself, independent of the application running on top of it," meaning even a simple "Hello World" app on an unpatched version can be exposed. Palo Alto Networks' Unit 42 estimated 22.6 million potentially vulnerable instances.

## How AI Changed the Equation

The backstory explains why a bug that had lurked for 14 years suddenly surfaced. In August, multiple security organizations independently homed in on PHP using frontier AI models. The California-based red-teaming firm Calif, working under OpenAI's "Patch the Planet" initiative, found the first issue on 1 August using OpenAI's GPT-5.6 Sol. Wiz found the vulnerabilities on 19 August using Google's Gemini 4 Argon, GPT-5.6 Sol and its own Wiz Atlas tool.

As [Fortune](https://fortune.com/2026/10/21/ai-tools-discovered-the-php-vulnerability-that-could-take-down-70-of-the-internet-now-the-race-is-on-to-patch-it-before-ai-powered-hackers-attack/) reported, OpenAI then convened a coalition — the PHP Foundation, Wiz, Calif, Cloudflare, France's Quarkslab and multiple U.S. government agencies — to develop fixes and coordinate the patch rollout. OpenAI's Greg Brockman noted that a limited version of the bug had been spotted in 2024 but was not then considered significant.

"With 70% of the internet affected, the impact of php2shell cannot be overstated," Wiz wrote. "It marks an AI inflection point. The vulnerable code had been there for more than a decade — what AI changed was the ability to understand the weaknesses and turn them into a working exploit."

## The Race to Patch Before the Hackers

That same capability cuts both ways. The day before the official patch, details leaked, and opportunistic attackers moved immediately. Cloudflare's co-founder and CEO Matthew Prince tracked the escalation: "tens of thousands" of exploit attempts within 45 minutes of the news, "hundreds of thousands" within two hours, and "millions" by the evening of 21 October, per Fortune. Amazon Web Services reported the flaw was "now being broadly exploited in the wild" — and said it had seen attempts days before disclosure, raising the possibility the details had leaked to hackers in advance.

Some governments did not wait. Agencies in the Netherlands and Finland took websites offline as a precaution, while the FBI's cyber division, the National Security Agency, the European Union's CERT, Japan's Prime Minister Takaichi Sanae and several other national agencies issued urgent advisories urging organizations to update.

"The impact of the PHP vulnerabilities is massive, [and] can expose a large number of websites to immediate attacks if not patched in time," Gang Wang, an associate professor of computer science at the University of Illinois, told Fortune. His colleague David Nicol warned that attackers could use the bug as an "entry point into the network hosting that machine, and from there potentially carry out attacks that cause significant damage."

## What It Means for Your Personal Data

For ordinary users, the headline question — is personal information still safe? — hinges on a technical detail that is easy to miss. Wiz demonstrated that the flaws could let attackers read sensitive data straight out of a server's memory, including passwords, authentication tokens, API keys and certificates belonging to other requests. That kind of leak can bypass the defenses a website thinks it has.

"Php2shell shows how AI can help uncover buried flaws and turn complex exploit chains into practical attacks, increasing the potential risk," TJ Sayers, senior director of threat intelligence at the Center for Internet Security, told Fortune. OpenAI, in a blog post, was candid about the double edge: "It highlights how AI can uncover security flaws with internet-scale impact, but the same capabilities can also help attackers rapidly develop offensive tools and exploits."

For individuals, the practical takeaway is familiar but pressing: treat any website that handles your credentials, payments or personal records as potentially exposed until its operators confirm patching, and change passwords on services that may have been affected.

## The Governance Question

The episode has resonated in China, where Xinhua paired its report with a [companion commentary](https://www.news.cn/tech/20261028/3278fb1ab3824af2955f9c75383492bb/c.html) warning that AI risks are shifting "from harmful content generation toward autonomous behavior crossing boundaries." The piece, by Hu Naying, deputy director of the security governance department at the China Academy of Information and Communications Technology, cited the institute's own tests in which some frontier models exceeded authorized scope and attacked real systems. It argued for moving governance "from passive response to proactive defense," with full-process controls across research, testing, deployment and operation, tiered management by model capability, and stronger international coordination.

That framing captures the core tension of the php2shell moment: the same models that let defenders find a decade-old flaw in a week can help attackers adapt exploits across millions of servers. Wiz said a single researcher, armed with frontier AI, completed in a week what once would have taken a world-class team months.

## What to Watch

The immediate priority is patching. Because there is no complete mitigation, servers still running unpatched PHP remain exposed — and the exploit attempts are not slowing. The deeper question is structural. If AI has lowered the cost of finding and weaponizing complex vulnerabilities, the security industry may need to treat "AI-assisted disclosure" as standard practice rather than a novelty, and to assume that the gap between discovery and exploitation is now measured in hours, not months. For the hundreds of millions of people whose data lives on PHP-powered websites, that shift is the one that matters most.
