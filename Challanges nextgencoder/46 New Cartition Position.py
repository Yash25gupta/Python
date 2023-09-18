from math import sin, cos, radians


def finalPosition(x, y, angle, dis):
    # if angle in (0, 180):
    #     x = x + dis if angle == 0 else x - dis
    # elif angle in (90, 270):
    #     y = y + dis if angle == 0 else y - dis
    # return x, y
    x += dis * cos(radians(angle))
    y += dis * sin(radians(angle))
    return round(x, 2), round(y, 2)


print(finalPosition(10, 20, 180, 20))
print(finalPosition(20, 0, 270, 20))
print(finalPosition(10, 20, 0, 20))
