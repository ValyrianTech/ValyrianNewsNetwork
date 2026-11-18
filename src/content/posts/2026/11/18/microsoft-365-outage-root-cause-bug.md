---
story_id: story_c6b5717d
title: Microsoft Outage Tied to Hidden Software Bug
date: '2026-11-18T13:14:00Z'
meta_description: Microsoft says a hidden software bug, Teams network shift and reduced
  server capacity combined to cause a 20-hour global Microsoft 365 outage.
slug: microsoft-365-outage-root-cause-bug
read_time_minutes: 7
word_count: 1234
tags:
- Microsoft
- outage
- cloud
- cybersecurity
- Belgium
categories:
- Technology
- Europe
style: formal_news
draft: false
---
# Microsoft Outage Tied to Hidden Software Bug

A hidden software bug that lay dormant for months, a sudden shift in network traffic and a temporary loss of server capacity combined to bring down Microsoft 365 services worldwide for roughly 20 hours last week, the company disclosed in a preliminary incident report. The outage, which struck on the evening of Thursday 12 November into Friday 13 November, disrupted Outlook, Teams, Copilot, SharePoint and OneDrive for millions of users — and exposed just how deeply businesses and governments depend on a single cloud provider. Microsoft confirmed there were no indications of malicious activity.

## What happened

The first user reports arrived around 18:40 Belgian time on Thursday, as customers found themselves unable to connect to Teams, Copilot, SharePoint and Outlook. Within hours the disruption spread well beyond the Americas to Australia, New Zealand, Japan, India and the wider Asia-Pacific region. According to [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/11/13/grote-storing-microsoft-outlook-en-teams-bedrijven-overheden/), the outage-tracking platform Downdetector logged more than 130,000 reports for Outlook alone, and monitoring sites recorded problems in 74 countries.

The impact reached beyond email. Cloud drives were often unavailable, meaning firms could not always reach their files, and AI assistants that plug into Microsoft accounts were affected too — Anthropic's Claude and OpenAI's ChatGPT both reported losing access to Microsoft 365 services. In the United Kingdom some police services were difficult to reach; in Australia the intelligence service and federal police reported hindrance.

## The root cause: three factors in a chain reaction

In the preliminary report, Microsoft vice-president Charles Lamanna described a failure produced by three interacting factors. The first was a software change pushed in July 2026 to the servers handling all Microsoft 365 network traffic. "That change contained a hidden fault," Lamanna wrote. "Under certain conditions, different processes on a server could block each other." The phenomenon, known as lock contention, causes processes competing for the same resource to freeze a server — but the bug only surfaced on higher-powered machines, while standard testing ran on less powerful ones. As [VRT NWS reported](https://www.vrt.be/vrtnws/nl/2026/11/16/microsoft-outlook-wereldwijde-storing-oorzaak-rapport/), the flaw went undetected for months.

The second factor was Teams. About 15 hours before the outage, Microsoft switched Teams back from its alternative network system to the primary platform — the same one that carries Exchange Online email traffic. This suddenly concentrated extra traffic on servers already vulnerable to the latent bug. The third factor was capacity: following an unrelated incident the day before, almost 14 percent of server capacity was temporarily out of service.

Together the three produced a cascade. Servers locked up; users were automatically rerouted to other servers, which were flooded and hit the same fault. "Within less than two hours, more than 80 percent of our servers were unreachable," Lamanna wrote. Protection mechanisms that are supposed to isolate failing components did not work as intended.

## Why recovery was so slow

Automatic recovery failed because rebooting servers were immediately overwhelmed by the traffic that had accumulated in the meantime, and failed again. Rolling back was difficult because the faulty change dated from July, so Microsoft ultimately had to develop a new software update to revert the code to its previous, stable state. At one point the company conceded that "the efforts are not progressing as expected." To prevent mail loss, Microsoft extended its email time-out period to 48 hours while it worked through the backlog.

## A Belgian reality check

For Belgium, the outage was a sharp reminder of its exposure. "The scale is gigantic," Danielle Jacobs, CEO of Beltug — the Belgian association of CIOs and business leaders — told [Trends](https://trends.knack.be/ai-en-tech/technieuws/urenlange-storing-bij-microsoft-365/). A recent Beltug market study calculated that about 90 percent of companies in Belgium work with Microsoft. "The dependence in Belgium is very large," she said. "This is really a wake-up call."

Jacobs warned that the disruption reached beyond email: in many cases cloud drives were unavailable, so companies could not always access their files. "Businesses must really do the exercise around their own business continuity," she advised, adding that while some firms are moving core applications back onto their own servers, "they often forget email, because it supposedly isn't crucial — yet it stops employees from doing their job." She also flagged the rise of so-called shadow IT during such incidents, as staff switch to WhatsApp, Signal or Google Drive to keep communicating — creating compliance and data-leak risks outside the secured IT environment.

The fragility was felt across Belgian sectors and beyond. At Apotheek Lamoot in Vlamertinge, near Ypres, staff had to process orders for hospitals, care homes and disability services by telephone because the usual email channel was down. Pharmacist Lies Alvoet told [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/11/13/apotheek-ieper-problemen-microsoft/) that the risk of error rises when orders are taken verbally — with sensitive medication names, dosages, patient details and room numbers, a similar patient name can easily lead to a mix-up. "The risk of mistakes becomes greater," she said.

At the Wintercircus in Ghent, a hub for the city's tech start-ups, CEO Dorien Van Steenberge said the direct impact was limited because about 75 percent of its start-ups use Google for office software — but their clients often use Microsoft. She called the incident a warning about European dependence on big software vendors, and pointed to the failure of internal back-up systems as a particular concern. "Back-up systems spread across different software providers are not yet common," she told [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/11/13/wintercircus-gent-microsoft-problemen/).

The real-world consequences could be serious. At Phantasialand, a theme park near Cologne, an automatic pool-dosing system at a hotel malfunctioned; because its alerts were sent via Outlook, they never arrived, and the faulty system pumped too much chlorine into a pool. Fifteen guests developed health complaints, and four were taken to hospital, [VRT NWS](https://www.vrt.be/vrtnws/nl/2026/11/14/outlookstoring-phantasialand-zwembad-chloor/) reported.

## Analysis: a concentration problem, not a cyberattack

Cybersecurity expert Eddy Willems, author of *Het cybergevaar*, said the episode points to a structural fragility rather than a single company's error. "Everything is connected," he told VRT NWS. "If one element in the chain fails, you see it worldwide." He noted that he warned on CNN some 15 years ago about the risks of moving everything to the cloud — and that the danger is now concentrated dependence on a single provider. "If you throw everything into the cloud, the problems can become very big."

The timing fits a wider pattern. Earlier in 2026 there were multi-hour outages at network-infrastructure firm Cloudflare and cloud provider AWS, disrupting websites and services across the internet; at the end of August, a major Outlook outage also hit thousands of users before being resolved relatively quickly. Each incident underlines the same lesson: as services consolidate onto a handful of hyperscale platforms, a single defect can travel around the globe in minutes.

Jacobs of Beltug also pointed to dangerous market concentration building around firms such as SpaceX and Nvidia, arguing the outage should accelerate European work on resilience and technological sovereignty — themes that Belgian and EU policymakers have been developing for months.

## What's next

Microsoft has promised a full, final incident report describing the root cause and the layered-defence measures it will adopt. The open question is whether a single provider's control of critical infrastructure will change course: whether companies genuinely diversify across multiple cloud providers, whether more core systems come back on premises, and whether regulators scrutinise concentration in cloud and AI infrastructure more closely. For Belgium, where nine in ten firms rely on Microsoft, the warning could hardly be clearer.
