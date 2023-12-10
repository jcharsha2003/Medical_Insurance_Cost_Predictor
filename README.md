### How to run our web application with Reactjs and Django
# Step-1:
## Open new terminal change the directory to frontend and install all the dependencies
```
cd frontend
```
## command for installing all dependencies is 
```
npm install
npm start
```
## npm start for webpacking the application
# Step-2:

## Now simultaneously open another new terminal,side by side in this new terminal before changing the current directory run 
```
env\Scripts\activate
```
## After this change, the current directory
```
cd Insurance
```
## command to run django applicaiton you need python,pip3 and pip in ur system paths
```
pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## After running successfully you can get your medical insurance price prediction 


