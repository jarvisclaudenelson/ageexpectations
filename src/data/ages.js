export const ageRanges = [
  { slug: '0-1-month', label: 'Newborn (0–1 Month)', shortLabel: 'Newborn', group: 'infant' },
  { slug: '1-3-months', label: '1–3 Months', shortLabel: '1–3 Mo', group: 'infant' },
  { slug: '3-6-months', label: '3–6 Months', shortLabel: '3–6 Mo', group: 'infant' },
  { slug: '6-9-months', label: '6–9 Months', shortLabel: '6–9 Mo', group: 'infant' },
  { slug: '9-12-months', label: '9–12 Months', shortLabel: '9–12 Mo', group: 'infant' },
  { slug: '12-18-months', label: '12–18 Months', shortLabel: '12–18 Mo', group: 'toddler' },
  { slug: '18-24-months', label: '18–24 Months', shortLabel: '18–24 Mo', group: 'toddler' },
  { slug: '2-3-years', label: '2–3 Years', shortLabel: '2–3 Yr', group: 'toddler' },
  { slug: '3-4-years', label: '3–4 Years', shortLabel: '3–4 Yr', group: 'preschool' },
  { slug: '4-5-years', label: '4–5 Years', shortLabel: '4–5 Yr', group: 'preschool' },
  { slug: '5-6-years', label: '5–6 Years', shortLabel: '5–6 Yr', group: 'school' },
  { slug: '6-8-years', label: '6–8 Years', shortLabel: '6–8 Yr', group: 'school' },
  { slug: '8-10-years', label: '8–10 Years', shortLabel: '8–10 Yr', group: 'school' },
  { slug: '10-12-years', label: '10–12 Years', shortLabel: '10–12 Yr', group: 'preteen' },
  { slug: '12-14-years', label: '12–14 Years', shortLabel: '12–14 Yr', group: 'teen' },
  { slug: '14-18-years', label: '14–18 Years', shortLabel: '14–18 Yr', group: 'teen' },
];

export const topics = [
  { slug: 'milestones', label: 'Milestones' },
  { slug: 'sleep', label: 'Sleep' },
  { slug: 'feeding', label: 'Feeding & Nutrition' },
  { slug: 'behavior', label: 'Behavior & Emotions' },
  { slug: 'language', label: 'Language & Communication' },
  { slug: 'play', label: 'Play & Learning' },
  { slug: 'social-skills', label: 'Social Skills' },
  { slug: 'health', label: 'Health & Safety' },
  { slug: 'red-flags', label: 'Red Flags' },
];

// Extra topic pages per age group (beyond the 9 standard topics)
export const extraTopics = {
  '5-6-years': [
    { slug: 'letter-reversals', label: 'Letter Reversals' },
    { slug: 'learning-disabilities', label: 'Learning Disabilities' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
  '6-8-years': [
    { slug: 'adhd', label: 'ADHD Signs' },
    { slug: 'bedtime', label: 'Bedtime Guide' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
  '8-10-years': [
    { slug: 'anxiety', label: 'Anxiety Signs' },
    { slug: 'deodorant', label: 'Deodorant & Hygiene' },
    { slug: 'puberty', label: 'Puberty & Development' },
    { slug: 'santa', label: 'Santa & Magical Thinking' },
    { slug: 'screen-time', label: 'Screen Time' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
  '10-12-years': [
    { slug: 'anxiety', label: 'Anxiety Signs' },
    { slug: 'bedtime', label: 'Bedtime Guide' },
    { slug: 'deodorant', label: 'Deodorant & Hygiene' },
    { slug: 'stomachaches-before-school', label: 'Stomachaches Before School' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
  '12-14-years': [
    { slug: 'bedtime', label: 'Bedtime Guide' },
    { slug: 'depression-anxiety-warning-signs', label: 'Depression & Anxiety Warning Signs' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
  '14-18-years': [
    { slug: 'always-tired', label: 'Always Tired' },
    { slug: 'bedtime', label: 'Bedtime Guide' },
    { slug: 'staying-home-alone-overnight', label: 'Staying Home Alone Overnight' },
    { slug: 'nutrition', label: 'Nutrition Guide' },
    { slug: 'safety', label: 'Safety' },
    { slug: 'school-learning', label: 'School & Learning' },
  ],
};

export const groupLabels = {
  infant: 'Infant (0–12 Months)',
  toddler: 'Toddler (12 Mo–3 Years)',
  preschool: 'Preschool (3–5 Years)',
  school: 'School Age (5–12 Years)',
  preteen: 'Preteen (10–12 Years)',
  teen: 'Teen (12–18 Years)',
};
