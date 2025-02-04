# Cau truc lap for
# for <ten_bien> in <tap_hop>:
# <lenh trong for>

a = "Hello"

for i in a:     # i dùng để chạy từng kí tự trong tập hợp
    print(i)

# Lenh range
#    range(start, end, step)    (start la gia tri bắt đầu, end là giá trị kết thúc, step là bước nhảy)

    
for i in range(1, 11, 2):  # Nếu i >= 10 thi se dung vong lap
    print("Hoc cong nghe")
    print(i)

# s1 = 1 + 2 + 3 + 4 + ... + n voi n nhap tu ban phim

n = int(input("Nhap n ="))
s = 0

for i in range(1, n + 1):
    s += i

print(s)    # n = 5 lÀ 1 + 2 + 3 + 4 + 5