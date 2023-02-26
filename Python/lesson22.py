import math

class Sphere():

    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4/3*math.pi*self.r**3

    def get_square(self):
        return 4*math.pi*self.r**2

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return True if ((x-self.x)**2)+((y-self.y)**2)+((z-self.z)**2) < self.r**2 else False

new_sphere = Sphere(0.6, 0, 0, 0)
print("Радиус сферы:", new_sphere.get_radius())
print("Объем сферы:", new_sphere.get_volume())
print("Площадь сферы:", new_sphere.get_square())
print("Центр сферы:", new_sphere.get_center())
print(f"Находится ли точка с координатами x = {0}, y = {-1.5}, z = {0} внутри сферы:", new_sphere.is_point_inside(0, -1.5, 0))
new_sphere.set_radius(1.6)
print("Новый радиус сферы:", new_sphere.get_radius())
print(f"Находится ли точка с координатами x = {0}, y = {-1.5}, z = {0} внутри сферы:", new_sphere.is_point_inside(0, -1.5, 0))
