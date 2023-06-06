import threading
import os

def print_cube(num):
    print("Task cube assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task cube: {}".format(os.getpid()))
    print("Cube: {}" .format(num * num * num))

def print_squqre(num):
    print("Task square assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task square: {}".format(os.getpid()))
    print("Square: {}" .format(num * num))

if __name__ == "__main__":

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=print_squqre, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    print("Done")