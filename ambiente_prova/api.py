from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'
    
    @property
    def URL(self):
        return self.__URL


    def extract(self, id):
        try:
            URL = self.URL + str(id)
            response = requests.get(URL)
            response.raise_for_status()
            dado = response.json()
            return (dado.get('id'), dado.get('name'), dado.get('species'))
        except requests.exceptions.RequestException as e:
            return f"Erro ao acessar API Rick and Morty: {e}"

class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        try:
            URL = self.URL + str(id)
            response = requests.get(URL)
            response.raise_for_status()
            dado = response.json()
            return (dado.get('name'), dado.get('films'))
        except requests.exceptions.RequestException as e:
            return f"Erro ao acessar API Star Wars: {e}"


class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        try:
            URL = self.URL + str(id)
            response = requests.get(URL)
            response.raise_for_status()
            dado = response.json()
            return (dado.get('name'), dado.get('tvSeries'))
        except requests.exceptions.RequestException as e:
            return f"Erro ao acessar API Ice and Fire: {e}"

