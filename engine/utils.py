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

VECTORS = {
    "vec_a": [],
    "vec_b": [],
}

def get_vectors(type_:str):
    X = []
    Y = []
    _idx    = (lambda x: 2 if type_ == "numbers3" else 3)
    _models = NUMBERS3 if type_ == "numbers3" else NUMBERS4
    for _k, _v in enumerate(_models):
        Y.append(NUMBERS[_k][_idx(type_)])
        # print(_v.values())

def get_old_week(type_:str, old_week_:str=""):
    X = []
    Y = []
    _idx    = (lambda x: 2 if type_ == "numbers3" else 3)
    _models = NUMBERS3 if type_ == "numbers3" else NUMBERS4
    for _i in range(len(NUMBERS)):
        _t = NUMBERS[_i][0]
        _f = NUMBERS[_i][4]
        _y = NUMBERS[_i][_idx(type_)]
        _x = _models[_i][_t][4]
        if len(old_week_) > 0:
            if old_week_ == NUMBERS[_i][4]:
                Y.append(NUMBERS[_i][0])
                X.append(NUMBERS[_i][_idx(type_)])
        else:
            Y.append(_y)
            X.append(_x)
        # if len(list(set(_y) & set(_x))) >= 2:
        #     print(_t, _f, _y, _x)
    return Y, X

def predict2(type_:str):
    pass


def proc(type_:str, vector_:str):
    """
    :method proc - 加工する
    :param type_
    """
    X = []
    Y = []
    _idx = (lambda x: 2 if type_ == "numbers3" else 3)
    _models = NUMBERS3 if type_ == "numbers3" else NUMBERS4
    # for _k, _v in enumerate(_models):
    #     if vector_ is "vec_a":
    #         X.append(_v[NUMBERS[_k][0]])
    #     elif vector_ is "vec_b":
    #         _b, _c = get_old_week(type_, "")
    #         X.append(_c)
    #     Y.append(NUMBERS[_k][_idx(type_)])
    _b, _c = get_old_week(type_)

    # _x = pd.DataFrame(X)
    # _y = pd.DataFrame(Y)
    _x = pd.DataFrame(_c)
    _y = pd.DataFrame(_b)

    return (_y, _x)


def predict(type_:str):
    """
    :method predict - 予測する
    :param type_
    """
    from sklearn import linear_model

    y, x = proc(type_, "vec_b")

    _model = linear_model.LinearRegression()
    _model.fit(x, y)
    
    _px = x
    _py = _model.predict(_px)

    # for _i in range(len(_py)):
    #     print("第{0}回 {1} {2}".format(NUMBERS[_i][0], round(_py[_i][0], 0), y[_i]))
    return (_model, _py)

def check(type_:str):
    _y, _x = proc(type_, "vec_b")
    _, _py = predict(type_)

    for _i in range(len(_y)):
        _true = _y[_i]
        _pred = str(int(round(_py[_i][0])))

        _true_list = list(_true)
        _pred_list = list(_pred)
        s = difflib.SequenceMatcher(None, _true, _pred).ratio()
    
    # print(_y, _py)


def predict_number(type_:str, vec_:list, file_:str):
    """
    """
    _model, _py = predict(type_)
    _vectors = []
    for _i in range(len(vec_)):
        _num = float(vec_[_i])
        _vectors.append(_num)

    joblib.dump(_model, "numbers3.pkl")
    _clf = joblib.load("numbers3.pkl")

    print("aaaaaaaaaaaa")
    print(_clf)

    _clf.predict([_vectors])


def get_info(year_:str, six_week_:str, type_:str):
    """
    """
    _idx = (lambda x: 2 if type_ == "numbers3" else 3)
    for _i in range(len(NUMBERS)):
        if six_week_ == NUMBERS[_i][4]:
            if re.search(year_, NUMBERS[_i][1]):
                print(NUMBERS[_i][0], NUMBERS[_i][_idx(type_)])


def main():
    pass

if __name__ == '__main__':
    # 2015 仏滅サイドスクリプト
    get_info("2014", "友引", "numbers4")

    # print(predict("numbers3"))
    WEEK = ["赤口", "友引", "仏滅", "先負", "先勝", "大安"]

    # predict("numbers3")
    # predict("numbers3")
    data = ["535", "496", "604", "299", "531", "909"] # 4929

    # predict_num = predict_number("numbers3", data, "20180527_numbers3.pkl")
    # print(predict_num)

    # for _x in WEEK:
    # get_old_week("numbers3", "大安")
    # get_vectors("numbers3")


    
