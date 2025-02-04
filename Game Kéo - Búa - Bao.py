# Game keo - bua - bao
# Quy uoc 1 - keo; 2 - bua; 3 - bao
# Muốn sinh ngẫu nhiên thì dùng hàm ran (random)


import random

robot = random.randint(1, 3)

user = input("Ban dinh ra cai gi (keo, bua, bao)? ")

if(user == "keo"):
    user = 1
elif(user == "bua"):
    user = 2
else:
    user = 3

if(user == 1):
    if(robot == 1):
        print("Robot chon keo, ban chon keo -> Hoa")
    elif(robot == 2):
        print("Robot chon bua, ban chon keo -> Robot thang")
    else:
        print("Robot chon bao, ban chon keo -> Ban thang")

elif(user == 2):
    if(robot == 1):
        print("Robot chon keo, ban chon bua -> Ban thang")
    elif(robot == 2):
        print("Robot chon bua, ban chon bua -> Hoa")
    else:
        print("Robot cho bao, ban chon bua -> Robot thang")

else:
    if(robot == 1):
        print("Robot chon keo, ban chon bao -> Robot thang")
    elif(robot == 2):
        print("Robot cho bua, ban chon bao -> Ban thang")
    else:
        print("Robot cho bao, ban chon bao -> Hoa")