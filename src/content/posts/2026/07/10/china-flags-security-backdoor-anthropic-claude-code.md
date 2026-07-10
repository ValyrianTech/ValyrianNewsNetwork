---
story_id: story_393092ce
title: China Flags Security Backdoor in Anthropic's Claude Code
date: '2026-07-10T06:25:00Z'
meta_description: China's MIIT warns of a security backdoor in Anthropic's Claude
  Code, accusing the AI tool of secretly transmitting user data. Alibaba bans internal
  use.
slug: china-flags-security-backdoor-anthropic-claude-code
read_time_minutes: 4
word_count: 664
tags:
- Anthropic
- Claude Code
- Cybersecurity
- China
- AI Security
categories:
- Cybersecurity
- Technology
style: formal_news
draft: false
---
# China Flags Security Backdoor in Anthropic's Claude Code

Chinese authorities have flagged a severe security backdoor in Anthropic's AI coding tool Claude Code, accusing the software of secretly transmitting user data to remote servers without consent. The warning, issued by China's Ministry of Industry and Information Technology (MIIT) through its National Vulnerability Database (CNVDB), has triggered an immediate response from Chinese tech giant Alibaba, which has banned internal use of the tool effective July 10, 2026.

## The Discovery

According to [Caixin Global](https://www.caixinglobal.com/2026-07-09/business-brief-july-9-china-flags-security-backdoor-in-ai-tool-claude-code-102462466.html), the CNVDB stated that it had "detected that the AI coding tool Claude Code contains security backdoor risks, posing a severe threat." The database advised users to "conduct a comprehensive check immediately" and "promptly uninstall or upgrade to the latest secure version from which the relevant backdoor code has been removed."

The affected versions — Claude Code 2.1.91 through 2.1.196 — were found to contain hidden steganographic code capable of transmitting sensitive information including user location, identity markers, and system environment data back to Anthropic servers.

## How the Tracking Worked

Independent security researcher "Thereallo" published a detailed analysis on June 30, 2026, revealing how the hidden tracking mechanism operated. As documented on [Thereallo's blog](https://thereallo.dev/blog/claude-code-prompt-steganography), Claude Code employed "prompt steganography" — hiding tracking markers in plain sight by making visually imperceptible changes to system prompts.

The tracking activated when the `ANTHROPIC_BASE_URL` environment variable was set to a non-Anthropic endpoint. It then performed three checks: detecting if the system timezone was set to `Asia/Shanghai` or `Asia/Urumqi`, comparing the API base URL hostname against a list of known Chinese corporate and proxy domains, and scanning for keywords associated with Chinese AI labs such as `deepseek`, `moonshot`, `zhipu`, and `baichuan`.

Depending on the classification, Claude Code would subtly alter the date format from `YYYY-MM-DD` to `YYYY/MM/DD` for Chinese timezones, or change the apostrophe in "Today's" to different Unicode characters — changes virtually invisible in most monospace fonts but readable by Anthropic's backend systems.

## Alibaba's Response

Chinese e-commerce giant Alibaba moved swiftly to distance itself from the tool. As reported by the [South China Morning Post](https://www.scmp.com/tech/big-tech/article/3359375/alibaba-bans-staff-using-claude-code-over-anthropic-spyware-concerns), an internal memo stated: "As Claude Code was recently discovered to carry back-door risks, after comprehensive evaluation, Claude Code has now been added to a list of high-risk software with security vulnerabilities." The ban took effect on July 10, 2026.

## Anthropic's Defense

Anthropic engineer Thariq Shihipar acknowledged the tracking code on X, describing it as "an experiment we launched in March that was meant to prevent account abuse from unauthorized resellers and protect against distillation." Shihipar stated that the team had "landed stronger mitigations since then" and that the code "should be fully rolled back in tomorrow's release."

A company spokesperson told [Ars Technica](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/) that Chinese labs' distillation attacks "pose a serious threat to national security and undermine AI safety standards across the industry." Anthropic has previously accused Alibaba of conducting the "largest distillation attack ever on Claude" in June 2026.

## Broader Implications

The incident marks a significant escalation in the US-China AI rivalry. Chinese firms have "consistently matched" US firms' model capabilities "within months," according to reporting from The Washington Post cited by Ars Technica. The hidden tracking code — implemented through steganography rather than transparent disclosure — has damaged trust in developer tools at a time when AI coding agents already operate on what security researchers describe as "the wrong side of a scary boundary," with extensive access to filesystems, shells, and code repositories.

As [TechRadar Pro](https://www.techradar.com/pro/china-warns-users-of-alleged-security-backdoor-vulnerabilities-in-anthropics-claude-code-tells-users-to-uninstall-for-sfaety-reasons) noted, the CNVDB warning creates regulatory pressure for Chinese companies to audit and potentially abandon foreign AI tools, accelerating the decoupling of US and Chinese AI ecosystems.

## What's Next

The CNVDB has urged organizations to strengthen network traffic monitoring to prevent unauthorized data leakage. It remains unclear whether other Chinese tech firms such as Baidu, Tencent, and ByteDance will follow Alibaba's lead in banning Claude Code. Meanwhile, Anthropic faces a significant trust crisis as the AI industry grapples with demands for greater transparency in how developer tools monitor and report user activity.