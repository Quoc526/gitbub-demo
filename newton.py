import math
def compute_square_root(N, num_loops):
    x_n = N / 2.0 
    for i in range(num_loops): # range(start,stop,step) , for c in "hello" : chạy kí tự
        x_np1 = (x_n + N/x_n) / 2.0
        x_n = x_np1

    return x_np1

    n = 10
    while i < n :
        print(i)
        i = i + 1

print(compute_square_root(9, 10))
print(compute_square_root(2,11))

#không nên dùng đệ quy mà dùng vòng lặp for