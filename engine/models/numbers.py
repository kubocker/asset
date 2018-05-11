# -*- coding: utf-8 -*-


__all__ = [
    "Numbers",
    "Loto"
]

"""
ex.
numbers = Numbers("4917")
numbers(3)
   => ("y", ["x"])
    x: [前日, 前々日, 先週, 先々週, 六曜前回, 六曜前々回, 旧暦] => ["037", "909", "589", "355", "119", "118", "936", ""]
    ※任意の旧暦日で当選がおこなれてない場合は、旧暦の旧暦を確認する
    or 旧暦がないバージョン
or
numbers.predict("3")
"""


class Numbers(object):

    vectors = {
        "keys": ["day1", "day2", "week1", "week2", "cal1", "cal2"]
    }

    def __init__(self, time_:str):
        self._day_1  = str(int(time_) - 1)
        self._day_2  = str(int(time_) - 2)
        self._week_1 = str(int(time_) - 5)
        self._week_2 = str(int(time_) - 6)
        self._cal_1  = self._check_calender()[0]
        self._cal_2  = self._check_calender()[1]
        self._old_1  = None

    def __call__(self, type_:str) -> list:
        self.all()

    def _check_calender(self):
        _cal = ["赤口", "先勝", "友引", "先負", "仏滅", "大安"]
        _list = None
        return []

    @property
    def times(self):
        return [self._day_1,
                self._day_2,
                self._week_1,
                self._week_2,
                self._cal_1,
                self._cal_2] # , self._old_1

    def all(self):
        _times = self.times
        return []

    def predict(self, type_: str):
        return 0

    def update(self):
        pass




class Loto(object):

    def __init__(self, no_:str):
        pass

    def __call__(self, type_:str) -> tuple:
        pass

    def update(self):
        pass