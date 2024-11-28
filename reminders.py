import random
import json
import os
from datetime import datetime

find_path = os.path.dirname(os.path.abspath(__file__))
used = os.path.join(find_path, 'used.json')
reminders_json = os.path.join(find_path, 'reminders.json')

def load_reminders():
    with open(reminders_json, encoding='utf-8') as file:
        reminders = json.load(file)['reminders']
    return reminders

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
    max_attempts = len(load_reminders())
    choice = load_reminders()[random.randint(0, max_attempts - 1)]
    
    while check_reminder(choice):
        attempts += 1
        if attempts >= max_attempts:
            print("All reminders have been used.")
            return None
        choice = load_reminders()[random.randint(0, max_attempts - 1)]
    
    add_reminder(choice)
    return choice