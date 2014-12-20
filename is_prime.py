def is_prime(n):
    i = 1
    if n < 0:
        n = n * -1
    k = 0
    while i <= n:
        if n % i == 0:
            k += 1
        i += 1
    if k != 2:
        return False
    else:
        return True


def main():
    i = 17
    print("Is ", i, " a  prime number")
    print(is_prime(i))
if __name__ == '__main__':
    main()
