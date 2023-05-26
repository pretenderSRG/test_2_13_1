import json


class CandidateDAO:
    """При створенні об'єкту потрібно вказати шлях"""
    def __init__(self, path):
        self.__path = path

    def __load_data(self):
        with open(self.__path, encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        return self.__load_data()

    def get_by_pk(self, pk):
        candidates = self.get_all()
        for candidate in candidates:
            if candidate["pk"] == pk:
                return candidate
