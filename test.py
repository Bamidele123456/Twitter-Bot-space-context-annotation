import requests
import os

# Set your environment variables in your terminal
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token ="AAAAAAAAAAAAAAAAAAAAAAD0pwEAAAAAzMyx25jM6muo7BvUhUcneldRIyQ%3DfszNn1wi14oeNL0DNzTrYgQjnEnARRtHVx1faO57PQiIqe5uip"

# Twitter Space ID
space_id ="1OdKrjdAlVnKX"
# Twitter Space ID

params = {
        "expansions": "host_ids,topic_ids,invited_user_ids,creator_id,speaker_ids",
        "space.fields": "created_at,lang,invited_user_ids,participant_count,scheduled_start,started_at,title,topic_ids,updated_at,speaker_ids,ended_at",
    }

# Make the request to get information about a Twitter Space
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",
}

response = requests.get(f"https://api.twitter.com/2/spaces/{space_id}", headers=headers, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)

data = response.json()


