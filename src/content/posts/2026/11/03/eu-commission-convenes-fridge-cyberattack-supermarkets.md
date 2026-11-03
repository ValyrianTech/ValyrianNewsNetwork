---
story_id: story_2cad9a67
title: EU Commission Convenes Over Supermarket Fridge Cyberattack
date: '2026-11-03T15:04:00Z'
meta_description: The European Commission met over a cyberattack on supermarket refrigeration
  systems, as Delhaize and other Belgian chains returned to normal operations.
slug: eu-commission-convenes-fridge-cyberattack-supermarkets
read_time_minutes: 4
word_count: 792
tags:
- cybersecurity
- retail
- Delhaize
- European Commission
- critical infrastructure
- Belgium
categories:
- Technology
- Europe
style: formal_news
draft: false
---
# EU Commission Convenes Over Supermarket Fridge Cyberattack

The European Commission has held high-level coordination meetings over a Europe-wide cyberattack that sabotaged supermarket refrigeration systems, even as affected Belgian chains—including Delhaize, Carrefour and Spar—reported a return to normal operations on 3 November 2026. The incident, which follows a larger attack on French supermarkets in October, has pushed the security of operational technology in the food supply chain to the top of the EU's agenda.

## What Happened

The attack struck on the night of 1–2 November. Hackers remotely hijacked internet-connected refrigeration controllers and forced them into continuous defrost mode, causing fridges and freezers to heat up rather than cool. In Belgium, the effects were visible within hours: Delhaize reported an "IT incident" at roughly 40 stores, Carrefour confirmed problems at 15 of its 700 outlets, Spar reported issues at 5 independent shops, and Intermarché was affected at 10 to 15 stores in Wallonia and Brussels. An Ikea store in Bergen was also hit, according to [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/11/02/cyberaanval-delhaize/).

The disruption was not confined to Belgium. Supermarkets in Luxembourg, the Netherlands, Sweden, Estonia, Ireland, Italy, Romania, Finland, Portugal and Germany reported similar problems. The financial toll at individual Belgian outlets was stark: a Proxy Delhaize in Hoepertingen estimated at least €60,000 in discarded food, while a store in Eeklo reported tens of thousands of euros in losses and freezer temperatures pushed to 50°C.

By the morning of 3 November, Delhaize, Carrefour and Spar had all told VRT NWS their stores were operating normally again.

## The Vulnerability Behind the Attack

The mechanism was not novel. As VRT NWS [explained](https://www.vrt.be/vrtnws/nl/2026/11/02/koelsystemen-verstoord-bij-onder-meer-delhaize-en-carrefour-hoe/), the affected controllers—primarily Danfoss models such as the AK-SM800 and AK-SC355—are often managed remotely by third-party installers via internet-facing web servers. The devices had a publicly reachable login screen with a hidden function that allowed attackers to bypass passwords entirely. The AK-SC355 reached end-of-life in 2016 and the AK-SM800 in May 2021, both no longer supported with updates.

The flaw was previously disclosed by cybersecurity firm Claroty in 2025 and patched by Danfoss in August 2025. It was also the mechanism behind the October attack on up to 700 French supermarkets, which caused more than €10 million in damage. Keanu Nys, an ethical hacker at Spotit, said the Belgian wave resulted from an inadequate response to the French incident, noting there is "no reason whatsoever" for such refrigeration systems to be publicly accessible on the internet.

## Brussels Steps In

As the scale of the incident became clear, the European Commission convened twice: once with the EU Inter-institutional Cybersecurity Task Force, including Europol, and once coordinated via EU-CyCLONe, the network of national authorities responsible for managing large-scale cyber incidents.

"The problems show that cyberattacks can disrupt services, affect businesses and have a direct impact on the daily life of citizens," a Commission spokesperson said. "We are using CYCLONe for coordination and information-sharing, as several member states are affected," the spokesperson added, according to [VRT NWS](https://www.vrt.be/vrtnws/nl/liveblog/europese-commissie-vergaderde-over-cyberaanval-supermarkten-van~1793610043244/).

In Belgium, the federal prosecutor's office has opened a criminal investigation. Interior Minister Bernard Quintin (MR) reassured the public that there were no general supply problems, as distribution centres were not affected, and said no avenue was being excluded. The Federal Agency for the Safety of the Food Chain (FAVV) reminded retailers that all shops fall under a self-monitoring system and must remove any products where food safety is in doubt.

## Rising Concern Over OT Security

The attack has amplified warnings from Belgium's Centre for Cybersecurity (CCB), which said it is "concerned about the increasing number of incidents, partly through the targeted use of AI." The agency added that "all IT systems are potentially vulnerable, and with AI this can now be successfully exploited, especially by advanced actors. This is an evolution of the last six months. The situation is changing very rapidly."

Experts remain divided on motive. Patrick Hauspie, a cybersecurity expert at VLAIO, suggested the attack was either financially motivated or intended to destabilise through a hybrid attack. "If you get hold of the password of the administrator who does the maintenance, then you can do a lot of bad things with it," he said. No group has claimed responsibility, and the October French incident also remains unattributed.

## What's Next

The episode has exposed a structural gap: cybersecurity is primarily a member-state competence, yet cross-border attacks on commercial infrastructure demand EU-level coordination. Belgian authorities strengthened their legal framework in December 2025 by transposing the EU CER Directive, which now covers the food sector from production to distribution. Minister Quintin was scheduled to meet sector federation Comeos to discuss protective measures.

For now, the immediate crisis has passed. But the deeper question—how many operators still run internet-exposed, end-of-life controllers—remains unanswered, and will likely shape the next round of regulatory scrutiny in Brussels.
