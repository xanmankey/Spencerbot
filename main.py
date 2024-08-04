import os

from dotenv import load_dotenv
from slack_bolt import App

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

load_dotenv()

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
DEBUG_BOT_CAHNNEL_ID = os.getenv("DEBUG_BOT_CAHNNEL_ID")
BOT_CHANNEL_ID = os.getenv("BOT_CHANNEL_ID")

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET, name="Spencerbot")
# scheduler = BackgroundScheduler()


# Runs every sunday at 8; scheduled via pythonanywhere
def weekly_reminder():
    """Send a weekly reminder to the bot channel"""
    print("Sending weekly reminder")
    app.client.chat_postMessage(
        channel=BOT_CHANNEL_ID, text="Don't forget to submit your weekly updates!"
    )


# Adding one slash command for getting event ideas
@app.command("/cutting")
def cutting(ack, respond, command):
    ack()
    respond(
        f"This test command will probably be cut (just like Pedro's doing), <@{command['user_id']}>!"
    )


from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)
# scheduler.add_job(weekly_reminder, CronTrigger(hour=20, day_of_week=1))
# scheduler.start()


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    print("Received a request")
    return handler.handle(request)


# def main():
#     scheduler.add_job(weekly_reminder, CronTrigger(hour=20, day_of_week=1))
#     scheduler.start()

#     # Starts the event loop (if desired)
#     handler = SocketModeHandler(app, SLACK_APP_TOKEN)
#     handler.start()

if __name__ == "__main__":
    # main()
    # flask_app.run(port=3000)
    weekly_reminder()
