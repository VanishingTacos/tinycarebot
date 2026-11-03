[![Post self-care tip](https://github.com/VanishingTacos/tinycarebot/actions/workflows/post.yml/badge.svg)](https://github.com/VanishingTacos/tinycarebot/actions/workflows/post.yml)

# tinycarebot

A Bluesky bot that posts a small self-care tip every hour.

It doesn't use a fixed list of tips. Each tip is put together at random from small pieces in `src/grammar.js`: an opener, an action, a timing, a reason, a closer and an emoji. The pieces are grouped by theme (hydration, movement, rest, breathing, and more), so the action and reason in a tip always go together. Before posting, the bot checks its last 50 posts so it doesn't repeat itself.

## Setup

1. Create a Bluesky account for the bot.
2. In Bluesky, go to **Settings → Privacy and security → App passwords** and create an app password. Don't use the account's main password.
3. Push this repo to GitHub.
4. In the repo, go to **Settings → Secrets and variables → Actions** and add:
   - `BLUESKY_HANDLE`: for example, `yourbot.bsky.social`
   - `BLUESKY_APP_PASSWORD`: the app password from step 2
5. Open the **Actions** tab, enable workflows if GitHub asks, then run **Post self-care tip** by hand to test it.

After that, it posts at the top of every hour.

## Local use

Requires Node 20 or newer.

```sh
npm install
npm test          # check the generator
npm run preview   # print 10 sample tips without posting
cp .env.example .env   # then fill in your handle and app password
node --env-file=.env src/post.js   # post one tip for real
```

## Adding variety

Add actions, reasons, openers, closers or templates in `src/grammar.js`. Keep actions and reasons lowercase with no ending punctuation; the generator adds capitals and punctuation itself.

## Notes

- GitHub's scheduled runs can start a few minutes late when GitHub is busy.
- GitHub turns off scheduled workflows in repos that have had no activity for 60 days. If posts stop, re-enable the workflow in the Actions tab.
