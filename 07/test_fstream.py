import unittest

from fstream.reader import BaseReader, TxtReader, JsonReader, CSVReader
from fstream.writer import BaseWriter, TxtWriter, JsonWriter, CSVWriter


class FstreamTest(unittest.TestCase):
    @staticmethod
    def read_data(fileobj, reader: BaseReader):
        return reader.read(fileobj)

    @staticmethod
    def dump_data(data, fileobj, writer: BaseWriter):
        writer.dump(fileobj, data)

    def test_txt(self):
        data = ["Load up on guns", "and bring your friend.",
                "It's fun to lose", "and to pretend."]
        with open("file.txt", "w", encoding="utf-8") as fout:
            FstreamTest.dump_data(data, fout, writer=TxtWriter())

        with open("file.txt", "r", encoding="utf-8") as fin:
            readed_data = FstreamTest.read_data(fin, reader=TxtReader())
        self.assertEqual(readed_data, data)

    def test_json(self):
        data = {"x": "1"}
        with open("file.json", "w", encoding="utf-8") as fout:
            FstreamTest.dump_data(data, fout, writer=JsonWriter())

        with open("file.json", "r", encoding="utf-8") as fin:
            readed_data = FstreamTest.read_data(fin, reader=JsonReader())
        self.assertEqual(readed_data, data)

    def test_csv(self):
        data = [["name", "surname", "age"],
                ["Maxim", "Stepura", "22"],
                ["Maria", "Zhuravleva", "20"]]
        with open("file.csv", "w", encoding="utf-8") as fout:
            FstreamTest.dump_data(data, fout, writer=CSVWriter())

        with open("file.csv", "r", encoding="utf-8") as fin:
            readed_data = FstreamTest.read_data(fin, reader=CSVReader())
        self.assertEqual(readed_data, data)


if __name__ == "__main__":
    unittest.main()
