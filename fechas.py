from datetime import datetime
mi_fecha = datetime.now()
print(mi_fecha)

mi_fecha_letras = mi_fecha.strftime('%d/%m/%Y')
print(f'Formato latam: {mi_fecha_letras} ')

mi_fecha_letras = mi_fecha.strftime('%m/%d/%Y')
print(f'Formato USA: {mi_fecha_letras} ')

mi_fecha_letras = mi_fecha.strftime(
    'Estamos en el año: %Y y en el mes de %m ')
print(f'Formato random:  {mi_fecha_letras} ')
