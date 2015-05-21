import string
import math
shape = raw_input().lower()
if shape.split().count('hexagon'):
    sides = 6
if shape.split().count('pentagon'):
    sides = 5
if shape.split().count('decagon'):
    sides = 10
if shape.split().count('octagon'):
    sides = 8
if shape.split().count('infinityagon'):
    print "Shut up Thomas"
else:
    word_start = 'nope'
    if len(shape.lower().translate(None, string.ascii_lowercase).split())==2:
        numbers = shape.lower().translate(None, string.ascii_lowercase)
        side_lengths = numbers.split()[1]
        print side_lengths
        sides = numbers.split()[0]
    else:
        side_lengths = shape.lower().translate(None, string.ascii_lowercase+""" ~!@#$%^&*()_+-={}|[]\;':",./<>?`""")
    print side_lengths
    center_degree = 360/int(sides)
    temp_degree = center_degree/2-90
    apothem = (float(side_lengths)/2)*math.tan(math.radians(temp_degree))
    print 'Apothem:' + str(apothem*-1) 
    area = float(sides)*(apothem*float(side_lengths))/2
    print 'Area:'+str(area*-1)
    perimeter = int(side_lengths)*sides
    print 'Perimeter:' +str(perimeter)