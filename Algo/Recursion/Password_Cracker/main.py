from typing import List
import sys

sys.setrecursionlimit(10 ** 8)

def match(word, currentIdx, loginAttempt):
    for i in range(len(word)):
        if currentIdx + i >= len(loginAttempt) or word[i] != loginAttempt[currentIdx+i]:
            return False
    return True

def helper(passwords: List[str], currentIdx: int, loginAttempt: str, resList: List[str], memo: dict):
    if currentIdx >= len(loginAttempt):
        return True
    if memo.get(currentIdx):
        return False
    for password in passwords:
        if match(password, currentIdx, loginAttempt):
            resList.append(password)
            if helper(passwords, currentIdx + len(password), loginAttempt, resList, memo):
                return True
            memo[currentIdx+len(password)] = True
            resList.pop()
    return False

def passwordCracker(passwords, loginAttempt):
    resList = []
    # used to check if 
    memo = {}
    if helper(passwords, 0, loginAttempt, resList, memo):
        return " ".join(resList)
    return 'WRONG PASSWORD'

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        print(result)