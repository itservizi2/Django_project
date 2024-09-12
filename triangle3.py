from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TriangleSides(BaseModel):
    a: Annotated[float, Field(gt=0)]
    b: Annotated[float, Field(gt=0)]
    c: Annotated[float, Field(gt=0)]


def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


def calculate_area(a: float, b: float, c: float) -> float:
    # calculate semi-perimeter
    s = (a + b + c) / 2
    # calculate area using Heron's formula
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def main():
    while True:
        try:
            a = float(input("Enter side length a: "))
            b = float(input("Enter side length b: "))
            c = float(input("Enter side length c: "))
            triangle_sides = TriangleSides(a=a, b=b, c=c)
            # check if the sides form a valid triangle
            if a + b > c and a + c > b and b + c > a:
                break
            else:
                print("Invalid triangle sides. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    perimeter = calculate_perimeter(a, b, c)
    area = calculate_area(a, b, c)
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")


if __name__ == "__main__":
    main()
