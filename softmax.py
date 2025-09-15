
 #chuyển các giá trị của một vectỏ thành các giá trị xác suất bằng softmax
import math 

v1 = float(input())
v2 = float(input())
v3 = float(input())

max_value = v3

total = math.exp(v1) + math.exp(v2) + math.exp(v3)

# khi trừ đi max_value thì giá trị xác suất không thay đổi 
# chấp nhận underflow
# hàm sigmoid nữa 
# cần chuyển qua xác suất để dùng hàm cross-entropy
# cách khử vòng lặp for để chạy framework của DL,ML
s1 = (math.exp(v1) - max_value) / total
s2 = (math.exp(v2) - max_value) / total
s3 = (math.exp(v3) - max_value) / total

print(f"{s1:.5f}  {s2:.5f}  {s3:.5f}")
