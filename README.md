# Valyrian News Network (VNN)

**AI-synthesized, context-rich news analysis with full transparency.**

A project of [Valyrian Tech](https://valyrian.tech), powered by the SERENDIPITY AGI framework.

## Overview

VNN is a static news website that publishes AI-generated articles with complete transparency about the automated methodology. Articles are synthesized from verified sources and presented with proper attribution and sourcing.

## Tech Stack

- **Framework:** [Astro](https://astro.build) with Content Collections
- **Styling:** [Tailwind CSS](https://tailwindcss.com) v4
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

## Project Structure

```
├── .github/workflows/     # GitHub Actions for deployment
├── automation/            # Pipeline scripts
│   └── publish_article.py # Script to publish articles from SERENDIPITY
├── public/                # Static assets
├── src/
│   ├── components/        # Astro components (Header, Footer, ArticleCard)
│   ├── content/posts/     # Article markdown files (organized by YYYY/MM/DD/)
│   ├── layouts/           # Page layouts (BaseLayout, ArticleLayout)
│   ├── pages/             # Routes (index, about, article pages)
│   └── styles/            # Global CSS with VNN brand
└── stories/               # Original pipeline output (gitignored)
```

## Commands

This project requires **Node.js >=22.12.0**. Use nvm to switch versions:

```bash
nvm use 22
npm run dev
```

| Command           | Action                                      |
| :---------------- | :------------------------------------------ |
| `npm install`     | Install dependencies                        |
| `npm run dev`     | Start dev server at `localhost:4321`        |
| `npm run build`   | Build production site to `./dist/`          |
| `npm run preview` | Preview build locally before deploying      |

## Publishing Articles

Articles from the SERENDIPITY pipeline can be published using:

```bash
python automation/publish_article.py /path/to/article.md --commit
```

The script validates front matter, copies the article to `src/content/posts/`, and optionally commits the change.

### Article Front Matter Schema

```yaml
---
title: "Article Title"
date: 2026-03-27T19:14:13.000Z
draft: false
categories: ["Policy", "China"]
tags: ["tag1", "tag2"]
meta_description: "Brief description for SEO"
slug: "article-slug"
read_time_minutes: 7
style: "formal_news"
word_count: 1625
featured_image: "/images/article-image.jpg"  # optional
featured_image_caption: "Image caption"       # optional
---
```

## Deployment

Push to `main` branch triggers automatic deployment via GitHub Actions to GitHub Pages.

## License

© Valyrian Tech. All rights reserved.
