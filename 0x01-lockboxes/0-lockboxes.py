#!/usr/bin/python3
"""
Solution to lock-box interview question.
"""

def canUnlockAll(boxes):
    """
        Checks if all boxes can be unlocked.
    """
    if not boxes:
        return True

    opened_boxes = set()
    opened_boxes.add(0)

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)

