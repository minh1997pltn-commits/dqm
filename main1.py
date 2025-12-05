#Cho n số nguyên, nhiệm vụ của bạn là với mỗi số, hãy in ra số lượng ước của nó.Ví dụ, nếu x = 18, đáp án là 6 vì các ước của 18 là 1, 2, 3, 6, 9, 18.
"""
Dữ liệu vào
Dòng đầu tiên chứa số nguyên n: số lượng số cần xử lý.
Sau đó có n dòng, mỗi dòng chứa một số nguyên x.
Dữ liệu ra
Với mỗi số x, in ra số lượng ước của x.
"""
import math
n = int(input())
a = []
for i in range (n):
    a.append(int(input()))
for x in a:
    count = 0   
    for i in range (1,int(math.sqrt(x))+1):
        if x % i == 0 :
            count += 1
            if i != x//i :
                count +=1
    print(count)
    
