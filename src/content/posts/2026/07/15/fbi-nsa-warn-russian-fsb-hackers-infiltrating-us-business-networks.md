---
story_id: story_ba34d75f
title: FBI and NSA Warn Russian FSB Hackers Targeting US Networks
date: '2026-07-15T16:27:00Z'
meta_description: FBI, NSA, and global partners warn Russian FSB Center 16 hackers
  are exploiting vulnerable routers to infiltrate US critical infrastructure.
slug: fbi-nsa-warn-russian-fsb-hackers-infiltrating-us-business-networks
read_time_minutes: 5
word_count: 873
tags:
- cybersecurity
- Russia
- FSB
- router security
- critical infrastructure
- United States
categories:
- Security
- Cyber
style: analytical_blog
draft: false
---
# FBI and NSA Warn Russian FSB Hackers Targeting US Networks

The FBI, NSA, and a coalition of 19 international agencies have issued an urgent joint warning that Russian state-sponsored hackers are actively exploiting vulnerable internet routers to infiltrate critical infrastructure networks across the United States and allied nations. The advisory, released July 13 under alert code AA26-194A, details a decade-long campaign by Russia's Federal Security Service (FSB) Center 16—also known as Military Unit 71330—that has targeted sectors including energy, financial services, healthcare, communications, government, and the defense industrial base.

## Who Is Behind the Attacks?

FSB Center 16 is the signals-intelligence arm of Russia's Federal Security Service, the successor to the KGB. Unlike Russia's GRU-linked hacking groups such as Sandworm or APT28, Center 16 focuses on foreign intelligence collection through communications interception and computer network operations. The cybersecurity industry tracks this group under multiple names, including Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, and Static Tundra.

The campaign has persisted for over 16 years, evolving from supply-chain attacks on industrial control systems to the current focus on exploiting poorly configured networking devices. In March 2022, the U.S. Department of Justice unsealed indictments against four Russian officers linked to Center 16, with a $10 million bounty offered for information leading to their capture.

## How the Hackers Operate

According to the [joint Cybersecurity Advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a), the hackers primarily scan internet IP ranges for networking devices running Simple Network Management Protocol (SNMP) versions 1 or 2c with default or weak community strings—essentially acting as passwords. Once identified, the attackers use SNMP Set-Requests routed through proxies with spoofed source IP addresses to:

- Copy device configuration files containing admin credentials and network layouts
- Exfiltrate the data via TFTP to attacker-controlled virtual private servers
- Create local accounts, enable Telnet, weaken logging, and build GRE tunnels for persistent access

The advisory also notes that the actors occasionally exploit known vulnerabilities, including CVE-2018-0171 (a critical Cisco Smart Install vulnerability with a CVSS score of 9.8) and CVE-2008-4128 (a Cisco IOS cross-site request forgery flaw affecting end-of-life devices). CISA added CVE-2008-4128 to its Known Exploited Vulnerabilities catalog on the same day the advisory was released.

## Critical Infrastructure in the Crosshairs

The advisory identifies six critical infrastructure sectors as most at risk: communications, defense industrial base, energy, financial services, government services and facilities (especially state and local organizations), and healthcare and public health. The warning builds on an FBI public service announcement from August 2025 that first alerted the public to Russian cyber actors targeting networking devices.

"Russian state-sponsored cyber actors have spent years quietly extracting configuration data from poorly configured routers across critical infrastructure," said Brett Leatherman, Assistant Director of the FBI's Cyber Division, in a [CISA press release](https://www.cisa.gov/news-events/news/cisa-joins-nsa-fbi-dc3-and-international-partners-warning-russian-cyber-threat-activity-targeting). "This advisory gives network defenders the visibility to spot this activity and the mitigations to counter it."

## Unprecedented International Cooperation

The advisory was co-sealed by agencies from 12 countries, including the United States, United Kingdom, Canada, Australia, New Zealand, Czech Republic, Denmark, Estonia, Finland, France, Italy, Poland, and Sweden. This level of coordination underscores the global nature of the threat and the unified Western response to Russian state-sponsored cyber activity.

Chris Butera, Acting Executive Assistant Director for Cybersecurity at CISA, emphasized the urgency: "CISA urges network defenders to implement mitigation and remediation measures to reduce your attack surface and risk of exploitation."

## Expert Analysis: A Preventable Threat

Cybersecurity experts have highlighted that many of the vulnerabilities being exploited are eminently preventable. "These adversaries continue to exploit relatively basic weaknesses because they know those weaknesses still exist," said Louis Eichenbaum, Federal CTO at ColorTokens, as [reported by Forbes](https://www.forbes.com/sites/daveywinder/2026/07/14/fbi-issues-warning-as-russias-fsb-center-16-hackers-target-routers/). "This is especially true with our OT systems that manage our critical infrastructure as they often use legacy components."

Ian Robinson, Chief Product Officer at network security firm Titania, added: "What makes this advisory significant is how avoidable it is. The recommended fixes should all be part of network configuration hygiene but are deprioritized." Robinson noted that routers and network infrastructure are often treated as "set-and-forget" devices, which is precisely what patient, opportunistic adversaries count on.

## Mitigation Steps and Recommendations

The advisory provides a comprehensive set of mitigation actions, including:

- **Immediate:** Disable Cisco Smart Install on all devices, block UDP 69 (TFTP), TCP 4786 (SMI), and UDP 161/162 (SNMP) at the firewall, and patch CVE-2018-0171 where supported
- **Near-term:** Migrate to SNMPv3 with authentication and encryption (authPriv), disable SNMPv1 and v2c, rotate community strings, and apply MIB allow-lists via SNMP views
- **Structural:** Build device lifecycle programs, centralize configuration management, extend telemetry to network devices, and use attack surface management services

## What to Watch For

The December 2025 attack on Poland's power grid, attributed to Static Tundra/Center 16, suggests a potential shift from espionage to active disruption. With the advisory now public, organizations have the visibility they need to defend themselves—but the question remains whether the private sector will act quickly enough.

As the [UK government has documented](https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/), Russia's FSB remains one of the world's most prolific cyber actors. Given the group's decade-plus track record and the DOJ indictments still outstanding, FSB Center 16 is unlikely to cease operations. The effectiveness of this unprecedented international warning will ultimately depend on whether network defenders take the recommended steps before the next breach occurs.