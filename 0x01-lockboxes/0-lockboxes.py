#!/usr/bin/python3
"""
Defines a function that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""

    unlocked = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue

        for item in box:
            if item < len(boxes) and item not in unlocked and item != box_id:
                unlocked.append(item)

    if len(unlocked) == len(boxes):
        return True
    return False
