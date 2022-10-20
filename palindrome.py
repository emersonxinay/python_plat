# muestra si una palabra se escribe al revez lo mismo
def is_palindrome(string: str)->bool:
  string = string.replace(" ", "").lower()
  return string == string[::-1]

def run():
  print(is_palindrome("ana"))
  # para obetener una mejor respuesta a los errores de argumentos 
  # usa lo siguiente
  # mypy archivo.py --check-untyped-defs

  # print(is_palindrome(100))
  
if __name__ == '__main__':
  run()