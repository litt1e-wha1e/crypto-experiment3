# 定义计算最大公约数的函数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 定义函数pq
def pq(p, q):
    phi = (p - 1) * (q - 1)
    return sum([e for e in range(2, phi) if
                gcd(e, phi) == 1 and (gcd(e - 1, p - 1) + 1 == 3) and (gcd(e - 1, q - 1) + 1 == 3)])


# 主函数
def main():
    print(pq(1009, 3643))


# 如果作为主程序运行，则调用main函数
if __name__ == "__main__":
    main()
