import csv
import json


class BaseReader:
    def read(self, fileobj):
        return None


class TxtReader(BaseReader):
    def read(self, fileobj):
        return [line for line in fileobj.read().splitlines()]


class JsonReader(BaseReader):
    def read(self, fileobj):
        return json.load(fileobj)


class CSVReader(BaseReader):
    def read(self, fileobj):
        csv_reader = csv.reader(fileobj)
        return [line_values for line_values in csv_reader]
