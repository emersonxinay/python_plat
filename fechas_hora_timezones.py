from datetime import datetime
from xmlrpc.client import boolean
import pytz
# fecha y hora de bogota
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, hora: %H:%M:%S"))

# fecha y hora de Lima
lima_timezone = pytz.timezone("America/Lima")
lima_date = datetime.now(lima_timezone)
print("Lima: ", lima_date.strftime("%d/%m/%Y, hora: %H:%M:%S"))


# Fecha y hora de Santiago

santiago_timezone = pytz.timezone("America/Santiago")
santiago_date = datetime.now(santiago_timezone)
print("Santiago: ", santiago_date.strftime("%d/%m/%Y, hora: %H:%M:%S"))
