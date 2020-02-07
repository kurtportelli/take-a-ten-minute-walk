def isValidWalk(walk):
    x, y = 0, 0
    for direction in walk:
        if direction == 'n': y += 1
        if direction == 's': y -= 1
        if direction == 'e': x += 1
        if direction == 'w': x -= 1
    return len(walk) == 10 and x == 0 and y == 0
