import random
import json
import os

from generate_names import generate_random_name


def gerar_lista_nomes_pets():
    nome_pet = generate_random_name(3)
    return nome_pet


def gerar_json_aleatorio():
    status_opcoes = ['available', 'pending', 'sold']

    categorias = [
        {'id': 1, 'name': 'Cachorro'},
        {'id': 2, 'name': 'Gato'},
        {'id': 3, 'name': 'Peixe'},
        {'id': 4, 'name': 'Ave'},
        {'id': 5, 'name': 'Roedor'}
    ]
    category = random.choice(categorias)
    tags = [
        {'id': 1, 'name': 'vacinado'},
        {'id': 2, 'name': 'castrado'},
        {'id': 3, 'name': 'localizador'},
        {'id': 4, 'name': 'pedigree'}
    ]
    num_tags = random.randint(1, 4)
    selected_tags = random.sample(tags, num_tags)
    name = gerar_lista_nomes_pets()
    photo_urls = ['https://example.com/photo1.jpg', 'https://example.com/photo2.jpg']

    id_min_length = 5
    min_id = 10 ** (id_min_length - 1)
    max_id = (10 ** id_min_length) - 1
    id_aleatorio = random.randint(min_id, max_id)

    json_data = {
        'id': id_aleatorio,
        'category': category,
        'name': name,
        'photoUrls': photo_urls,
        'tags': selected_tags,
        'status': random.choice(status_opcoes)
    }

    return json_data


pasta = 'jsons'
if not os.path.exists(pasta):
    os.makedirs(pasta)

quantidade_jsons = 10

for i in range(quantidade_jsons):
    json_aleatorio = gerar_json_aleatorio()
    nome_arquivo = f'{pasta}/pet_{i + 1}.json'  # Nome do arquivo baseado no valor de i
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(json_aleatorio, arquivo, indent=4)
    print(f'JSON {i + 1} adicionado ao arquivo "{nome_arquivo}"')

print(f'{quantidade_jsons} JSONs adicionados aos arquivos individuais na pasta "{pasta}"')