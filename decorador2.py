# definir en cuanto tiempo se tarda una función en ejecutarse

from datetime import datetime


def execute_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        result_time = final_time - initial_time

        print("pasaron + de " + str(result_time.total_seconds()) + " segundos")
    return wrapper


@execute_time
def random_func():
    for _ in range(1, 1000000):
        pass


@execute_time
def suma(a: int, b: int) -> int:
    return a + b


@execute_time
def saludo(nombre="Emerson"):
    print("hola " + nombre)


random_func()
suma(5, 5)
saludo("gabriela")
