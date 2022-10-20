# crear una división de acuerdo al dato que ingresa

def make_division_by(n):
  return lambda x: x/n
def run():
  division_by_3 = make_division_by(3)
  print(division_by_3(18))
  division_by_5 = make_division_by(5)
  print(division_by_5(100))
  
if __name__ == '__main__':
  run()