import { AtpAgent } from '@atproto/api';
import { generateTip } from './generator.js';

const RECENT_POSTS = 50;
const MAX_TRIES = 10;

async function recentTexts(agent, actor) {
  const { data } = await agent.getAuthorFeed({ actor, limit: RECENT_POSTS });
  return new Set(data.feed.map((item) => item.post.record.text));
}

async function main() {
  if (process.argv.includes('--dry-run')) {
    for (let i = 0; i < 10; i++) console.log(`- ${generateTip()}`);
    return;
  }

  const identifier = process.env.BLUESKY_HANDLE;
  const password = process.env.BLUESKY_APP_PASSWORD;
  if (!identifier || !password) {
    throw new Error('Set BLUESKY_HANDLE and BLUESKY_APP_PASSWORD');
  }

  const agent = new AtpAgent({ service: 'https://bsky.social' });
  await agent.login({ identifier, password });

  // No stored history between runs, so check the bot's own feed for repeats.
  const recent = await recentTexts(agent, agent.session.did);
  let text = generateTip();
  for (let tries = 1; recent.has(text) && tries < MAX_TRIES; tries++) {
    text = generateTip();
  }

  await agent.post({ text, createdAt: new Date().toISOString() });
  console.log(`Posted: ${text}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
