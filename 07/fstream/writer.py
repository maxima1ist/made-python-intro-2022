import csv
import json


class BaseWriter:
    def dump(self, fileobj, data):
        pass


class TxtWriter(BaseWriter):
    def dump(self, fileobj, data):
        fileobj.writelines('\n'.join(data))


class JsonWriter(BaseWriter):
    def dump(self, fileobj, data):
        fileobj.write(json.dumps(data))


class CSVWriter(BaseWriter):
    def dump(self, fileobj, data):
        csv_writer = csv.writer(fileobj)
        for line_values in data:
            csv_writer.writerow(line_values)
