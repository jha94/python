import my_class
import math
class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = my_class.Circle(10)
    
    def test_area(self):
        assert self.circle.area() == math.pi*self.circle.radius**2
    def test_perimeter(self):
        assert self.circle.perimeter() == 2*math.pi*self.circle.radius