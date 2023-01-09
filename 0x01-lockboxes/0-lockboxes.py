#!/usr/bin/python3

"""ALX Interview Lockboxes"""


def canUnlockAll(boxes):
    """
    To determine if all the boxes can be opened
    """
    if type(boxes) is not list:
        return False
    if len(boxes) == 0:
        return False
    for i in range(1, len(boxes)-1):
        isLock = False
        for j in range(0, len(boxes)):
            if i in boxes[j] and j != i:
                isLock = True
                break
        if isLock = False:
            return False
    return True
