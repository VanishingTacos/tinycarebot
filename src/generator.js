import {
  categories,
  openers,
  timings,
  closers,
  sharedEmoji,
  templates,
} from './grammar.js';

export const MAX_GRAPHEMES = 300;

const segmenter = new Intl.Segmenter('en', { granularity: 'grapheme' });

export function graphemeLength(text) {
  return [...segmenter.segment(text)].length;
}

function pick(list, rng) {
  return list[Math.floor(rng() * list.length)];
}

function tidy(text) {
  return text
    .replace(/\s+/g, ' ')
    .replace(/\s+([.,?!:])/g, '$1')
    .trim()
    // Capitalize the first letter and the start of each new sentence.
    .replace(/(^|[.?!]\s+)([a-z])/g, (_, before, letter) => before + letter.toUpperCase());
}

function buildTip(rng) {
  const category = pick(Object.values(categories), rng);
  const slots = {
    opener: pick(openers, rng),
    action: pick(category.actions, rng),
    timing: pick(timings, rng),
    reason: pick(category.reasons, rng),
    closer: pick(closers, rng),
    emoji: pick([...category.emoji, ...sharedEmoji], rng),
  };
  const template = pick(templates, rng);
  return tidy(template.replace(/#(\w+)#/g, (_, name) => slots[name]));
}

export function generateTip(rng = Math.random) {
  for (let attempt = 0; attempt < 20; attempt++) {
    const tip = buildTip(rng);
    if (graphemeLength(tip) <= MAX_GRAPHEMES) return tip;
  }
  throw new Error('Could not generate a tip short enough to post');
}
