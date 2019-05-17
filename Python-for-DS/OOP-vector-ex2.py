import math

class Points(object):
    '''A class for dot and cross product of 3D vectors'''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return print("({},{},{})".format(self,x, self.y, self.z))

    def __sub__(self, no):
        sub_x = self.x - no.ximport math
        sub_y = self.y - no.y
        sub_z = self.z - no.z
        return Points(sub_x,sub_y, sub_z)

    def dot(self, no):
        dot_x  = self.x * no.x
        dot_y = self.y * no.y
        dot_z = self.z * no.z
        return dot_x+dot_y+dot_z


    def cross(self, no):
        cr_x = self.y*no.z - self.z*no.y 
        cr_y = self.z*no.x - self.x*no.z
        cr_z = self.x*no.y - self.y*no.x
        return Points(cr_x, cr_y, cr_z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
