
let lot_numbers3_lists = @["085", "933", "394", "236", "219",
                           "021", "227", "420", "071", "252", 
                           "921", "072", "830", "205", "023",
                           "046", "501", "221", "996", "496",
                           "714", "836", "621", "732", "523",
                           "385", "754", "434", "891", "176",
                           "609", "794", "177", "173", "261",
                           "782", "820", "242", "945", "233",
                           "218", "618", "937", "278", "276",
                           "043", "078", "542", "325", "162",
                           "351", "663", "288", "720", "809",
                           "372", "591", "842", "858", "384",
                           "976", "930", "634", "223", "413",
                           "881", "368", "873", "916", "955",
                           "122", "327", "092", "282", "956",
                           "415", "432", "437", "546", "291",
                           "461", "139", "138", "448", "936",
                           "221", "876", "347", "631", "725",
                           "949", "271", "545", "320", "060",
                           "060", "350", "839", "382", "776",
                           "411", "586", "045", "123", "720",
                           "497", "243", "363", "236", "399",
                           "217", "118", "486", "029", "900",
                           "484", "905", "800"]

=> "339"


  # ?          # 029      # 236      # 123      # 382        # 320      # 631      # 448      # 546       # 282
 0 -> xxxxxx  0 ->       0 -> xx    0 -> x     0 -> xxxxx   0 ->       0 ->       0 ->        0 -> x     0 -> x
 1 ->         1 -> xxx   1 -> x     1 -> xx    1 -> xxx     1 -> xx    1 -> xx    1 -> xxxx   1 -> x     1 -> xx
 2 -> x       2 -> xx    2 -> xxx   2 -> x     2 -> x       2 -> xx    2 -> xx    2 -> x      2 -> xxxx  2 -> xxxx 
 3 ->         3 -> xxxx  3 -> xxxx  3 -> xx    3 -> xx      3 -> xx    3 -> xxx   3 -> xxx    3 -> xx    3 -> xx
 4 -> xxx     4 -> xx    4 -> xxx   4 -> xx    4 -> x       4 -> xx    4 -> xxx   4 -> xxx    4 -> xxx   4 ->  
 5 -> x       5 ->       5 -> x     5 -> xx    5 -> xxx     5 -> xxx   5 ->       5 -> x      5 -> x     5 -> xx 
 6 -> x       6 -> x     6 -> x     6 -> x     6 -> xx      6 -> x     6 -> x     6 -> xx     6 -> x     6 -> x 
 7 ->         7 -> x     7 -> xx    7 -> xx    7 ->         7 -> xxx   7 -> xxx   7 -> x      7 -> x     7 -> xx 
 8 -> xxx     8 -> xx    8 ->       8 -> xxx   8 -> x       8 ->       8 ->       8 -> x      8 -> x     8 -> x 
 9 -> xxx     9 -> xx    9 -> x     9 -> x     9 -> x       9 -> xx    9 -> xx    9 -> x      9 -> x     9 -> xx 

 - 0n ->
 - 1n ->
 - 2n ->
 - 3n ->
 - 4n ->

 [0, 1, ,2 ,3, 4]
 - 0個が焦点
 -

# 4884 教訓
 - 5個の数字あって、4個数字もあると、4個の数字は選択される
 - 0個の数字が一個のみ時は、0個の数字は選択されないが
 - 0個の数字が複数ある場合は、0個の数字も選択される
 - 4個の数字が複数存在していても、選択される保証はない
 - パターン個数を選択されるが、桁も一致するとは限らない

 # 4885 教訓
 - 5個の数字あって、4個数字もあると、4個の数字は選択される
 - 0個の数字が一個のみ時は、0個の数字は選択されないが
 - 0個の数字が複数ある場合は、0個の数字も選択される
 - 4個の数字が複数存在していても、選択される保証はない
 - パターン個数を選択されるが、桁も一致するとは限らない

 # 4886
 ### 092
 - 0個の数字が複数ある場合は、1つは選択される
 - 1個の数字が1つのみの時は選択れない
 ### 437
 - 同じ個数の数字が7つある場合、その中から2つ選択される
 ### 138
 - 0個が2つある場合、どれかは選択される
 - 3個の数字、2個の数字、1個の数字の個数が同じ場合、どれかが２つとも選択される可能性がある
   (4個の数字がある場合)
 ### 347
 - 3個の数字、2個の数字、1個の数字の個数が同じ場合、その中の２つ選択される可能性がある
   (4個の数字がない場合)
 - 0個の数字が複数ある場合、1つは選択される
 ### 545
 - 0個の数字が複数存在しても、選択されない可能性がある
   (確率は低い)
 - 4個の数字があっても3個の数字がない場合、どちらも選択されない
 ### 839
 - 極端に個数が多い数字は選択されない可能性がある
 - 2個の数字が3つと1個の数字が３つ同じ場合、2個の数字が選択される可能性がある
 - 0個の数字が複数存在してても、その中の1つ選択というより２つとも選択される可能性はある
 ### 045
 - 0個の数字が一切なく、同じ個数の数字が5個ある場合、その中から2つ選択される可能性がある
 ### 363
 - 0個の数字が1つだけでも選択される可能性はある
 ### 486
 - 0個の数字が複数存在しても、選択されない可能性がある
 - 1個の数字が4つある場合、３つとも選択される可能性がある
   が、同じ数字が選択されるわけではない