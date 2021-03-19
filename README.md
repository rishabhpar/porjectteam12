# projectteam12

To setup for working, first clone the git repository using git clone <git url> .
Use the . to clone directly into the current directory.


## Backend
Run the following commands

### For Mac:
    cd api
    python3 -m venv venv
    source venv/bin/activate
    cd ..
    python3 -m pip install -r requirements.txt

### For Windows (Someone verify this the mac part works):
    cd backend
    python app.py (you may need to download some stuff)


To update requirements.txt, enter the following commands in the activated virtual environment:

### For Mac:
    pip install -r requirements.txt
    pip freeze > requirements.txt

Note: >> appends to the end of the file, while > overwrites the file.

### For Windows:


## Frontend
Run the following commands

### For Mac and Windows:
    cd frontend
    npm install
    npm run build
    (if needed)
    npm start


## To Test if it works:
Inside /frontend/ run the following command 'npm run build' to compile the code to a production build again.
Activate virtual environment and go to base git directory.

## To Test just the front end:
You can test it just like a regular react app. Go into the frontend directory and run the command 'npm start' or 'yarn start'. This is good because you can see UI changes every time you save the code rather than running 'npm run build' each time. Save that for end-to-end testing.