import requests
from bs4 import BeautifulSoup


def wether(place):
    url = f'https://www.google.com/search?&q=weather in {place}'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    temperature = s.find('div', class_='BNeawe').text

    return temperature


def verify(string):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if string[0] in numbers:
        print(f'Current temperature in ({place}): {string}')
    else:
        print('Something is wrong. Try again later.')


if __name__ == '__main__':
    place = input('Place: ')
    verify(wether(place))
