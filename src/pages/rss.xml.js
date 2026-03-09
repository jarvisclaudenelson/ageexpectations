import rss from '@astrojs/rss';

export async function GET(context) {
  const pages = import.meta.glob('./ages/**/*.astro', { eager: true });
  
  const items = Object.entries(pages).map(([path, page]) => {
    // Extract age and topic from path
    // Format: ./ages/0-1-month/index.astro -> /ages/0-1-month/
    // Format: ./ages/12-18-months/sleep/index.astro -> /ages/12-18-months/sleep/
    const url = path
      .replace('./', '/ages/')
      .replace('index.astro', '')
      .replace('.astro', '/');

    // Get title and description from the page's exported components if possible,
    // or fall back to sensible defaults. Since they are .astro files,
    // we can't easily read the frontmatter unless they are using markdown.
    // For now, we'll use a placeholder and suggest moving to Content Collections.
    
    return {
      title: url.split('/').filter(Boolean).join(' ').replace(/-/g, ' '),
      pubDate: new Date(),
      description: `Developmental guide for ${url.split('/').filter(Boolean)[1]}`,
      link: url,
    };
  });

  return rss({
    title: 'AgeExpectations.com',
    description: 'Practical developmental guides for every stage of parenting.',
    site: context.site,
    items: items,
  });
}
