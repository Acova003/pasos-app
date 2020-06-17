from datetime import datetime
from datetime import timedelta
import time
import httplib2
from googleapiclient import discovery

def get_steps_from_api(creds):
    today = datetime.combine(datetime.today().date(), datetime.min.time()). \
        replace(hour=7)
    yesterday = today - timedelta(days=1)
    start = int(yesterday.timestamp()) * 1000
    end = int(today.timestamp()) * 1000

    print(start)
    print(end)

    fitness_service = discovery.build('fitness', 'v1', credentials=creds)

    body = {
        "aggregateBy": [{
            "dataSourceId":
            "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
        }],
        "bucketByTime": { "durationMillis": 86400000 },
        "startTimeMillis": start,
        "endTimeMillis": end
    }

    response = fitness_service.users().dataset(). \
              aggregate(userId="me", body=body, x__xgafv=None). \
              execute()

    try:
        return response["bucket"][0]["dataset"][0]["point"][0]["value"][0]["intVal"]
    except:
        return 0
