import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    categories: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    meta_description: z.string(),
    slug: z.string(),
    featured_image: z.string().optional(),
    featured_image_caption: z.string().optional(),
    read_time_minutes: z.number().int().positive(),
    style: z.enum(['formal_news', 'analytical_blog', 'concise_summary']).default('formal_news'),
    word_count: z.number().int().positive(),
  }),
});

export const collections = { posts };
