import json


class VacanciesDAO:
    def __init__(self, path):
        self.__path = path
        self.__vacancies_data = self.__load_data()

    def __load_data(self):
        with open(self.__path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self):
        return self.__vacancies_data

    def get_by_pk(self, pk):
        for vacancy in self.__vacancies_data:
            if vacancy["pk"] == pk:
                return vacancy

