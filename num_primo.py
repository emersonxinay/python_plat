# mostramos si el numeros es primo o no

def is_number_prime(number: int)-> bool:
  list_prime = [x for x in range(2, number)
                if number % x == 0
                ]
  return len(list_prime)== 0

def run():
  number: int = 59
  list_number_prime: bool = is_number_prime(number)
  print(f'Is {number} un numero primo?  {list_number_prime}')  

if __name__ == '__main__':
  run()