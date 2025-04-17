import multiprocessing as mp

def sum_squares(start, end, queue):
    total = sum(i * i for i in range(start, end + 1))
    queue.put(total)

if __name__ == "__main__":
    queue = mp.Queue()
    ranges = [(1, 2500000), (2500001, 5000000), (5000001, 7500000), (7500001, 10000000)]
    processes = [mp.Process(target=sum_squares, args=(start, end, queue)) for start, end in ranges]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    result = sum(queue.get() for _ in ranges)
    print(f"Sum of squares: {result}")