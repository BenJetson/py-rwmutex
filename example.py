from threading import Thread
from rwmutex import RWLock
from time import sleep

lock = RWLock()
shared_resource = ""


def do_writes():
    global lock
    global shared_resource

    print("writer thread waiting for write lock")

    with lock.write:
        print("writer thread received write lock")

        for i in range(10):
            print(f"writing {i}")
            shared_resource += f"{i} "
            sleep(1)

        print("writer thread will yield write lock")


def do_read(id):
    global lock
    global shared_resource

    print(f"reader thread {id} waiting for read lock")

    with lock.read:
        print(f"reader thread {id} received read lock")

        print(f"reader thread {id} found '{shared_resource}'")

        print(f"reader thread {id} will yield read lock")


threads = []

writer_thread = Thread(target=do_writes, daemon=True)
writer_thread.start()
threads.append(writer_thread)

for i in range(5):
    reader_thread = Thread(target=do_read, args=[i])
    reader_thread.start()
    threads.append(reader_thread)

for t in threads:
    t.join()
