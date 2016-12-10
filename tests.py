import httplib
import json
from datetime import datetime, timedelta

conn = httplib.HTTPConnection("localhost", port=5000)

# The time for the messeage to be sent to the slack users
desired_runtime = (datetime.now() + timedelta(seconds = 30)).strftime("%Y-%m-%d %H:%M:%S")

conn.request(
    "POST", 
    "/", 
    body=json.dumps({'time': desired_runtime, "message" : "Time For Lunch!"}),
    headers={'Content-Type': 'application/json'}
)

r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1