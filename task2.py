import math
center_file = input()
coordinates_file=input()
center = open(center_file, 'r', encoding = 'UTF-8')
center_content = list(map(str.strip, center.readlines())) #список координат центра и радиус
a=int(center_content[0].split()[0])
b=int(center_content[0].split()[1])
radius = int(center_content[1]) #list center coord
center.close()
coordinates = open(coordinates_file, 'r', encoding = 'UTF-8')
coordinates_content = list(map(str.strip, coordinates.readlines())) #список координат точек
for i in coordinates_content:
    x_y = i.split()
    dist = math.sqrt((int(x_y[0])-a)**2 + (int(x_y[1])-b)**2)
    if dist == radius:
        print('0')
    elif dist < radius:
        print('1')
    elif dist > radius:
        print('2')
coordinates.close()
