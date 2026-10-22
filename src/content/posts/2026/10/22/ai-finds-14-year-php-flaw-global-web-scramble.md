---
story_id: story_0a8fafe0
title: AI Finds 14-Year-Old PHP Flaw, Sparking Global Web Scramble
date: '2026-10-22T17:30:00Z'
meta_description: Frontier AI uncovered critical PHP vulnerabilities dormant for 14
  years, forcing a global scramble as websites worldwide went offline to patch.
slug: ai-finds-14-year-php-flaw-global-web-scramble
read_time_minutes: 6
word_count: 1111
tags:
- cybersecurity
- PHP
- artificial intelligence
- open source
- vulnerability
- International
categories:
- Technology
- Cybersecurity
style: formal_news
draft: false
---
# AI Finds 14-Year-Old PHP Flaw, Sparking Global Web Scramble

Two critical vulnerabilities in PHP — the open-source scripting language that underpins roughly 70% of the world's websites — were disclosed this week after lying dormant in the code for about 14 years, having been detected with the help of frontier artificial intelligence models. The flaws, collectively dubbed "PHP2Shell," allow unauthenticated attackers to take control of affected servers, and prompted governments, hospitals, banks and media companies across Europe, Asia and North America to take services offline as a precaution before an emergency patch was prepared.

According to [PHP's official security advisory](https://www.php.net/archive/2026.php#2026-10-21-5), published on October 21, the two vulnerabilities — tracked as CVE-2026-109618 and CVE-2026-109619 — permit "unauthenticated remote code execution" and carry a CVSS severity rating of 9.2 out of 10. Fixed releases were issued the same day: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. The advisory urged all users to update immediately, warning that for some configurations "there are no complete mitigations."

## What is PHP, and why does one flaw matter so much?

The scale of the disruption stems from PHP's ubiquity. The language powers major content-management systems including WordPress, Drupal and Joomla, and is bundled into hosting control panels and countless web services. As Belgian computer scientist Jeroen Baert explained to [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/10/21/php-lek-data-wat-is-het/), the danger lies not in any single website's code but in the engine beneath it.

"Through this leak, someone with bad intentions can gain access to the underlying system of a website," Baert said. "That is one of the most severe security problems that exist." Because the flaw sits in PHP itself, even a simple application running on an affected version can be vulnerable — a point [Wiz Research](https://www.wiz.io/blog/php2shell-php-rce) emphasised, noting that exploitation "does not depend on a flaw in the application's code."

The vulnerabilities reach back to PHP 5.4, released in 2012. Wiz researchers said the underlying bugs had been present for more than a decade but that demonstrating their exploitability required "an exceptionally complex chain of steps, at the edge of what human researchers could practically achieve." Frontier AI models, they said, substantially lowered that barrier.

## How AI found what humans missed

Two independent teams made the discovery in August 2026. One was researcher Ryan Austin at the California-based security firm Calif, working under OpenAI's "Patch the Planet" initiative; the other was Wiz, the cloud-security company owned by Google parent Alphabet.

[OpenAI](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) confirmed that Calif identified a critical flaw using its GPT-5.6 Sol model, while Wiz independently discovered and reported both vulnerabilities. Wiz said its researchers used its own Atlas tool alongside Gemini 4 Argon and GPT-5.6 Sol, with Gemini 4 Argon making a "particularly significant contribution" to finding the flaw and validating the patch.

The disclosure marks one of the first major cases of AI discovering a high-severity vulnerability in software used across the internet. "To our knowledge, frontier AI found these vulnerabilities before attackers did, opening a Defender's Window for maintainers and security providers to prepare fixes and protections ahead of disclosure," OpenAI wrote.

## A global scramble to go offline

The public announcement on October 20 — a day before the patch — set off a worldwide wave of precautionary shutdowns. In Belgium, all Flemish government websites running on PHP were taken offline on the instruction of Minister-President Matthias Diependaele, while federal finance and foreign-affairs portals, hospital sites, local police zones and even the website of the country's cybersecurity centre went dark. In the Netherlands, the DigiD digital identity system and government portals were affected; France, Finland and Denmark saw public services pulled; and in the United States, the Wikimedia Foundation shut down supporting services and the Internet Archive briefly went offline.

"The period in which the vulnerability is publicly known and not yet contained can be extremely dangerous," Vincent Ginis, a professor of AI and mathematics at the Vrije Universiteit Brussel, told VRT NWS. Baert described the moment as "a kind of tipping point," because once the fix is published, malicious actors can study it to learn exactly where the flaw lies.

By the afternoon of October 21, services began returning as patches were applied. Cloudflare said it deployed firewall protections to block exploitation attempts and reported "millions" of attempts on its network. Government agencies including the US National Security Agency, the FBI, the UK's National Cyber Security Centre and the EU's ENISA issued urgent advisories, though the US Cybersecurity and Infrastructure Security Agency said it had not observed confirmed exploitation as of October 21 — a point of some disagreement with private-sector reports.

## The double-edged sword of AI

The episode has become a landmark case study in the dual-use nature of artificial intelligence in cybersecurity. The same models that helped defenders find and fix the bug faster than humans could might also help attackers locate and weaponise others.

"AI is in this story both the helper and the culprit," said Steven Latré, an AI expert at the Belgian research institute Imec, speaking to VRT NWS. "That leak was there for more than 14 years and was never discovered by humans. AI came to the rescue to find it. But there's also a flip side."

Experts stressed that the window between a patch's release and its exploitation is collapsing. "Where we used to have weeks or even a month to install an update, it's now reduced to a few days or even a few hours before hackers abuse systems," Miguel De Bruycker of Belgium's Centre for Cybersecurity told VRT NWS. Latré put it more bluntly: "What they could do in days before, they can now do in a few hours."

The incident also laid bare a structural fragility in the open-source ecosystem. The PHP Foundation, which maintains the language, operates with a small staff reliant on contributions, while AI research commands billions in investment — an asymmetry that leaves critical shared infrastructure thinly defended.

## What to watch next

The most immediate risk lies with organisations that cannot patch quickly. Wiz warned that millions of companies run an affected PHP version, most of them small businesses with limited security resources and no easy way to be reached. "You can't afford today not to know what's running in your environment and where your biggest technological dependencies are," said Maxime Thiebaut, a digital forensics expert at the security firm NVISO.

For now, no large-scale breach has been confirmed, and the precautionary shutdowns have largely reversed. But the deeper lesson is unlikely to fade: as AI grows more capable, vulnerabilities that survived more than a decade of human scrutiny may become routine discoveries — and routine weapons. "100% secure software doesn't exist," Ginis said. "As AI gets smarter, you'll have more and more software that becomes vulnerable."
