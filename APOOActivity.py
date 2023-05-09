from typing import Tuple, List

class DatosMeteorologicos:
   def __init__(self, nombre_archivo: str):
       self.nombre_archivo = r"C:\Users\ASUS\PycharmProjects\DiscretasRSA\Actividad"
       self.direcciones_viento = []

   def procesar_datos(self) -> Tuple[float, float, float, float, str]:
       prom_temp = 0
       prom_humedad = 0
       prom_presion = 0
       promedio_viento = 0
       num_mediciones = 0

       with open(self.nombre_archivo, "r") as archivo:
           for linea in archivo:
               if "Temperatura" in linea:
                   temperatura = float(linea.split(":")[1])
                   prom_temp += temperatura
               elif "Humedad" in linea:
                   humedad = float(linea.split(":")[1])
                   prom_humedad += humedad
               elif "Presion" in linea:
                   presion = float(linea.split(":")[1])
                   prom_presion += presion
               elif "Viento" in linea:
                   viento, direccion_viento = linea.split(":")[1].split(",")
                   promedio_viento += float(viento)
                   self.direcciones_viento.append(direccion_viento.strip())
                   num_mediciones += 1

       temp_promedio = prom_temp / num_mediciones
       humedad_promedio = prom_humedad / num_mediciones
       presion_promedio = prom_presion / num_mediciones
       velocidad_viento = promedio_viento / num_mediciones

       direcciones_grados = []
       for direccion in self.direcciones_viento:
           if direccion == 'N':
               direcciones_grados.append(0)
           elif direccion == 'NNE':
               direcciones_grados.append(22.5)
           elif direccion == 'NE':
               direcciones_grados.append(45)
           elif direccion == 'ENE':
               direcciones_grados.append(67.5)
           elif direccion == 'E':
               direcciones_grados.append(90)
           elif direccion == 'ESE':
               direcciones_grados.append(112.5)
           elif direccion == 'SE':
               direcciones_grados.append(135)
           elif direccion == 'SSE':
               direcciones_grados.append(157.5)
           elif direccion == 'S':
               direcciones_grados.append(180)
           elif direccion == 'SSW':
               direcciones_grados.append(202.5)
           elif direccion == 'SW':
               direcciones_grados.append(225)
           elif direccion == 'WSW':
               direcciones_grados.append(247.5)
           elif direccion == 'W':
               direcciones_grados.append(270)
           elif direccion == 'WNW':
               direcciones_grados.append(292.5)
           elif direccion == 'NW':
               direcciones_grados.append(315)
           elif direccion == 'NNW':
               direcciones_grados.append(337.5)

       grados_promedio = sum(direcciones_grados) / len(direcciones_grados)

       direccion_promedio = obtener_direccion_promedio(grados_promedio)

       return temp_promedio, humedad_promedio, presion_promedio, velocidad_viento, direccion_promedio

def obtener_direccion_promedio(grados: float) -> str:

    direccion = ""
    if grados >= 348.75 or grados < 11.25:
        direccion = "N"
    elif grados < 33.75:
        direccion = "NNE"
    elif grados < 56.25:
        direccion = "NE"
    elif grados < 78.75:
        direccion = "ENE"
    elif grados < 101.25:
        direccion = "E"
    elif grados < 123.75:
        direccion = "ESE"
    elif grados < 146.25:
        direccion = "SE"
    elif grados < 168.75:
        direccion = "SSE"
    elif grados < 191.25:
        direccion = "S"
    elif grados < 213.75:
        direccion = "SSW"
    elif grados < 236.25:
        direccion = "SW"
    elif grados < 258.75:
        direccion = "WSW"
    elif grados < 281.25:
        direccion = "W"
    elif grados < 303.75:
        direccion = "WNW"
    elif grados < 326.25:
        direccion = "NW"
    elif grados < 348.75:
        direccion = "NNW"
    return direccion


ruta_archivo = r"C:\Users\ASUS\PycharmProjects\DiscretasRSA\Actividad" 
datos = DatosMeteorologicos(ruta_archivo)
