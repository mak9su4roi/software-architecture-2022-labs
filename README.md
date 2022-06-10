# software-architecture-2022-labs

> Protocol

### Lab IV: Micro_mq
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
git checkout micro_mq
```

---

### Run

- Part I:
    - Launch a cluster
        ```bash
        kubectl apply -f minikube.yaml \
            && sleep 15 \
            && kubectl get pods \
            && kubectl port-forward facade 8080:8080
        ```
        ![](media/1.png)

- Part II:
    - Send 10 messages
        ```bash
        cat ./write_messages.sh \
            && ./write_messages.sh
        ```
        ![](media/2.png)

- Part III
    - Message distribution between `logging` services
        ```bash
        ./read_messages.sh \
            && kubectl logs logging-0 -c logging \
            && kubectl logs logging-1 -c logging \
            && kubectl logs logging-2 -c logging
        ```
        ![](media/3.png)
 
- Part IV
    - Message distribution between `messages` services
        ![](media/4.png)


- Part V:
    - Read messages from `logging` and `messages` services
        ![](media/5.png)

- Part VI:
    - Stop cluster
        ```bash
        kubectl delete -f minikube.yaml \
            && kubectl get pods
        ```
        ![](media/6.png)

