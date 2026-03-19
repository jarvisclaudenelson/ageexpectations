export function articleSchema({ title, description, url, datePublished = '2025-01-15', dateModified = '2026-03-19' }) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: title,
    description,
    url,
    datePublished,
    dateModified,
    author: {
      '@type': 'Organization',
      name: 'AgeExpectations.com',
      url: 'https://ageexpectations.com',
    },
    publisher: {
      '@type': 'Organization',
      name: 'AgeExpectations.com',
      url: 'https://ageexpectations.com',
    },
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': url,
    },
  };
}

export function faqSchema(faqs) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(faq => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
}

export function medicalWebPageSchema({ name, description, url, lastReviewed = '2026-03-19' }) {
  return {
    '@context': 'https://schema.org',
    '@type': 'MedicalWebPage',
    name,
    description,
    url,
    about: {
      '@type': 'MedicalCondition',
      name: 'Child Development Milestones',
    },
    audience: {
      '@type': 'PeopleAudience',
      audienceType: 'Parents',
    },
    lastReviewed,
    medicalAudience: {
      '@type': 'MedicalAudience',
      audienceType: 'Patient',
    },
    speakable: {
      '@type': 'SpeakableSpecification',
      cssSelector: ['.answer-first'],
    },
  };
}
