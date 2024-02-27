from turtle import *
from random import randint
from colorsys import *
class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)

    def translate(self, dx, dy):
        self._position =(self._position[0] + dx, self._position[1] + dy)

    def set_position(self, x, y):
        self._position=(x, y)

    def cap(self, vertex):
        x= self._position[0] + vertex[0]
        y = self._position[1] + vertex[1]
        return x, y

    def draw(self):
        v0 = self.cap((0, 0))
        v1 = self.cap(self._vertex1)
        v2 = self.cap(self._vertex2)
        a = randint(0, 10)/10
        b = randint(0, 10)/10
        c = randint(0, 10)/10


        up()
        pencolor(a, b, c)
        setpos(*v0)
        down()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        up()
def CreateTriangles(num):
    bound = 350
    triangles = []
    for i in range (num):
        x1 = randint(-bound, bound)
        y1 = randint(-bound, bound)
        x2 = randint(-bound, bound)
        y2 = randint(-bound, bound)
        t = Triangle(x1, y1, x2, y2)
        triangles.append(t)
    return triangles

if __name__ == '__main__':
    triangles = CreateTriangles(50)
    for el in  triangles:
        bound = 100
        x0 = randint(-bound, bound)
        y0 = randint(-bound, bound)
        el.set_position(x0, y0)
        el.draw()



    mainloop()