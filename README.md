# software-architecture-2022-labs

> Protocol

### Lab I: Basic Architecture 
- Author: [Maksym Bilyk](https://github.com/mak9su4roi)

---

### Set-up
```bash
git clone https://github.com/mak9su4roi/software-architecture-2022-labs.git
```
```bash
cd software-architecture-2022-labs
```
```bash
git checkout micro_basics 
```
```bash
pipenv install
```
```bash
pipenv shell
```
```bash
chmod +x app.py
```
---

### Run
```bash
./app.py
```

---

# Interface

## facade_service
![](media/facade.png)
## logging_service
![](media/logging.png)
## messages_service
![](media/messages.png)

---

# Demo
1. GET
    - Action:
        ```bash
            curl -X 'GET' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json'
        ```
    - Result:
        ![](media/get_01.png)
2. POST
    - Action:
        ```bash
            curl -X 'POST' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                "txt": "Timendi causa est nescire"
                }'
        ```
    - Result:
        ![](media/post_01.png)
3. GET
    - Action:
        ```bash
            curl -X 'GET' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json'
        ```
    - Result:
        ![](media/get_02.png)
4. POST
    - Action:
        ```bash
            curl -X 'POST' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                "txt": "Ad astra per aspera"
                }'
        ```
    - Result:
        ![](media/post_02.png)
5. GET
    - Action:
        ```bash
            curl -X 'GET' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json'
        ```
    - Result:
        ![](media/get_03.png)
6. POST
    - Action:
        ```bash
            curl -X 'POST' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                "txt": "Ad meliora"
                }'
        ```
    - Result:
        ![](media/post_03.png)
7. GET
    - Action:
        ```bash
            curl -X 'GET' \
                'http://localhost:8000/facade_service/' \
                -H 'accept: application/json'
        ```
    - Result:
        ![](media/get_04.png)
