# Event store

This repository contains a demo application demonstrating storing arbitrary events ingested by HTTP. 

## Local environement

To run the system locally, use `docker-compose up` . On start, test data will be ingested in the store.

## Listening for events
Web server is listening for events on http://localhost:5000/event . Server is implemented in Python - Flask framework

## Storing events
Arbitrary payload is accepted and stored in Elasticsearch database.

## Displaying events
All ingested events can be displayed using kibana on http://localhost:6501

First time kibana is started, index pattern under the name events* should be created. Data will then be visible in the discover section.


## TLDR
1. Clone the repository 
2. Run everything using `Docker`
```
docker-compose up 
```
3. Go to `http://localhost:6501` to open up kibana
4. Create an index pattern `events-*`
5. Navigate to discover tab
