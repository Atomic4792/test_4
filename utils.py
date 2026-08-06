import json
import os
import requests
from dotenv import load_dotenv
from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    Abstract base class defining the interface for any data source that
    can supply a list of commands.
    """

    @abstractmethod
    def parse_file(self) -> list:
        """
        Parses a file and returns its contents as a Python list of commands.
        """
        pass


class TextDataSource(DataSource):
    """
    Reads commands from a plain text file, parsing one command per line.
    """

    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def parse_file(self) -> list:
        """
        Reads the text file line by line, strips trailing whitespace,
        and appends each parsed line into a list which is then returned.
        """
        data = []
        with open(self.file_name) as file:
            for line in file:
                line = line.strip()
                data.append(line)
        return data


class JsonDataSource(DataSource):
    """
    Reads commands from a JSON file and extracts its values.
    """

    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def parse_file(self) -> list:
        """
        Loads the JSON file and extracts all values from
        dictionary, returning them as a list of commands.
        """
        data = []
        with open(self.file_name, "r") as file:
            file = json.load(file)
            for value in file.values():
                data.append(value)

        return data


class APIDataSource(DataSource):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        load_dotenv()

    def parse_file(self) -> list:
        data = []
        headers = {"Authorization": f"Bearer {os.getenv("BEARER_TOKEN")}"}
        r = requests.get(self.file_name, headers= headers)
        response_obj = json.loads(r.text)
        for value in response_obj.values():
            data.append(value)

        return data
