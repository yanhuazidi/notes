print("求球的颜色搭配")
for red in range(1,4):
    for yellow in range(1,4):
        for green in range(1,7):
            if red+yellow+green==8:
                print(red,"红",yellow,"黄",green,"绿")