import { test } from 'node:test';
import assert from 'node:assert/strict';
import { generateTip, graphemeLength, MAX_GRAPHEMES } from '../src/generator.js';

// Small seeded PRNG (mulberry32) so runs are repeatable.
function seeded(seed) {
  return () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

test('generated tips are well formed', () => {
  const rng = seeded(42);
  for (let i = 0; i < 2000; i++) {
    const tip = generateTip(rng);
    assert.ok(tip.length > 0);
    assert.ok(graphemeLength(tip) <= MAX_GRAPHEMES, tip);
    assert.doesNotMatch(tip, /#\w+#/, tip);
    assert.doesNotMatch(tip, / {2}/, tip);
    assert.doesNotMatch(tip, /\s[.,?!:]/, tip);
    assert.match(tip, /^[A-Z]/, tip);
  }
});

test('same seed gives the same tip', () => {
  assert.equal(generateTip(seeded(7)), generateTip(seeded(7)));
});

test('tips vary', () => {
  const rng = seeded(1);
  const tips = new Set(Array.from({ length: 200 }, () => generateTip(rng)));
  assert.ok(tips.size > 150, `only ${tips.size} unique tips`);
});
