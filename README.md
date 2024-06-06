## Steps to set up the project:

### Local setup

* create a python environment and activate it
* install all the requirements 
    > pip install -r requirements.txt
* Do the migrations
    > python manage.py makemigrations
* and now time to migrate the changes
    > python manage.py migrate
* then run the server
    > python manage.py runserver
* Access all the APIs on swagger
    > localhost:8000/api-doc/
* to create the admin run below command and provide email password etc
    > python manage.py createsuperuser
* To check the data please visit to admin panel of django by providing username and password
    > localhost:8000/admin/
* To run the testcases
    > python manage.py test

### Please provide the delivery date before changing the status of the PO to completed using admin panel as it is not mentioned any endpoint to change the delivery date
### Avg response time is in seconds
