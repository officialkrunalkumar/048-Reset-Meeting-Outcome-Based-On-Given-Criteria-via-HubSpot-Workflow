import os
import time
import random
import requests

def main(event):
    token = os.getenv("RevOps")
    mid = event.get("inputFields").get("id")
    outcome = event.get("inputFields").get("outcome")
    mtype = event.get("inputFields").get("type")

    # Check if outcome is "RESCHEDULED" and mtype contains "overview"
    if outcome == "RESCHEDULED" and "Zeni Overview" in mtype:
        delay = random.uniform(1, 10)
        time.sleep(delay)
        url = f'https://api.hubapi.com/crm/v3/objects/meetings/{mid}'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'properties': {
                'hs_meeting_outcome': ""
            }
        }
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            answer = 1
        else:
            answer = 0
    else:
        answer = 0

    return {
        "outputFields": {
            'id': mid,
            'answer': answer
        }
    }