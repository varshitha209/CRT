def reverse_number(n: int) -> int:
    reverse = 0
    while n >0:
        digit = n%10
        reverse = reverse*10 +digit 
        n = n//10
    return reverse

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
