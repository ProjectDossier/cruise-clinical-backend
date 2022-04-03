# Cruise Clinical Backend

Backend service for Cruise Clinical Trails

## Requirements:
```
1. Mongo DB 
2. Dataset with patient records.
```


## Mongo Build:

```bash
cd ./mongo
docker-compose up -d
```

## Docker Build: 

```bash
docker build -t <docker image name>:tag .
docker-compose up -d
```
Update the env in docker-compose.

## Volume mounts
1. <host-data-path>:/python/data



## API for video enrichment

### Request
`POST http://host-name:service-port/post_queries`

```json
{
  "id" : "Patient ID", 
  "query" : "Query for Current symptoms|Query for other relevant options",
}
```
###Request
`GET http://host-name:service-port/get_patients`

-Get list of patients related to mentioned name,date of birth and medical conditions
```json
{
  "name" : "name of the patient", 
  "dob" : "date of birth (dd/mm/yyyy)", 
  "conditions" : "medical conditions e.g. (cancer)",
}
```
### Response

    200

    {id:{name:ABC,dob:1998-02-11,texts=i am having...}}


## Demo Script:

```python
import json
import requests

# get patient list for specific conditions
a=requests.get('http://0.0.0.0:8083/get_patients',data=json.dumps({'dob':'','name':'william'}))

# post queries in the database
b=requests.post('http://0.0.0.0:8083/post_queries',data=json.dumps({'id':'6a9252fa-0132-46a1-8e56-c18f7cd80881','query':'Parker|hmmm'}))
```
