from pydantic import BaseModel, confloat


class Triangle(BaseModel):
    side1: confloat(gt=0)
    side2: confloat(gt=0)
    side3: confloat(gt=0)


def calculate_triangle_properties():
    while True:
        try:
            triangle = Triangle(
                side1=float(input("Enter the first side length of the triangle : ")),
                side2=float(input("Enter the second side length of the triangle : ")),
                side3=float(input("Enter the third side length of the triangle : "))
            )
            if triangle.side1 + triangle.side2 > triangle.side3 and \
                    triangle.side2 + triangle.side3 > triangle.side1 and \
                    triangle.side1 + triangle.side3 > triangle.side2:
                area = 0.5 * triangle.side1 * triangle.side2
                perimeter = triangle.side1 + triangle.side2 + triangle.side3
                print(f"Area of the triangle: {area} ")
                print(f"Perimeter of the triangle: {perimeter} ")
                break
            else:
                print("The sides do not form a valid triangle. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")


if __name__ == "__main__":
    calculate_triangle_properties()
