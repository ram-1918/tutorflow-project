1. Navigate into the project directory: ./tutorflow/
2. Use 'ls' command to check if the following files exist: tutobackend, tutorfronend, docker-compose.yaml, Readme.md
3. If exist, then start setting up enviroments for both backend and frontend

## Setting up Backend
#### Go into backend folder
cd tutorbackend
#### Create the environment
python3 -m venv venv
#### Activate the environment
source venv/bin/activate
#### Install dependencies
pip3 install --upgade pip
pip3 install -r requirements.txt
#### Start the django server on port 8001
python3 manage.py runserver 8001

## Setting up Frontend
#### Go into frontend folder, make sure you are in the project's root directory
cd tutorfrontend
#### Start the vuejs node server
npm run serve
#### Access the application on the web browser
Go to http://localhost:8081/questions




