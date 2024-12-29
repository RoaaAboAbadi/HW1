# - If the length of the street is less than or equal to 60, the width of the street is
# 4 meters
# - If the length of the street is greater than 60 ,less than or equal to 80, the
# width of the street is 6 meters.
# - If the length of the street is greater than 80 meter, width of the street is 8
# meters.
# The program will do the following:
# - Read the length of the street from the user in meters.
# - Determine the street width according to the entered length
# - Calculating street area = street length * street width
# - Print street information vertically just one print statement

street_length = float(input("Enter the length of the street in meters: "))

if street_length <= 60:
    street_width = 4
    street_area = street_length * street_width
    print("Street length:", street_length, "meters")
    print("Street width:", street_width, "meters")
    print("Street area:", street_area, "square meters")
elif 60 < street_length <= 80:
    street_width = 6
    street_area = street_length * street_width
    print("Street length:", street_length, "meters")
    print("Street width:", street_width, "meters")
    print("Street area:", street_area, "square meters")
else:
    street_width = 8
    street_area = street_length * street_width
    print("Street length:", street_length, "meters")
    print("Street width:", street_width, "meters")
    print("Street area:", street_area, "square meters")
