from typing import List

class Space:
    def __init__(self, startRow, startCol, direction):
        self.startRow = startRow
        self.startCol = startCol
        self.direction = direction
        self.length = 0
        self.used = False
    
def findSpaces(grid):
    spaceList = []

    for r in range(10):
        c = 0
        while c < 10 - 1:
            if grid[r][c] == '-' and grid[r][c + 1] == '-':
                s = Space(r, c, 'horizontal')
                while c < 10 and grid[r][c] == '-':
                    s.length += 1
                    c += 1
                spaceList.append(s)
            c += 1
    
    for c in range(10):
        r = 0
        while r < 10 - 1:
            if grid[r][c] == '-' and grid[r + 1][c] == '-':
                s = Space(r, c, 'vertical')
                while r < 10 and grid[r][c] == '-':
                    s.length += 1
                    r += 1
                spaceList.append(s)
            r += 1
    return spaceList

def placeWord(word: str, space: Space, grid: List[str]):
    for i in range(space.length):
        if space.direction == 'horizontal':
            if grid[space.startRow][space.startCol+i] == '-' or grid[space.startRow][space.startCol+i] == word[i]:
                grid[space.startRow][space.startCol+i] = word[i]
        else:
            if grid[space.startRow+i][space.startCol] == '-' or grid[space.startRow+i][space.startCol] == word[i]:
                grid[space.startRow+i][space.startCol] = word[i]

def isValid(word: List[str], space: Space, grid: List[List[str]]):
    if space.used is True:
        return False

    if space.length != len(word):
        return False
    
    for i in range(space.length):
        if space.direction == 'horizontal':
            if grid[space.startRow][space.startCol+i] != '-' and grid[space.startRow][space.startCol+i] != word[i]:
                return False
        else:
            if grid[space.startRow+i][space.startCol] != '-' and grid[space.startRow+i][space.startCol] != word[i]:
                return False
    return True

def replaceSpace(word: str, space: Space, grid: List[str]):
    origin = []
    for i in range(space.length):
        if space.direction == 'horizontal':
            origin.append(grid[space.startRow][space.startCol+i])
            grid[space.startRow][space.startCol+i] = word[i]
        else:
            origin.append(grid[space.startRow+i][space.startCol])
            grid[space.startRow+i][space.startCol] = word[i]
    return origin

def restoreSpace(origin: List[str], space: Space, grid: List[str]):
    for i in range(space.length):
        if space.direction == 'horizontal':
            origin.append(grid[space.startRow][space.startCol+i])
            grid[space.startRow][space.startCol+i] = origin[i]
        else:
            origin.append(grid[space.startRow+i][space.startCol])
            grid[space.startRow+i][space.startCol] = origin[i]

def helper(wordListIdx: int, grid: List[List[str]], wordList: List[str], spaceList: List[Space]):
    if wordListIdx >= len(wordList):
        return True
    findAns = False
    for space in spaceList:
        if isValid(wordList[wordListIdx], space, grid):
            space.used = True
            origin = replaceSpace(wordList[wordListIdx], space, grid)
            if helper(wordListIdx+1, grid, wordList, spaceList):
                findAns = True
                break
            restoreSpace(origin, space, grid)
            space.used = False

    return findAns

                
def crosswordPuzzle(crossword: List[str], words: str):
    wordList = words.split(';')
    grid = []
    for line in crossword:
        grid.append([*line])

    spaceList = findSpaces(grid)
    helper(0, grid, wordList, spaceList)

    for i, charList in enumerate(grid):
        grid[i] = "".join(charList)
    return grid



if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        item = input()
        crossword.append(item)
    
    words = input()

    result = crosswordPuzzle(crossword, words)

    print('\n'.join(result))
        