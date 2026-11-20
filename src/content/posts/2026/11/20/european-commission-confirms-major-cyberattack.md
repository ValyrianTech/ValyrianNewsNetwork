---
story_id: story_5c9e6f50
title: European Commission Confirms Major Cyberattack
date: '2026-11-20T14:48:00Z'
meta_description: The European Commission confirms a cyberattack disrupted HR systems
  for over ten days, with the AI tool ARTEX suspected and staff data still in doubt.
slug: european-commission-confirms-major-cyberattack
read_time_minutes: 5
word_count: 926
tags:
- European Commission
- cybersecurity
- ARTEX
- EU institutions
- data breach
- International
categories:
- Technology
- Politics
style: formal_news
draft: false
---
# European Commission Confirms Major Cyberattack

The European Commission has confirmed that it was the target of a significant cyberattack that disrupted internal systems for more than ten days, affecting payroll, timesheet and medical-reimbursement platforms and raising unresolved questions about the security of staff personal data. The incident, first reported by Politico on the morning of 19 November, was confirmed the same day by Commission spokesperson Thomas Regnier during a press briefing in Brussels.

According to [Politico's Brussels Playbook](https://www.politico.eu/newsletter/brussels-playbook/cyberattack-hits-the-commission/), the attack has "potentially compromised swaths of personal data," left staff unable to input salary and leave information, and prompted the Commission's most senior officials to convene over the crisis.

## A Three-Week Gap Between Detection and Disclosure

The Commission says the malicious activity was detected on 22 October 2026 and confirmed on 26 October following an initial investigation — meaning roughly three weeks elapsed before the incident became public.

"We have disabled a number of applications and most of them have already been reactivated," Regnier said, describing the response to what he called a "cyber campaign." He added: "Individual systems were targeted and, in line with our standard practice, we have informed those concerned."

## Which Systems Were Affected

The disruption reached deep into the Commission's internal administration. According to [Le Soir](https://www.lesoir.be/783727/article/2026-11-19/la-commission-europeenne-reconnait-avoir-ete-la-cible-dune-cyberattaque-aux), which reported the story with AFP, the affected programs included the encoding of salaries and leave.

Reporting by [SecurityAffairs](https://securityaffairs.com/203483/hacking/european-commission-cyberattack-artex-ai-tool-suspected-in-prolonged-disruption.html) filled in the operational detail: Sysper, the HR platform for payslips, timesheets and leave, crashed briefly again on 18 November after access had been restored earlier in the week. MyPMO, the medical-reimbursement system, came back online around the same time. JSIS, the staff health-insurance portal, was still down on 19 November, and translation services went offline on 17 November.

Despite the chaos, pay landed on time for staff Politico spoke to, even as some could not submit timesheets or request leave.

## The Suspected Weapon: ARTEX

The EU institutions' cybersecurity service, CERT-EU, detected the activity and identified ARTEX — an AI-powered penetration-testing framework — as a possible tool used in the attack.

In a [technical note published on 5 November](https://www.cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex), CERT-EU described ARTEX as an "open-source, LLM-driven autonomous penetration testing platform" that takes a security objective in natural language, decomposes it into sub-tasks, and has AI agent workers execute reconnaissance and exploitation using real hacking tools.

"Following reports of misuse, the original author made the repository unavailable in October 2026," CERT-EU wrote, adding that "the publicly available versions are now independent forks rather than an official upstream release." Because the tool does not include its own AI model and connects to external providers, removing the original project does not prevent others from using it.

CERT-EU warned that ARTEX's public availability "will likely accelerate adoption by threat actors, resulting in more frequent, faster, and more scalable automated attacks with a higher success rate."

Officials stressed that the ARTEX reference points to a *suspected tool*, not a confirmed attack method or attribution. There is no public information on how attackers entered the Commission's systems, and no actor, group or state has been named.

## The Data Question Remains Open

The most pressing unanswered question is whether staff personal data — names, salary details, home addresses or health information — was stolen.

The Commission states it has "no evidence" of a data breach, but has not ruled one out. According to the analysis in SecurityAffairs, taking systems offline or restoring them "does not prove that no data was stolen" — bringing a service back online only shows it is working again, not that attackers failed to copy information before shutdown.

Under EU Regulation 2018/1725, a confirmed personal-data breach must normally be reported to the European Data Protection Supervisor (EDPS) within 72 hours, with affected individuals informed without delay if there is a high risk. Those deadlines only begin once a breach has been confirmed — which helps explain the Commission's carefully hedged language while its investigation continues.

The Commission rejected accusations that it had been slow to communicate. "When you are hit by a cyberattack, you have to take measures that you don't want to be made public, precisely so as not to hinder their effectiveness," Regnier said.

## Context: A Wave of Cyber Aggression

The incident is the latest in a widening surge of cyber aggression against European institutions and infrastructure. Earlier in November, coordinated attacks struck food-distribution refrigeration systems across roughly ten EU member states, including Belgium. In France, Crédit Mutuel Arkéa was hit by a diversion of more than €100 million.

It is also not the Commission's first security incident this year. In January, attackers left traces in the system used to manage staff mobile devices, exposing some names and phone numbers. A more serious incident in March saw attackers compromise a software update for the Trivy security tool to enter an AWS cloud environment, stealing about 91.7 GB of compressed data — a breach that may have affected at least 29 other EU institutions and bodies. No link between these cases and the November incident has been established.

## What to Watch

Attention now turns to several open threads: whether the EDPS opens a formal investigation, whether any confirmed data breach affecting staff is disclosed, and whether the Commission or CERT-EU offers updated guidance on ARTEX. The incident also sharpens a broader policy question — how EU institutions govern the dual-use risk of AI-powered security tools that can be repurposed by attackers once they leak into the wild.

For now, the Commission's systems are largely back online. But the answers, as one EU official put it, are taking a little longer.
