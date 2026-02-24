import requests

BASE_URL = "http://127.0.0.1:8000/api/productos/"

# 1️⃣ GET
def get_productos():
    response = requests.get(BASE_URL)
    print("GET Status:", response.status_code)
    print(response.json())

# 2️⃣ POST
def crear_producto():
    data = {
        "nombre": "Laptop Gamer",
        "precio": 25000.00,
        "stock": 10
    }
    response = requests.post(BASE_URL, json=data)
    print("POST Status:", response.status_code)
    print(response.json())
    return response.json()["id"]

# 3️⃣ PUT
def actualizar_producto_put(id):
    data = {
        "nombre": "Laptop Gamer Actualizada",
        "precio": 30000.00,
        "stock": 5
    }
    response = requests.put(f"{BASE_URL}{id}/", json=data)
    print("PUT Status:", response.status_code)
    print(response.json())

# 4️⃣ PATCH
def actualizar_producto_patch(id):
    data = {
        "stock": 2
    }
    response = requests.patch(f"{BASE_URL}{id}/", json=data)
    print("PATCH Status:", response.status_code)
    print(response.json())

# 5️⃣ DELETE
def eliminar_producto(id):
    response = requests.delete(f"{BASE_URL}{id}/")
    print("DELETE Status:", response.status_code)

if __name__ == "__main__":
    get_productos()
    producto_id = crear_producto()
    actualizar_producto_put(producto_id)
    actualizar_producto_patch(producto_id)
    eliminar_producto(producto_id)