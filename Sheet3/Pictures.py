from gasp import *

begin_graphics()

Circle((300, 220), (40))

Circle((285, 230), (5))

Circle((315, 230), (5))

Line((300, 230), (290, 210))

Line((290, 210), (310, 210))

Arc((300, 220), 30, 225, 315)

update_when('key_pressed')   

end_graphics()
