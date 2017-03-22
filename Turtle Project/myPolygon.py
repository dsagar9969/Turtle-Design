def polygon (t,sides,distance):
    for times in range(sides):
        t.forward(distance)
        t.left(360/sides)
