from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv() #carga las variables de entorno de .env
MONGODB_URI = os.getenv('url_bd')


client = MongoClient("mongodb://localhost:27017")
db = client["yovoybd"]
print("Conectado a MongoDB")

import vehiculos
import sensores
import conducciones
import mantenimientos
import disponibilidades

if __name__ == "__main__":
    vehiculo = {
        "id_vehiculo": "V001",
        "aceleracion": 9.26,
        "frenado": -3.4,
        "velocidad_variacion": "2.5 km",
        "horas_operacion": "10 hrs",
        "temperatura_motor": "95.5 °C",
        "masotomocineticas": "ligeras",
        "vibracion": 2.4,
        "modelo": "mercedes",
        "marca": "Mercedes",
        "año": 2018,
        "kilometraje": 120000,
        "estado_actual": "Bueno",
        "fecha_ultimo_mantenimiento": "2025-02-20",
        "ubicacion_actual": "Aguascalientes",
        "nivel_combustible": 65,
        "estado_motor": "Óptimo",
        "horas_operacion": 3500
    }
    vehiculos.agregar_vehiculo(vehiculo)


    sensor = {
        "id_sensor": "S001",
        "id_vehiculo": "V001",
        "aceleracion": 1.2,
        "frenado": 0.3,
        "velocidad_actual": 80,
        "vibraciones": 0.02,
        "temperatura_motor": 90,
        "ubicacion_gps": "19.432608,-99.133209",
        "fecha_registro": "2025-02-28",
        "horas_motor": 100,
        "revolucionesxmin": 30,
    }
    sensores.agregar_sensor(sensor)

    conduccion = {
        "id_conduccion": "C001",
        "id_vehiculo": "V001",
        "nivel_agresividad": 2,
        "frecuencia_frenadas": 3,
        "fecha_registro": "2025-02-28",
        "patrones_conduccion": ["Aceleración suave", "frenado brusco"]
    }
    conducciones.agregar_conduccion(conduccion)

    mantenimiento= {
        "id_mantenimiento": "M001",
        "id_vehiculo": "V001",
        "tipo_mantenimiento": "Preventivo",
        "piezas_cambiadas": ["Filtro de aceite", "Llantas"],
        "piezas_que_cambiar": ["Filtro de aceite","P001", "2025-04-015"],
        "tiempo_estimado_reparacion": 4,
        "fecha_programada": "2025-04-015",
        "fecha_realizado": "2025-05-28",
        "alertas_fallas": "Sensor de oxígeno",
        "vida_util_piezas": 5000,
        "cambio_aceite": ["tipo","2025-05-28"],
        "desgaste_frenos": "intermedio",
        "historial_eventos": "se detecto ruido en las llantas"
    
    }
    mantenimientos.agregar_mantenimiento(mantenimiento)
    
    disponibilidad= {
        "id_camion": "C001",
        "fecha_mantenimiento": "2025-05-28",
        "salida": "2025-03-12 08:30:00",
        "ruta": "ruta norte",
        "tiempo_de_mantenimiento": "3 horas"
    }
    disponibilidades.agregar_disponibilidad(disponibilidad)



