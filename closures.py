# Hola 3 -> HolaHolaHola
# Emerson 2 -> EmersonEmerson
def make_repeater_off(n):
  def repeater(string):
    assert type(string) == str, "Solo puedes usar cadenas"
    return string * n
  return repeater

def run():
  repeat_5 = make_repeater_off(5)
  print(repeat_5("Emerson"))
  
if __name__ == '__main__':
  run()