# FastApi Reservations API
##### Reservations REST API App based on Python FastApi framework

**HOT TO START APP**
--

1. *Start app and build required Docker containers:*
``docker-compose up -d``
1. *Exec into running container:*
``docker exec -it res_api bash``
1. *Start uvicorn dev server with reload option:*
``uvicorn app.main:app --host 0.0.0.0 --port 80 --reload``

App is available on ``5082`` port
--
    http://127.0.0.1:5082