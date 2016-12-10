from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from slack_wrapper import SlackWrapper

MY_APP_AUTH_TOKEN = "YOUR-AUTH-TOKEN"
SCHEDULED_EVENT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

app = Flask(__name__)

def create_slack_message_task(job_execution_time, message_text):
	scheduler.add_job(
    	slack_api.send_direct_message_to_all_users, 
    	'date', 
    	run_date=job_execution_time, 
    	args=[message_text])

@app.route("/", methods=["POST"])
def submit_scheduled_message():
    data = request.get_json(force=True)
    parsed_run_time = datetime.strptime(data["time"], SCHEDULED_EVENT_DATE_FORMAT)
    
    # Time and Data validation should go here......
    
    create_slack_message_task(parsed_run_time, data["message"])
    return "Slack request has been submited"
 

if __name__ == "__main__":
    slack_api = SlackWrapper(MY_APP_AUTH_TOKEN)
    scheduler = BackgroundScheduler()
    scheduler.start()
    app.run(debug = True, host="0.0.0.0")
