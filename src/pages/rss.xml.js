import rss from '@astrojs/rss';
import { articles } from '../data/content.js';

export function GET(context) {
  return rss({
    title: 'AgeExpectations.com',
    description: 'Evidence-based parenting guidance — developmental milestones, sleep, feeding, behavior, and red flags for every age from newborn through 18 years.',
    site: context.site,
    items: articles.map(article => ({
      title: article.title,
      description: article.description,
      link: article.path,
      pubDate: new Date(article.pubDate),
    })),
    customData: '<language>en-us</language>',
  });
}
