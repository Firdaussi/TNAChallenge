# TNAChallenge
Coding test for TNA

Build code:

To run the project, use the Virtual Environment
pip install virtualenv

Making and Activating the Virtual Environment:-

virtualenv venv
source venv/bin/activate

In the National Archives directory is a requirements.txt file. Use this to install requirements:
pip install -r requirements.txt

Initialisation:
You may need to run the following commands to setup the database migrations:-
  python3 manage.py makemigrations
  python3 manage.py migrate

To run:

There are two components to this project. 
Firstly, the command line management command. This connects to the National Archive api and imports data on an id by id basis.
To run this command, type:-
  python3 manage.py retrievetnaid <id>
  
This populates the table TNARecord. In fact, given the scope of the project, it only populates id, title, description and citablereference

Once a few records have been loaded, run the server:-
  python3 manage.py runserver
  
Navigate in a web browser to http://127.0.0.1:8000/
This is the default page and should list all record id's currently held on the database
Each id is clickable and will lead you to a detail page giving the required level of information.

Tests:

I have added a few tests to check on the basic integrity of the model and the views.
To run the tests, please type the following:-
  python3 manage.py test
  
Assumptions:

id is unique.
All other fields can be empty.
Only 4 fields are referenced so most data is discarded.

