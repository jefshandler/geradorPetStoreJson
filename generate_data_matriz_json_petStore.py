import random
import json
import os


from generate_names import generate_random_name


def gerar_lista_nomes_pets():
    name_pet = generate_random_name(3)
    return name_pet


def gerar_json_aleatorio():
    status_opcoes = [
        'available',
        'pending',
        'sold'
    ]
    status = random.choice(status_opcoes)

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
    # Define a quantidade de digitos para o Id do pet
    id_min_length = 5
    min_id = 10 ** (id_min_length - 1)
    max_id = (10 ** id_min_length) - 1
    json_data = {
        'id': random.randint(min_id, max_id),
        'category': category,
        'name': name,
        'photoUrls': photo_urls,
        'tags': selected_tags,
        'status': status
    }

    return json_data


def main():
    pasta = 'jsons'
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    while True:
        try:
            quantidade_jsons = int(input("Digite a quantidade de JSONs a serem gerados na matriz (número positivo): "))
            if quantidade_jsons > 0:
                break
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Por favor, digite um número válido.")

    jsons_aleatorios = []

    for i in range(quantidade_jsons):
        json_aleatorio = gerar_json_aleatorio()
        jsons_aleatorios.append(json_aleatorio)

    # Salvar a lista de JSONs no arquivo
    nome_arquivo = f'{pasta}/jsons_matriz.json'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(jsons_aleatorios, arquivo, indent=4)

    print(f'{quantidade_jsons} JSONs adicionados ao arquivo "{nome_arquivo}"')


if __name__ == "__main__":
    main()
