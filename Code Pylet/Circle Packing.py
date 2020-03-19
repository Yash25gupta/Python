# code.Pylet - Circle Packing
# watch the video here - https://youtu.be/HLUqDIOng80
# Any questions? Just ask!

import random
import math
import sys
import pygame

W, H = 864, 486
HW, HH = W / 2, H / 2
AREA = W * H


class circle:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.radius = 2
        self.id = id
        self.active = True


circles = list([])
find_space_attempts = 0
max_find_space_attempts = 100000
exit = False
gap = 3

area_covered = 0.0
percentage_covered = 0
last_reported_percentage = -1

while True:
    while True:
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)

        found_space = True
        for c in circles:
            distance = math.hypot(c.x - x, c.y - y)
            if distance <= c.radius + gap:
                found_space = False
                break
        if found_space: break
        find_space_attempts += 1
        if find_space_attempts >= max_find_space_attempts:
            exit = True
            break

    if exit: break
    circles.append(circle(x, y, len(circles)))

    for c in circles:
        if not c.active: continue
        for C in circles:
            if c.id == C.id: continue

            distance_between_circles = math.hypot(c.x - C.x, c.y - C.y)
            combined_radius = c.radius + C.radius

            if distance_between_circles - combined_radius <= gap:
                c.active = False
                if C.active:
                    area_covered += (C.radius ** 2) * math.pi
                C.active = False

                area_covered += (c.radius ** 2) * math.pi
                percentage_covered = int((area_covered / AREA) * 100)
                if last_reported_percentage != percentage_covered:
                    print(percentage_covered)
                    last_reported_percentage = percentage_covered
                break

        if c.active: c.radius += 1

print("Circles Generated!")
print("Saving File.")
image = pygame.Surface((W, H))
for c in circles:
    pygame.draw.circle(image, (255, 255, 255), (c.x, c.y), c.radius, 1)
pygame.image.save(image, "circle.png")
print("Done")
