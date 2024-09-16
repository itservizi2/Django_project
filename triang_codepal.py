class Triangle:

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

        # Check the triangle inequality theorem
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise ValueError("The provided lengths do not form a valid triangle.")

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2  # Semi-perimeter
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area

    def perimeter(self) -> float:
        return self.a + self.b + self.c


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def main():
    print("Enter the lengths of the sides of the triangle:")

    # Get positive side lengths from the user
    a = get_positive_float("Length of side a: ")
    b = get_positive_float("Length of side b: ")
    c = get_positive_float("Length of side c: ")

    try:
        # Create a Triangle object
        triangle = Triangle(a, b, c)

        # Calculate area and perimeter
        area = triangle.area()
        perimeter = triangle.perimeter()

        # Display results
        print(f"The area of the triangle is: {area:.2f}")
        print(f"The perimeter of the triangle is: {perimeter:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
