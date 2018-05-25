#! -*- coding: utf-8 -*-

import sys
import re

from config import NUMBERS, NUMBERS3, NUMBERS4


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


def main():
    for _i in range(len(NUMBERS)):
        if "" == NUMBERS[_i][4]:
            if re.search("2016", NUMBERS[_i][1]):
                print(NUMBERS[_i][3])
            pass

    
if __name__ == '__main__':
    main()