# Events SPA

## Launching the project

Run `git clone https://github.com/alexfurmenkov/Events.git`

### Docker
1. Run `docker-compose up` if building for the first time or `docker-compose up --build` to rebuild
2. Wait 
3. **Run migrations in the running "backend" container**

    _Using PyCharm:_
   
    Services -> Docker -> events-full -> backend-> /events-full_backend_1
    
    Click "Exec"
    
    Run the following commands:
    
    `python /code/manage.py makemigrations events`
    
    `python /code/manage.py migrate`
    
    _Using terminal:_
    
    Run `docker ps`
    
    Copy CONTAINER ID of events-full_backend image
    
    Run `docker exec -it <CONTAINER ID> bash`
    
    Run `python /code/manage.py makemigrations events`
    
    Run `python /code/manage.py migrate`
        
3. Navigate to http://localhost:8080 to see frontend and to http://localhost:8000 see backend 

## Stack
### Frontend
Vue.js
### Backend
Django

DRF

PostgreSQL