# cau truc while
#while(<dieu_kien>):
#    <cac lenh trong while>

# Lenh range
    #range(start, end, step) .Neu để step là 2 thì sau mỗi vòng lặp sẽ cộng thêm 2

#s = "Hello"

#for i in s:
    #print(i)

#for i in range(10):  #Neu i = 10 thì sẽ dừng vòng lặp
    #print(i)   

    # s = 1 + 2 + 3 + 4 + ... + n voi n nhap tu ban phim

n = int(input("Nhap n = "))
s = 0
for i in range(1, n + 1):
    s += i 

print(s)       