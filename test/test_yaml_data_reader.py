# -*- coding: utf-8 -*-
import tempfile
import os
import yaml
import pytest
from yaml_data_reader import YamlDataReader


def test_read_valid_yaml():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml",
                                      mode="w", encoding="utf-8")
    yaml.dump({"Иванов Иван Иванович": {"математика": 95,
                                        "литература": 90}}, tmp)
    tmp.close()

    reader = YamlDataReader()
    data = reader.read(tmp.name)

    assert "Иванов Иван Иванович" in data
    assert ("математика", 95) in data["Иванов Иван Иванович"]
    assert isinstance(data, dict)
    os.remove(tmp.name)


def test_read_invalid_yaml_not_dict():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml",
                                      mode="w", encoding="utf-8")
    tmp.write("- just a list")
    tmp.close()

    reader = YamlDataReader()
    with pytest.raises(ValueError):
        reader.read(tmp.name)
    os.remove(tmp.name)


def test_read_invalid_score_type():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml",
                                      mode="w", encoding="utf-8")
    yaml.dump({"Иванов": {"математика": "отлично"}}, tmp)
    tmp.close()

    reader = YamlDataReader()
    with pytest.raises(ValueError):
        reader.read(tmp.name)
    os.remove(tmp.name)
