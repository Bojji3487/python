import threading,time,multiprocessing

def infint_loop():
    i=1
    while i>0:
        time.sleep(2)
        print('hey')

def print_once():
    print('heyyy')

def print_five():
    for i in range(1,6):
        print('heya')

# t1=threading.Thread(target=infint_loop)
# t2=threading.Thread(target=print_five)
# t3=threading.Thread(target=print_once)
# t1.start()
# t2.start()
# t3.start()

print(multiprocessing.cpu_count())