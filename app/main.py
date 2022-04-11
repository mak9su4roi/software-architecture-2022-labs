import hazelcast
from hazelcast.proxy.map import Map
from hazelcast.proxy import Queue
import argparse
from enum import Enum
from time import sleep

COFFEE_BREAK = .01
TERMINAL_VALUE = -1

class HZTask(str, Enum):
    MAP_CLEAR = "MAP_CLEAR"
    MAP_PUT = "MAP_PUT"
    MAP_LCK_NO = "MAP_LCK_NO"
    MAP_LCK_PSM = "MAP_LCK_PSM"
    MAP_LCK_OPM = "MAP_LCK_OPM"
    Q_CLEAR = "Q_CLEAR"
    Q_PRD = "Q_PRD"
    Q_CNM = "Q_CNM"

def map_lck(map_: Map, task: HZTask):
    key = "1"
    map_.put_if_absent(key, 0)
    print(f"Starting: {task.value}")
    for i in range(1000):
        if i % 100 == 0: print(f"At: {i}")
        match (task):
            case HZTask.MAP_LCK_PSM:
                map_.lock(key)
                try:
                    value = map_.get(key)
                    value += 1
                    sleep(COFFEE_BREAK)
                    map_.put(key, value)
                finally:
                    map_.unlock(key)
            case HZTask.MAP_LCK_OPM:
                while (True):
                    old_value = map_.get(key)
                    new_value = old_value+1
                    sleep(COFFEE_BREAK)
                    if ( map_.replace_if_same(key, old_value, new_value) ): break
            case _:
                value = map_.get(key)
                value += 1
                sleep(COFFEE_BREAK)
                map_.put(key, value)
    print(f"Finished! Result = {map_.get(key)}")

def queue_pc(queue_: Queue, task: HZTask):
    print(f"Starting: {task.value}")
    match (task):
        case HZTask.Q_PRD:
            for item in range(100):
                while ( True ):
                    sleep(COFFEE_BREAK)
                    if (queue_.offer(item)):
                        print(f"PRODUCED ITEM: {item}")
                        break
                    else:
                        print("QUEUE IS FULL")
            print("FINISHED PRODUCING")
        case _:
            while (True):
                sleep(COFFEE_BREAK)
                item = queue_.take()
                if item == -1:
                    break
                print(f"CONSUMED ITEM: {item}")
            print("FINISHED CONSUMING")
    queue_.put(TERMINAL_VALUE)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=HZTask)
    task = HZTask(parser.parse_args().task)

    hz = hazelcast.HazelcastClient(
        cluster_name="dev",
        cluster_members=[
            "hz_001:5701",
            "hz_001:5701",
            "hz_001:5701",
        ]
    )

    match (task):
        case HZTask.MAP_CLEAR | HZTask.MAP_PUT |\
            HZTask.MAP_LCK_NO | HZTask.MAP_LCK_PSM | HZTask.MAP_LCK_OPM:
            hz_map = hz.get_map("map").blocking()
            match (task):
                case HZTask.MAP_CLEAR:
                    hz_map.clear()
                case HZTask.MAP_PUT:
                    hz_map.put_all({i:i for i in range(1000)})
                case _:
                    map_lck(hz_map, task)
        case HZTask.Q_CLEAR |\
            HZTask.Q_PRD | HZTask.Q_CNM:
            hz_queue = hz.get_queue("queue").blocking()
            match (task):
                case HZTask.Q_CLEAR:
                    hz_queue.clear()
                case _:
                    queue_pc(hz_queue, task)

    hz.shutdown()


if __name__ == "__main__":
    main()