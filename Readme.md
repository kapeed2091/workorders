# Work Order - Task Management


## Setup virtualenv

```bash
pip install virtualenv
virtualenv .venv -p python3.6
```

## Install requirements

```bash
pip install -r requirements.txt
pip install -r requirements_deploy.txt
```

## To run django management commands & usage (in local env)

```bash
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=workorders.settings.local
python manage.py migrate
python manage.py runserver 8000 #(Runs on 8000 port)
```

# Workorders Application

Objective of this application is to enable user to manage workers and orders.
User can create worker and delete worker.
User can create work-orders and assign workers to work-order. 
A work-order cannot have more than 5 workers assigned to it.
User should be able to fetch work orders for a specific worker sorted by datetime. 

## Functionality / User Stories

* Create a worker (name, email, company_name)
* Delete a worker
* Create a work order
* Assigning a worker to an order (an order can have max 5 workers)
* Fetch all work orders: 
    * For a specific worker
    * Sorted by deadline

## REST APIs

### Create Worker

```bash
curl -d '{"name":"Deepak", "email":"kapeed2091@gmail.com", "company_name": "iB"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/task-management/create-worker/
```

### Delete Worker

```bash
curl -d '{"worker_id":9}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/task-management/delete-worker/
```

### Create Work Order

```bash
curl -d '{"title": "Test Order", "description": "Test Description", "deadline": "2019-12-31"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/task-management/create-work-order/
```

### Assign Worker to Order

```bash
curl -d '{"order_id": 4, "worker_id":9}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/task-management/assign-worker/
```

### Get Work Orders

```bash
curl -d '{"worker_id":6}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/task-management/get-work-orders/
```

## Tests

```bash
python manage.py test task_management.tests

# Tests are written for model functions
# Tests can be written at API level as well

# To check for coverage:
# pip install coverage
# coverage run manage.py test task_management.tests
# coverage report -m
```

## Deployment

CI/CD is enabled for this project. A build is triggered on Codeship when a commit is made.
This project is packaged and pushed to AWS-Lambda. For database storage, AWS Aurora Serverless is used. 
AWS S3 is used to store static files. 

Build status can be checked on github (https://github.com/kapeed2091/workorders/tree/sqreen).

An admin panel (https://pbxgttj1o2.execute-api.ap-south-1.amazonaws.com/dev/admin) is setup, to view data present in tables.
Login with the credentials ---> username: sqreen, password: Sqreen123*

Above listed REST API calls can be made with URL: https://pbxgttj1o2.execute-api.ap-south-1.amazonaws.com/dev/ (instead of localhost:8000) 

# Sqreen Application

```
If needed set appropriate values in "sqreen_demo.config" file
```

## Check Signature

```
Reference: sqreen_demo.views.check_signature
```

## Dispatch Notification to multiple targets

### Email

```
Reference: sqreen_demo.dispatchers.email_dispatcher.EmailDispatcher
```

### Slack

```
Reference: sqreen_demo.dispatchers.slack_dispatcher.SlackDispatcher
```

### SMS

```
Reference: sqreen_demo.dispatchers.sms_dispatcher.SMSDispatcher
```

### Log

```
Reference: sqreen_demo.dispatchers.log_dispatcher.LogDispatcher
```

### HTTP

```
Reference: sqreen_demo.dispatchers.http_dispatcher.HTTPDispatcher
```

## Tests

```
Reference: sqreen_demo.tests.test_check_signature.TestCheckSignature
```

To run tests,
```
python manage.py test sqreen_demo
```
