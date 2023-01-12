# -*- coding: utf-8 -*-
from src.Types import DataType
from src.TopStudent import TopStudent
import pytest

RatingsType = int


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 20),
                    ("русский язык", 35),
                    ("программирование", 91)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 92),
                    ("русский язык", 92),
                    ("программирование", 92),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = "Петров Игорь Владимирович"

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating =TopStudent(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = TopStudent(input_data[0]).calc()
        assert rating == input_data[1]