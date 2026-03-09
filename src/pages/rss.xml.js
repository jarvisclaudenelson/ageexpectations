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

    const parts = url.split('/').filter(Boolean);
    const age = parts[1];
    const topic = parts[2] || 'index';
    
    // Predicted image path
    const imageUrl = `${context.site}images/pins/${age}-${topic}.png`;
    
    return {
      title: url.split('/').filter(Boolean).join(' ').replace(/-/g, ' '),
      pubDate: new Date(),
      description: `Developmental guide for ${url.split('/').filter(Boolean)[1]}`,
      link: url,
      customData: `<media:content url="${imageUrl}" medium="image" />`,
    };
  });

  return rss({
    title: 'AgeExpectations.com',
    description: 'Practical developmental guides for every stage of parenting.',
    site: context.site,
    items: items,
    xmlns: {
      media: 'http://search.yahoo.com/mrss/',
    },
  });
}
