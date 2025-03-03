n = int(input())


def one_fdd(n):
    for i in range(1, n + 1):
        print((" " * (n - i) + "*" * (2 * i - 1)))
        

def two_ddd(n):
    for i in range(n-1, 0, -1):
        print((" " * (n - i) + "*" * (2 * i - 1)))


one_fdd(n)
two_ddd(n)