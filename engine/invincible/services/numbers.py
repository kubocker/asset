# -*- coding: utf-8 -*-

# from models import numbers, numbers3, numbers4


__all__ = [
    "Numbers3",
    "Numbers4"
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

__all__ = [
    "Numbers3",
    "Numbers4",
]


class Numbers(object):

    vectors = {
        "keys_a": ["day1", "day2", "week1", "week2", "cal1", "cal2"]
    }

    def __init__(self, time_:str):
        self._day_1  = str(int(time_) - 1)
        self._day_2  = str(int(time_) - 2)
        self._week_1 = str(int(time_) - 5)
        self._week_2 = str(int(time_) - 6)
        # self._cal_1  = self._check_calender()[0]
        # self._cal_2  = self._check_calender()[1]
        self._old_1  = None
        self._time = time_

    def __call__(self, type_:str) -> list:
        self._setup(type_)

    
    def _setup(self, type_:str):

        _last = int(self._time)
        _next = int(self._time)
        if not self._time in []:
            # @TODO:
            _last = self.models[0]

        if _next != _last+1:
            return
        return []


    def _check_calender(self):
        _cal = ["赤口", "先勝", "友引", "先負", "仏滅", "大安"]
        _list = None
        return []

    @property
    def week(self):
        pass

    @property
    def old_week(self):
        pass
        
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


class Numbers3(Numbers):
    pass


class Numbers4(Numbers):
    pass