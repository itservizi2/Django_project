class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.side = [a, b, c]

    def is_valid(self):
        for side in self.side:
            if side <= 0:
                return False
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        return False

    def calculate_area(self):
        # calculate semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # calculate area using Heron's formula
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area

    def calculate_perimeter(self):
        return self.a + self.b + self.c


def main():
    while True:
        try:
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            triangle = Triangle(a, b, c)
            if triangle.is_valid():
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    area = triangle.calculate_area()
    perimeter = triangle.calculate_perimeter()
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")


if __name__ == "__main__":
    main()
