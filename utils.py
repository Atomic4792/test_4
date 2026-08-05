import json
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def parse_file(self) -> list:
        """parse file_name into a python list"""
        pass


class TextDataSource(DataSource):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def parse_file(self) -> list:
        data = []
        with open(self.file_name) as file:
            for line in file:
                line = line.strip()
                data.append(line)
        return data

class JsonDataSource(DataSource):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def parse_file(self) -> list:
        data = []
        with open(self.file_name, "r") as file:
            file = json.load(file)
            for value in file.values():
                data.append(value)

        return data
