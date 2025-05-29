from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["yovoybd"]
sensores = db["sensores"]

def agregar_sensor(sensor):
    sensores.insert_one(sensor)
    print("El sensor fue agregado.")

def leer_sensor(id_sensor):
    return sensores.find_one({"id_sensor": id_sensor})

def actualizar_sensor(id_sensor, actualizacion):
    sensores.update_one({"id_sensor": id_sensor}, {"$set": actualizacion})
    print("El sensor fue actualizado.")

def eliminar_sensor(id_sensor):
    sensores.delete_one({"id_sensor": id_sensor})
    print("El sensor fue eliminado.")

if __name__ == "__main__":
    sensor = {
        "id_sensor": "S001",
        "id_vehiculo": "V001",
        "aceleracion": 1.2,
        "frenado": 0.3,
        "velocidad_actual": 80,
        "vibraciones": 0.02,
        "temperatura_motor": 90,
        "ubicacion_gps": "19.432608,-99.133209",
        "fecha_registro": "2025-02-28T21:00:00",
        "horas_motor": 100,
        "revolucionesxmin": 30
    }
    agregar_sensor(sensor)
