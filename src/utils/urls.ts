/**
 * Prefix an absolute, root-relative path with the configured Astro base path
 * (import.meta.env.BASE_URL) so links work when the site is served from a
 * subpath, e.g. https://valyriantech.github.io/ValyrianNewsNetwork/.
 */
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL;
  const normalizedBase = base.endsWith('/') ? base.slice(0, -1) : base;
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `${normalizedBase}${normalizedPath}`;
}

/**
 * Generate a date-based URL path for a post.
 * Returns path like: /posts/2026/03/27/article-slug
 */
export function getPostUrl(slug: string, date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return withBase(`/posts/${year}/${month}/${day}/${slug}`);
}

/**
 * Generate a date-based slug path for routing.
 * Returns path like: 2026/03/27/article-slug
 */
export function getPostSlugPath(slug: string, date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}/${month}/${day}/${slug}`;
}
