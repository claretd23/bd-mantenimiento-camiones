from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["yovoybd"]
vehiculos = db["vehiculos"]

def agregar_vehiculo(vehiculo):
    vehiculos.insert_one(vehiculo)
    print("El vehículo fue agregado.")

def leer_vehiculo(id_vehiculo):
    return vehiculos.find_one({"id_vehiculo": id_vehiculo})

def actualizar_vehiculo(id_vehiculo, actualizacion):
    vehiculos.update_one({"id_vehiculo": id_vehiculo}, {"$set": actualizacion})
    print("El vehículo se actualizo")

def eliminar_vehiculo(id_vehiculo):
    vehiculos.delete_one({"id_vehiculo": id_vehiculo})
    print("El vehículo fue eliminado.")

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
    agregar_vehiculo(vehiculo)
