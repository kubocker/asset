# code: utf8

## 前回:18個, 前々回:28個, 前回曜日:27個, 前々回曜日:18個, 前回六曜:23個, 前々回六曜:20個

VECTOR_NUMBERS3 = [
    { "name": "赤口", "type": "+", "vectors": [0, 2, 3] },
    { "name": "赤口", "type": "-", "vectors": [1, 4, 5] },
    { "name": "友引", "type": "+", "vectors": [0, 2, 5] },
    { "name": "友引", "type": "-", "vectors": [1, 3, 4] },
    { "name": "先勝", "type": "+", "vectors": [1, 2, 4] },
    { "name": "先勝", "type": "-", "vectors": [0, 3, 5] },
    { "name": "先負", "type": "+", "vectors": [1, 2, 4] },
    { "name": "先負", "type": "-", "vectors": [0, 3, 5] },
    { "name": "仏滅", "type": "+", "vectors": [1, 3, 5] },
    { "name": "仏滅", "type": "-", "vectors": [0, 2, 4] },
    { "name": "大安", "type": "+", "vectors": [1, 3, 5] },
    { "name": "大安", "type": "-", "vectors": [0, 2, 4] },
]

PATTERN_NUMBERS3 = [
    #### +
    { "name": "pattern1", "type": "+", "patterns": [3, 3] },
    { "name": "pattern2", "type": "+", "patterns": [3, 2] },
    { "name": "pattern3", "type": "+", "patterns": [2, 3] },
    { "name": "pattern4", "type": "+", "patterns": [2, 2] },
    { "name": "pattern5", "type": "+", "patterns": [2, 1] },
    { "name": "pattern6", "type": "+", "patterns": [1, 2] },
    { "name": "pattern7", "type": "+", "patterns": [1, 1] },

    ### -
    { "name": "pattern1", "type": "-", "patterns": [3, 3] },
    { "name": "pattern2", "type": "-", "patterns": [3, 2] },
    { "name": "pattern3", "type": "-", "patterns": [2, 3] },
    { "name": "pattern4", "type": "-", "patterns": [2, 2] },
    { "name": "pattern5", "type": "-", "patterns": [2, 1] },
    { "name": "pattern6", "type": "-", "patterns": [1, 2] },
    { "name": "pattern7", "type": "-", "patterns": [1, 1] },
]