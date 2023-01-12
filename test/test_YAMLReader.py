# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YAMLReader import TextDataReaderYAML


class TestTextDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "- Иванов Иван Иванович:\n" + \
                "    - математика: 20\n" +\
                "    - литература: 35\n" +\
                "    - программирование: 91\n" +\
                "- Петров Петр Петрович:\n" +\
                "    - математика: 92\n" +\
                "    - химия: 92\n" +\
                "    - социология: 92\n"

        data = {
            "Иванов Иван Иванович": [
                ("математика", 20),
                ("литература", 35),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 92),
                ("химия", 92),
                ("социология", 92)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = TextDataReaderYAML().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]