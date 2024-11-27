from atproto import Client
from dotenv import load_dotenv
import os
from reminders import final_choice

load_dotenv()

# Access the environment variables
bluesky_username = os.getenv("BLUESKY_USERNAME")
bluesky_password = os.getenv("BLUESKY_PASSWORD")

reminder = final_choice()

# instantiate the client
client = Client()
client.login(bluesky_username, bluesky_password)

# send the message
try:
    client.send_post(reminder)
except Exception as e:
    print(e)