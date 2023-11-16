import random


def generate_random_name(num_silabas):

    silabas = ['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du',
               'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu',
               'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu',
               'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
               'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu',
               'va', 've', 'vi', 'vo', 'vu', 'xa', 'xe', 'xi', 'xo', 'xu', 'za', 'ze', 'zi', 'zo', 'zu']


    nome = ''
    for _ in range(num_silabas):
        nome += random.choice(silabas)

    return nome
# Escolher o tamanho do nome, quantas silabas


desired_number_of_syllables = 2


randon_name = generate_random_name(desired_number_of_syllables)

print(randon_name)
