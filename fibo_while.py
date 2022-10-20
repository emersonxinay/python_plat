import time


def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = a+b


if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
