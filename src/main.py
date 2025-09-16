# -*- coding: utf-8 -*-
import argparse
import sys

# from CalcRating import CalcRating
# from TextDataReader import TextDataReader
from student_analyzer import StudentAnalyzer
from yaml_data_reader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = YamlDataReader()
    students = reader.read(path)
    print("Студенты: ", students)

    count = StudentAnalyzer(students).count_excellent_students()
    print("Количество отличников: ", count)


if __name__ == "__main__":
    main()
