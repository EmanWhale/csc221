from gasp import *

begin_graphics()

Circle((300, 220), (40))

Circle((285, 233), (5))

Circle((315, 233), (5))

Line((300, 230), (290, 210))

Line((290, 210), (310, 210))

Arc((300, 220), 30, 225, 315)

Circle((255, 225), (5))

Circle((345, 225), (5))

Line((285, 245), (295, 235))

Line((315, 245), (305, 235))

update_when('key_pressed')   

end_graphics()
