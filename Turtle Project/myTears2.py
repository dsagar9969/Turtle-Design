def tear2(t):
    for times in range(48):
        t.begin_fill()
        t.color("cyan")
        t.circle(times/8)
        t.left(202)
        t.forward(101)
        t.end_fill()
