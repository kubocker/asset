# File: main.nim

import random
import future
import algorithm,tables,hashes,math
import sets,lists,critbits,sequtils,queues,intsets,strutils

randomize()


let lot_numbers3_lists = @["187", "925", "085", "933", "394", "236", "219", "021", "227", "420",
                           "071", "252", "921", "072", "830", "205", "023", "046", "501", "221",
                           "996", "496", "714", "836", "621", "732", "523", "385", "754", "434",
                           "891", "176", "609", "794", "177", "173", "261", "782", "820", "242",
                           "945", "233", "218", "618", "937", "278", "276", "043", "078", "542",
                           "325", "162", "351", "663", "288", "720", "809", "372", "591", "842",
                           "858", "384", "976", "930", "634", "223", "413", "881", "368", "873",
                           "916", "955", "122", "327", "092", "282", "956", "415", "432", "437",
                           "546", "291", "461", "139", "138", "448", "936", "221", "876", "347",
                           "631", "725", "949", "271", "545", "320", "060", "060", "350", "839",  # ~第4866回 2018/02/28
                           "382", "776", "411", "586"]
let youtube = @["58", "85", "86", "68", "56", "65",
                "41", "14", "11",
                "77", "76", "67",
                "38", "83", "82", "28", "32", "23",
                "83", "38", "39", "93", "89", "98",
                "35", "53", "50", "05", "30", "03"]


echo "################################################################"
for i in youtube:
  echo random(max=9).intToStr & i

let data1: string = """
1. 
2. 
3. 
4. 
5. 
"""


echo "################################################################"
# for i in yo utube:
#   echo i & random(max=9).intToStr

let data2: string = """
1. 
2. 
3. 
4. 
5. 
"""

########################################################################
# 
# 
# 
# 
#
# 
# 
# 
#
#
#
#########################################################################

let memo: string = """
# 4870 (586)
# 4869 (411)
41 -> 413, 415
14 -> 714
11 -> 411

# 4868 (776)
77 -> 177
76 -> 176, 276, 976, 876
67 -> 

# 4867 (382)
38 -> 385, 384, 138
83 -> 830, 836, 839
82 -> 782, 820, 282
32 -> 732, 325, 327, 432, 320 
23 -> 236, 023, 233, 223

# 4866 (839)
83 -> 830, 836, 839
38 -> 385, 384, 138
39 -> 839
93 -> 394, 139, 936
89 -> 891
98 ->

# 4865 (350)
35 -> 351
53 ->
50 -> 501
05 -> 205
30 -> 830, 930
03 -> 
"""


# URL: http://nmbrs.blog.fc2.com
# 第4869回
let predict_lot_numbers_list = @["021", "028", "031", "032", "038",
                                 "081", "361", "362", "368", "501",
                                 "502", "503", "508", "536", "561",
                                 "562", "568", "621", "628", "681",
                                 "721", "728", "731", "732", "738",
                                 "751", "752", "753", "758", "781",
                                 "901", "902", "903", "908", "936",
                                 "950", "956", "961", "962", "968",
                                 "971", "972", "973", "975", "978"]

block:
  var ary = lot_numbers3_lists
  var y = lc[x | (x <- ary), string]
  echo y
  echo y.len

echo "5 x 5 回まわし判断する"
block:
  randomize()
  for num in 1..5:
    echo random(predict_lot_numbers_list)
# 1. 902 753 621 753 721
# 2. 968 501 362 752 038
# 3. 973 361 758 028 362
# 4. 361 751 362 753 721
# 5. 950 361 561 536 751

let predicts =  @["902", "753", "621", "753", "721",
                  "968", "501", "362", "752", "038",
                  "973", "361", "758", "028", "362",
                  "361", "751", "362", "753", "721",
                  "950", "361", "561", "536", "751"]
echo predicts
let facebook: string = """
753, 751, 752,
536, 561,
361, 362
973, 968, 950
"""




let lot_numbers4_lists = @["5859", "7920", "2699", "8061", "6856", "6708", "6863", "7187", "4615", "6897",
                           "6135", "5359", "3309", "6341", "6701", "9542", "4924", "3880", "1343", "3185",
                           "2533", "7893", "8560", "2114", "6351", "4700", "9033", "5808", "5360", "5863",
                           "8642", "9840", "3598", "9182", "7288", "9698", "6229", "0740", "6287", "9035",
                           "1556", "2348", "4974", "4991", "0382", "3627", "8528", "1920", "8835", "6907",
                           "0991", "8318", "8333", "9436", "0587", "8894", "6933", "4543", "9664", "7789",
                           "5319", "6489", "5346", "9751", "1523", "5820", "7751", "6605", "5564", "3506",
                           "6610", "3027", "3146", "0341", "6443", "0517", "8334", "9016", "4945", "4148",
                           "7163", "8905", "2859", "2666", "2864", "2657", "9600", "9246", "1509", "6647",
                           "3275", "1540", "5550", "4687", "8987", "2979", "0757", "5510", "7336", "0626", # ~第4866回 2018/02/28
                           "5061", "1107", "6976"]


# numbers 3
echo "本日のナンバーズ3"
for i in 1..3:
  echo random(max=9)

# numbers 4
echo "本日のナンバーズ4"
for i in 1..4:
  echo random(max=9)
