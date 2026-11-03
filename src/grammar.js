// Building blocks for generated tips. Nothing here is a finished tip --
// generator.js stitches these pieces together at random.
//
// Each category keeps its actions and reasons together so a tip never pairs
// an action with a reason that doesn't fit it.
//   actions: imperative phrases, lowercase, no trailing punctuation
//   reasons: full clauses, lowercase, no trailing punctuation

export const categories = {
  hydration: {
    actions: [
      'drink a glass of water',
      'refill your water bottle',
      'take a few slow sips of water',
      'make yourself a cup of tea',
      'grab something to drink',
    ],
    reasons: [
      'your brain works better when it is hydrated',
      'thirst often shows up as tiredness',
      'your body has been working hard for you',
      'a little water can lift a foggy head',
    ],
    emoji: ['💧', '🫖', '🥤'],
  },
  movement: {
    actions: [
      'roll your shoulders back a few times',
      'stand up and stretch your arms overhead',
      'take a short walk around the room',
      'gently tilt your head side to side',
      'wiggle your fingers and toes',
      'unclench your jaw and drop your shoulders',
    ],
    reasons: [
      'your body holds on to stress you might not notice',
      'sitting still for a long time makes everything stiff',
      'a little movement can reset your whole mood',
      'your muscles will thank you later',
    ],
    emoji: ['🌿', '🙆', '🚶'],
  },
  rest: {
    actions: [
      'close your eyes for a moment',
      'look away from your screen and find something far away',
      'take a real break, not a scrolling break',
      'rest your eyes and let your face relax',
      'lie down for a bit',
    ],
    reasons: [
      'rest is not something you have to earn',
      'your eyes have been doing a lot today',
      'being tired is information, not a failure',
      'you get more done when you are not running on empty',
    ],
    emoji: ['☁️', '🌙', '😌'],
  },
  breathing: {
    actions: [
      'take three slow, deep breaths',
      'breathe in for four counts and out for six',
      'notice your breath without changing it',
      'let out a big sigh',
      'put a hand on your chest and breathe slowly',
    ],
    reasons: [
      'slow breathing tells your body it is safe',
      'a long exhale can calm a racing mind',
      'you might have been holding your breath without noticing',
      'your breath is always there to come back to',
    ],
    emoji: ['🌬️', '🍃', '🫧'],
  },
  mind: {
    actions: [
      'write down one thing that is on your mind',
      'name one thing that has gone okay so far',
      'pick just one small thing to focus on',
      'let go of one task that can wait',
      'notice five things you can see around you',
    ],
    reasons: [
      'your thoughts get lighter once they are out of your head',
      'you do not have to hold everything at once',
      'small wins still count',
      'it is okay if today is a slow day',
    ],
    emoji: ['📝', '🧠', '✨'],
  },
  connection: {
    actions: [
      'send a kind message to someone you like',
      'text a friend you have not talked to in a while',
      'tell someone you appreciate them',
      'ask someone how they are really doing',
      'send someone a quick hello',
    ],
    reasons: [
      'people often miss you more than you think',
      'connection is good for both of you',
      'a tiny message can make someone’s whole day',
      'you do not have to go through things alone',
    ],
    emoji: ['💌', '🫶', '💛'],
  },
  environment: {
    actions: [
      'open a window and let some fresh air in',
      'step outside for a minute',
      'tidy one small spot near you',
      'adjust your lighting so it is easier on your eyes',
      'put on a song you love',
      'find a little sunlight',
    ],
    reasons: [
      'your space can change how you feel',
      'a small change of scenery goes a long way',
      'fresh air helps clear your head',
      'you deserve a space that feels good to be in',
    ],
    emoji: ['🪟', '🌞', '🎶'],
  },
  kindness: {
    actions: [
      'speak to yourself the way you would speak to a friend',
      'forgive yourself for something small',
      'eat something nourishing',
      'check in with how you are actually feeling',
      'give yourself permission to do less',
    ],
    reasons: [
      'you are doing better than you think',
      'being hard on yourself does not make things easier',
      'you are allowed to take up space',
      'you matter, even on unproductive days',
    ],
    emoji: ['🌸', '🌱', '💖'],
  },
};

// Empty strings let a slot be skipped some of the time.
export const openers = [
  '',
  '',
  'gentle reminder:',
  'hey friend,',
  'tiny care check:',
  'hi there,',
  'just a nudge:',
  'friendly reminder:',
];

export const timings = [
  'right now',
  'before your next task',
  'when you get a chance',
  'in the next few minutes',
];

export const closers = [
  '',
  'you deserve it.',
  'it is okay to go slow.',
  'you are doing great.',
  'be gentle with yourself.',
  'one small thing is enough.',
  'take care of you.',
];

export const sharedEmoji = ['', '🌱', '✨', '🫶'];

// Sentence shapes. #slot# names map to the pieces above.
export const templates = [
  '#opener# #action# #timing#. #reason#. #closer# #emoji#',
  '#opener# #action# #timing#. #closer# #emoji#',
  '#opener# #reason#, so #action# #timing#. #emoji#',
  '#opener# could you #action# #timing#? #reason#. #emoji#',
  '#opener# if you can, #action#. #reason#. #emoji#',
  '#opener# #action#. #closer# #emoji#',
];
