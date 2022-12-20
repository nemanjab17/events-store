import os
import uuid
import json
import time

from flask import Flask, render_template, request
from flask_restx import Api, Resource
from elasticsearch import Elasticsearch, ElasticsearchException, RequestError

from es_process import init_es

app = Flask(__name__)

api = Api(app)

es = Elasticsearch([{
    'host': os.environ["ELASTICSEARCH_HOST"], 
    'port': os.environ["ELASTICSEARCH_PORT"]}])
time.sleep(15)
init_es(es)



@api.route("/event")
class Events(Resource):

    def post(self):
        payload = request.json
        if payload is None:
            return 400, "Bad input data"
        es.create(index="events", id=str(uuid.uuid4()), document=payload)
        return payload
        


if __name__ == "__main__":
    
    app.run(debug=False,host='0.0.0.0', port=5000)