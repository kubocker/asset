# File: main.nim

import random

randomize()

# numbers 3
echo "本日のナンバーズ3"
for i in 1..3:
  echo random(max=9)

# numbers 4
echo "本日のナンバーズ4"
for i in 1..4:
  echo random(max=9)
