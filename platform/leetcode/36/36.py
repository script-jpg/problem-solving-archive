# https://leetcode.com/problems/valid-sudoku/description/

from typing import List
import itertools


def validList(l: List[str]) -> bool:
    filtered = [c for c in l if c != "."]
    res = len(filtered) == len(set(filtered))
    return res


def transpose(board: List[List[str]], r=9) -> List[List[str]]:
    new_board = []
    for i in range(r):
        new_board.append([])
        for j in range(r):
            new_board[-1].append(board[j][i])
    return new_board


def subboxes(board: List[List[str]]) -> List[List[str]]:
    boxes = []
    starts = itertools.product([0, 3, 6], [0, 3, 6])
    for i, j in starts:
        boxes.append([board[a][b] for a in range(i, i + 3) for b in range(j, j + 3)])
    return boxes


def isValidSudoku(board: List[List[str]]) -> bool:
    test = False
    if test:
        assert validList(["5", "3", "."])
        assert validList([".", "."])
        assert not validList(["5", ".", "5"])
        assert transpose([["1", "2"], ["3", "4"]], r=2) == [["1", "3"], ["2", "4"]]
        print(subboxes(board))
    return (
        all(map(validList, board))
        and all(map(validList, transpose(board)))
        and all(map(validList, subboxes(board)))
    )
