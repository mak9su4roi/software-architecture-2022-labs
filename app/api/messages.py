import threading
from time import sleep

class QueuePC:
    def __init__(self):
        import hazelcast
        from os import environ

        q_name, q_port = environ["queue_name"], environ["queue_port"]
        self.messages = []
        self.hz=hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=[
                f'{q_name}:{q_port}'
            ]
        )
        self.queue = self.hz.get_queue(q_name).blocking()
        print(f"successfulldy obtained queue {q_name}") 
    
    def crawl(self):
        def queue_iter():
            while True:
                msg = self.queue.take()
                if msg: 
                    print(msg)
                    yield msg
                sleep(.005)
        threading.Thread(target=lambda: [self.messages.append(msg) for msg in queue_iter()]).start()
        return self

    def put(self, msg: str):
        self.queue.put(msg)
    
    def get(self):
        return ' '.join(self.messages)