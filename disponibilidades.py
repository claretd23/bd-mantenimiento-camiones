from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["yovoybd"]
disponibilidades = db["disponibilidad"]

def agregar_disponibilidad(disponibilidad):
    disponibilidades.insert_one(disponibilidad)
    print("La disponibilidad fue agregada.")

def leer_mantenimiento(id_disponibilidad):
    return disponibilidades.find_one({"id_mantenimiento": id_disponibilidad})

def actualizar_mantenimiento(id_disponibilidad, actualizacion):
    disponibilidades.update_one({"id_disponibilidad": id_disponibilidad}, {"$set": actualizacion})
    print("La disponibilidad fue actualizada.")

def eliminar_mantenimiento(id_disponibilidad):
    disponibilidades.delete_one({"id_disponibilidad": id_disponibilidad})
    print("La disponibilidad fue eliminada.")

if __name__ == "__main__":
    disponibilidad= {
        "id_camion": "C001",
        "fecha_mantenimiento": "2025-05-28",
        "salida": "2025-03-12 08:30:00",
        "ruta": "ruta norte",
        "tiempo_de_mantenimiento": "3"
    }
    agregar_disponibilidad(disponibilidad)
