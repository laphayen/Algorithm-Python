
# 최대공약구
def gcd(a, b):

    # 최소값 함수수
    i = min(a,b)

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(1, 6))