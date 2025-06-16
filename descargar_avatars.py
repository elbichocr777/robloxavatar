import requests
import os

# Lista de IDs (ejemplo)
user_ids = [
    325015357, 1283729109, 215353863, 467193818,
    # ...agregá los que quieras
]

# Crear carpeta de salida
os.makedirs("avatars", exist_ok=True)

for user_id in user_ids:
    url = f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width=150&height=150&format=png"
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"avatars/{user_id}.png", "wb") as f:
            f.write(response.content)
        print(f"✅ Guardado: {user_id}.png")
    else:
        print(f"❌ Falló: {user_id}")
