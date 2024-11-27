import random
import json
import os
from datetime import datetime

find_path = os.path.dirname(os.path.abspath(__file__))
used = os.path.join(find_path, 'used.json')

reminders = [
    "Take a quick moment to get a sip of water. 💧",
    "Time to stretch! Reach for the sky and touch your toes. 🧘",
    "How about a deep breath? Inhale... Exhale... 🌬️",
    "Check your posture! Sit up straight and relax your shoulders. 🪑",
    "Maybe it’s time for a short walk? A few steps can clear your mind. 🚶",
    "Give your eyes a break. Look away from the screen for a minute. 👀",
    "Listen to your favorite song for a quick mood boost. 🎵",
    "Take a few minutes to meditate and clear your mind. 🧘‍♂️",
    "Write down something you're grateful for today. ✍️",
    "Stand up and do a quick dance to get your blood flowing. 💃",
    "Take a moment to organize your workspace. 🗂️",
    "Step outside and get some fresh air. 🌳",
    "Do a quick hand massage to relieve tension. ✋",
    "Read a few pages of a book you enjoy. 📖",
    "Take a moment to reflect on your accomplishments today. 🌟",
    "Pause and check in with yourself. How are you feeling right now? 🤔",
    "Take a moment to stretch your wrists and fingers. 💻🖐️",
    "Drink some tea or coffee—mindfully savor the taste. ☕",
    "Close your eyes for a minute and visualize a calming place. 🏞️",
    "Try a breathing exercise: inhale for 4 seconds, hold for 4, exhale for 4. 🌬️",
    "Tidy a small corner of your room or desk for clarity. 🧹",
    "Treat yourself to a healthy snack or a piece of fruit. 🍎",
    "Give yourself a gentle face massage to refresh. 😌",
    "Reconnect with someone you care about—send a quick message. 💌",
    "Step away and do 5-10 jumping jacks for energy. 🤸",
    "Spend a moment appreciating the view outside your window. 🪟",
    "Write a short affirmation or mantra for positivity. ✨",
    "Put on a fun playlist and sway to the rhythm. 🎶",
    "Take a moment to doodle or sketch something creative. 🎨",
    "Make a quick list of three things you want to focus on next. 📋",
    "Roll your shoulders back and forth to release tension. 🤗",
    "Light a candle or use essential oils for a calming scent. 🕯️",
    "Take 5 minutes to declutter your thoughts by journaling. 🖊️",
    "Put down your phone and just enjoy the silence for a moment. 📵",
    "Do a quick neck stretch—side to side and front to back. 🙆",
    "Check your hydration—refill your water bottle if needed. 🚰",
    "Listen to the sounds around you and focus on the present. 🌍",
    "Smile, even if there's no one around—it can lift your mood! 😊",
    "Loosen up your body with a quick twist from side to side. 🔄",
    "Give yourself permission to take a guilt-free break. 🛌",
    "Watch a funny video or meme to make yourself laugh. 😂",
    "Adjust your lighting—natural light can improve your mood. 🌞",
    "Set a timer and rest your eyes for a few minutes. 🕒",
    "Treat yourself to a quick mindfulness exercise: focus on 5 things you see, 4 you feel, 3 you hear, 2 you smell, and 1 you taste. 🌟",
    "Think of one small goal you can achieve today and write it down. 🏁",
    "Do a quick back stretch—touch your toes or arch gently. 🧍‍♂️",
    "Hug a pet or a pillow for comfort. 🐾",
    "Take a mini tech detox—step away from screens for 10 minutes. 📴",
    "Play with a stress ball or fidget toy to release tension. 🌀",
    "Remind yourself: It’s okay to not be productive all the time. 🌈",
    "Pause and take a moment to listen to your heartbeat. ❤️",
    "Stretch your arms out wide like you’re giving the world a big hug. 🤗",
    "Drink a glass of water and imagine it recharging you like a battery. 🔋",
    "Write down a small victory from today, no matter how tiny. 🏆",
    "Rub your temples or do a gentle scalp massage to relax. 💆",
    "Open a window and feel the breeze on your face. 🌬️",
    "Change your posture—try standing if you’ve been sitting, or vice versa. 🔄",
    "Pause and think of three people who make you smile. 😊",
    "Enjoy a piece of chocolate or your favorite treat slowly. 🍫",
    "Put your hand on your chest and say something kind to yourself. 💖",
    "Take 10 seconds to shake out your arms and legs to release tension. 🕺",
    "Think of a place you love and imagine being there. 🌊",
    "Take a break and do a small act of kindness for someone. 🌸",
    "Pick up a nearby object and observe its texture, color, and details. 🖌️",
    "Unplug from notifications for a set time and just be present. 🔕",
    "Try a new stretch: bend to the side and reach your arm overhead. 🌈",
    "Smile at your reflection in the mirror—it can be surprisingly uplifting! 🪞",
    "Create a short list of things you’d like to do just for fun. 🎯",
    "Visualize your favorite meal or snack and treat yourself to it soon. 🍽️",
    "Sit quietly and notice the rhythm of your breathing—no need to change it. 🌾",
    "Write a small thank-you note to yourself for something you handled well today. ✍️",
    "Snap a photo of something beautiful or interesting around you. 📸",
    "Put on your coziest sweater or blanket for extra comfort. 🧣",
    "Look at an old photo or memory that brings you joy. 🖼️",
    "Do a slow, intentional shoulder roll and feel the tension melt away. 💆‍♂️",
    "Take a moment to practice gratitude—think of three things you're thankful for. 🙏",
    "Do a quick leg stretch—stand up and touch your toes. 🦵",
    "Take a few deep breaths and focus on the sensation of breathing. 🌬️",
    "Write down a positive affirmation and repeat it to yourself. ✨",
    "Take a moment to appreciate something beautiful around you. 🌸",
    "Do a quick mindfulness exercise: focus on your senses for a minute. 🧘",
    "Take a break and enjoy a healthy snack. 🍇",
    "Spend a few minutes doing something creative, like drawing or writing. 🎨",
    "Take a moment to reflect on a recent achievement. 🏅",
    "Do a quick body scan meditation to relax. 🧘‍♀️",
    "Take a moment to connect with nature, even if it's just looking at a plant. 🌿",
    "Do a quick facial exercise to relax your face muscles. 😊",
    "Take a moment to set a small, achievable goal for the day. 🎯",
    "Do a quick breathing exercise: inhale for 4 seconds, hold for 7, exhale for 8. 🌬️",
    "Take a moment to appreciate yourself and your efforts. 🌟",
    "Do a quick stretch for your back and shoulders. 🧍",
    "Take a moment to enjoy a piece of fruit or a healthy snack. 🍏",
    "Do a quick meditation to clear your mind. 🧘",
    "Take a moment to appreciate the present moment. 🌼",
    "Do a quick exercise to get your blood flowing, like jumping jacks. 🤸‍♂️",
    "Put on a face mask or skincare treatment for some self-pampering. 💆‍♀️",
    "Take a few moments to step back and look at the big picture. 🌍",
    "Play with your pet or simply watch them be cute for a quick mood lift. 🐕",
    "Listen to the sounds of nature, whether it’s rain, birds, or wind. 🌧️🐦",
    "Give yourself permission to say no to something that drains you. ❌",
    "Try a new breathing technique like box breathing for calmness. 📦",
    "Organize your thoughts by doing a quick mental check-in. 🧠",
    "Light a scented candle or incense to set a peaceful atmosphere. 🕯️",
    "Step outside and take a few deep breaths of fresh air. 🌬️",
    "Play a guided relaxation or body scan meditation. 🎧",
    "Drink a cup of herbal tea, and let it warm you up from the inside. 🍵",
    "Celebrate a small success today, no matter how minor it seems. 🎉",
    "Do a gentle ankle or wrist rotation to release any stiffness. 🔄",
    "Watch a short clip or video that makes you laugh out loud. 😂",
    "Take a moment to list 5 things you’re grateful for. 🙏",
    "Practice mindful eating: slow down and savor each bite. 🍽️",
    "Give yourself a few minutes to listen to your favorite podcast. 🎙️",
    "Step away from technology and just be present in the moment. 🌿",
    "Try journaling for a few minutes to clear your mind. ✍️",
    "Do a quick gratitude walk, acknowledging the beauty around you. 🚶‍♀️",
    "Take a moment to stretch your legs and back. 🦵",
    "Write down a positive affirmation and keep it in sight. ✨",
]

def get_reminder():
    return random.choice(reminders)

# Check if the reminder has been used
def check_reminder(reminder):
    with open(used, 'r') as f:
        data = json.load(f)
    return reminder in data.get('used_reminders', [])

# Add the reminder to the used list
def add_reminder(reminder):
    with open(used, 'r') as f:
        data = json.load(f)
    
    if 'used_reminders' not in data:
        data['used_reminders'] = []
    
    data['used_reminders'].append(reminder)
    
    with open(used, 'w') as f:
        json.dump(data, f, indent=4)

# Ensure date is correct, clear reminders if necessary
def ensure_date():
    today = datetime.now().strftime('%Y-%m-%d')
    # today = "2024-11-29"  # For testing purposes
    
    try:
        with open(used, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if data.get('date') != today:
        data = {'date': today, 'used_reminders': []}  # Reset reminders and update date
    
    with open(used, 'w') as f:
        json.dump(data, f, indent=4)

# Get the final reminder
def final_choice():
    ensure_date()
    
    with open(used, 'r') as f:
        data = json.load(f)

    attempts = 0
    max_attempts = len(reminders)
    choice = get_reminder()
    
    while check_reminder(choice):
        attempts += 1
        if attempts >= max_attempts:
            print("All reminders have been used.")
            return None
        choice = get_reminder()
    
    add_reminder(choice)
    return choice

