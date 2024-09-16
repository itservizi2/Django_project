from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Triangle(BaseModel):
    a: Annotated[float, Field(gt=0)]
    b: Annotated[float, Field(gt=0)]
    c: Annotated[float, Field(gt=0)]

    @property
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    @property
    def area(self):
        if self.is_valid:
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        else:
            return None

    @property
    def perimeter(self):
        if self.is_valid:
            return self.a + self.b + self.c
        else:
            return None


def get_side(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Side length must be positive.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    a = get_side("Enter side a: ")
    b = get_side("Enter side b: ")
    c = get_side("Enter side c: ")

    triangle = Triangle(a=a, b=b, c=c)

    if triangle.is_valid:
        print(f"Area: {triangle.area:.2f}")
        print(f"Perimeter: {triangle.perimeter:.2f}")
    else:
        print("The sides do not form a valid triangle.")


if __name__ == "__main__":
    main()
