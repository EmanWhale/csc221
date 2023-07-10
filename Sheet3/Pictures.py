from gasp import *

begin_graphics()

Circle((300, 220), (40))

Circle((285, 233), (5))

Circle((315, 233), (5))

Circle((285, 233), (1), filled=True)

Circle((315, 233), (1), filled=True)

Line((300, 230), (290, 210))

Line((290, 210), (310, 210))

Arc((300, 220), 30, 225, 315)

Circle((253, 225), (7))

Circle((347, 225), (7))

Line((252.5, 221.5), (253.5, 221.5))

Line((346.5, 222), (347.5, 222))

Line((285, 245), (295, 235))

Line((315, 245), (305, 235))

update_when('key_pressed')   

end_graphics()
