# -*- coding: utf-8 -*-
"""
Чтение данных о студентах из YAML-файла.
"""
import yaml
from Types import DataType
from DataReader import DataReader  # проверь путь к DataReader


class YamlDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f)

        if not isinstance(raw, dict):
            raise ValueError("Неверный формат YAML:"
                             "требуется словарь студентов.")

        result: DataType = {}
        for student, subjects in raw.items():
            if not isinstance(subjects, dict):
                raise ValueError(f"Неверные данные по студенту {student}")
            pairs: list[tuple[str, int]] = []
            for subj, score in subjects.items():
                if not isinstance(score, int):
                    raise ValueError(f"Баллы по {subj} у {student} должны"
                                     " быть целыми.")
                pairs.append((subj, score))
            result[student] = pairs
        return result
