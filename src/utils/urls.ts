/**
 * Generate a date-based URL path for a post.
 * Returns path like: /posts/2026/03/27/article-slug
 */
export function getPostUrl(slug: string, date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `/posts/${year}/${month}/${day}/${slug}`;
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
