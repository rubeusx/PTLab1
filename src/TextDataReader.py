# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader


class TextDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.rstrip()
                if not line:
                    continue  # пропустить пустые строки

                if line == line.lstrip():
                    # Имя студента (без отступа)
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    # Предмет и оценка (с отступом)
                    if self.key:  # защита от отсутствия ключа
                        try:
                            subj, score = line.strip().split(":", maxsplit=1)
                            self.students[self.key].append((subj.strip(), int(score.strip())))
                        except ValueError:
                            print(f"Ошибка в строке: {line.strip()}")
        return self.students
