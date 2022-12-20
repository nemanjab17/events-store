import json
import uuid
import datetime

from elasticsearch import RequestError

def init_es(es):
    try:
        es.indices.create(index="events")
        ingest_test_data(es)
    except RequestError:
        # already exists
        pass

def ingest_test_data(es):

    f = open('test-data.json')
    data = json.load(f)
    try:
        for payload in data:
            payload.update({
                "time": str(datetime.datetime.now().isoformat())
            })
            resp = es.create(index="events", id=str(uuid.uuid4()), document=payload)
    except RequestError as e:
        print(e)
        pass
    
    f.close()