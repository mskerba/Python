import time

def ft_progress(lst):
    l = len(lst)
    start_time = time.time()
    for i, elem in enumerate(lst):
        progress = (i + 1) / l
        elapsed_time = time.time() - start_time
        eta = elapsed_time * (1 - progress) / progress
        progress_bar = "[{:{}}] {:>3}% | elapsed time {:.2f}s ETA: {:.2f}s".format("=" * int(progress * 20), 20, int(progress * 100), elapsed_time, eta)
        yield elem
        print("\r" + progress_bar, end="")
        time.sleep(0.01)
    print("\r" + " " * len(progress_bar) + "\r", end="")

# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += (elem + 3) % 5
#     time.sleep(0.01)
# print()
# print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
