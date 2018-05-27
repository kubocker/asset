#! -*- coding: utf-8 -*-

import sys
import re
import difflib
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import (mean_absolute_error,
                             mean_squared_error,
                             r2_score)
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from config import NUMBERS, NUMBERS3, NUMBERS4
from invincible import services as g


"""
~ NUMBERS3 ~
2016 - 大安 x
2016 - 仏滅 x
2016 - 赤口 x
2016 - 先負 x
2016 - 先勝 x
2016 - 友引 x

2015 - 大安
2015 - 仏滅
2015 - 赤口
2015 - 先負
2015 - 先勝
2015 - 友引

2014 - 大安
2014 - 仏滅
2014 - 赤口
2014 - 先負
2014 - 先勝
2014 - 友引

~ NUMBERS4 ~
2017 - 大安
2017 - 仏滅
2017 - 赤口
2017 - 先負
2017 - 先勝
2017 - 友引

2016 - 大安
2016 - 仏滅
2016 - 赤口
2016 - 先負
2016 - 先勝
2016 - 友引

2015 - 大安
2015 - 仏滅
2015 - 赤口
2015 - 先負
2015 - 先勝
2015 - 友引

2014 - 大安
2014 - 仏滅
2014 - 赤口
2014 - 先負
2014 - 先勝
2014 - 友引
"""

__all__ = [
    "predict",
    "predict_number",
    "get_info"
]

def predict(type_:str):
    X = []
    Y = []
    models = NUMBERS3 if type_ == "numbers3" else NUMBERS4
    for _k, _v in enumerate(models):
        _idx = (lambda x: 2 if type_ == "numbers3" else 3)
        Y.append(NUMBERS[_k][_idx(type_)])
        X.append(_v[NUMBERS[_k][0]])

    _model = linear_model.LinearRegression()
    _x = pd.DataFrame(X)
    _y = pd.DataFrame(Y)

    _model.fit(_x, _y)
    
    _px = _x
    _py = _model.predict(_px)

    return (_model, _py)


def predict_number(type_:str, vec_:list, file_:str):
    _model, _py = predict(type_)
    _vectors = []
    for _i in range(len(vec_)):
        _num = float(vec_[_i])
        _vectors.append(_num)

    joblib.dump(_model, file_)
    _clf = joblib.load(file_)

    return _clf.predict([_vectors])


def get_info(year_:str, six_week_:str, type_:str):
    _idx = (lambda x: 2 if type_ == "numbers3" else 3)
    for _i in range(len(NUMBERS)):
        if six_week_ == NUMBERS[_i][4]:
            if re.search(year_, NUMBERS[_i][1]):
                print(NUMBERS[_i][0], NUMBERS[_i][_idx(type_)])


def main():
    pass

if __name__ == '__main__':
    get_info("2014", "大安", "numbers3")