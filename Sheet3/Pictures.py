from gasp import *

begin_graphics()

Circle((300, 220), (40))

Circle((285, 233), (5))

Circle((315, 233), (5))

Circle((285, 233), (1.5), filled=True)

Circle((315, 233), (1.5), filled=True)

Line((300, 230), (290, 210))

Line((290, 210), (310, 210))

Arc((300, 220), 30, 220, 325)

Line((277, 202), (324.49999999999997155, 202))

Circle((253, 225), (7))

Circle((347, 225), (7))

Circle((253, 222.5), (1), filled=True)

Circle((347, 222.5), (1), filled=True)

Line((285, 245), (295, 235))

Line((315, 245), (305, 235))

Line((300, 260), (300, 275))

Line((300, 260), (285, 270))

Line((300, 260), (315, 270))

update_when('key_pressed')   

end_graphics()
