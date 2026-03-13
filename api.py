import requests
from PIL import Image
from io import BytesIO
response = requests.get("https://rickandmortyapi.com/api/character")
data=response.json()
busca=input("Digite o nome do personagem: ").lower()
encontrou=False
for character in data["results"]:
    if busca in character["name"].lower():
        print(f"Nome: {character['name']}")
        print(f"Status: {character['status']}")
        print(f"Espécie: {character['species']}")
        print(f"Gênero: {character['gender']}")
        print(f"Origem: {character['origin']['name']}")
        print(f"Localização: {character['location']['name']}")
        print("----------------------------------------------------------------------------------------------------------")
        encontrou=True
        image_url = character['image']
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image.show()
if not encontrou:
    print("Personagem não encontrado.")



    