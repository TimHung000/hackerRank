def helper(n):
    if len(n) == 1:
        return n
    
    sum = 0
    for digit in n:
        sum += int(digit)

    return helper(str(sum))


def superDigit(n, k):
    sum = 0
    for digit in n:
        sum += int(digit)
    sum *= k
    return helper(str(sum))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    print(result)
