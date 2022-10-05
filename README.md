In integrated terminal:
    Step 1:
        docker-compose up -d --build

    Step 2:
        docker ps (search your container ID, image name = snetwork-web)

    Step 3:
        docker exec -t -i "container ID" bash

    Step 4:
        python manage.py migrate
    
    Step 5:
        in browser open: localhost:8000