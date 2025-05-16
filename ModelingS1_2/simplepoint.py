import random

class Point:
    """
    Class representing a 2D point in a Cartesian coordinate system.
    Includes comparison operators based on distance from the origin (0, 0).
    """

    def __init__(self, x, y):
        """
        Initializes a Point instance with x and y coordinates.

        Parameters:
            x (int | float): The x-coordinate of the point.
            y (int | float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a user-friendly string when the Point is printed.

        Returns:
            str: A formatted string representing the point's coordinates.
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Returns a string that represents the object, typically for debugging.

        Returns:
            str: Same as __str__, useful when printing lists of Points.
        """
        return self.__str__()

    def distance_from_origin(self):
        """
        Calculates the distance from this point to the origin (0, 0)
        using the Euclidean distance formula.

        Returns:
            float: Distance from origin.
        """
        return (self.x**2 + self.y**2) ** 0.5

    def __gt__(self, other):
        """
        Overrides the 'greater than' (>) operator based on distance from origin.

        Parameters:
            other (Point): Another Point instance to compare with.

        Returns:
            bool: True if this point is farther from the origin than the other.
        """
        return self.distance_from_origin() > other.distance_from_origin()

    def __eq__(self, other):
        """
        Overrides the equality operator (==). Two points are considered equal
        if they are the same distance from the origin.

        Parameters:
            other (Point): Another Point instance to compare with.

        Returns:
            bool: True if distances from origin are equal.
        """
        return self.distance_from_origin() == other.distance_from_origin()


# --- Script execution (not part of class) ---

if __name__ == "__main__":
    # Create a couple of points and print basic details
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(f"p1 coordinates: x={p1.x}, y={p1.y}")
    print(f"p1 as string: {p1}")

    # Generate a list of 5 random points
    print("\nGenerating 5 random points:")
    points = []
    for i in range(5):
        rand_point = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        points.append(rand_point)

    # Print the unsorted list of points
    print("Unsorted points:")
    print(points)

    # Sort the points based on their distance from origin
    points.sort()
    print("Sorted points by distance from origin:")
    print(points)

    # Calculate and display the distance from origin for a specific point
    specific_point = Point(-12, -5)
    print(f"\nDistance from origin for point {specific_point}: {specific_point.distance_from_origin():.2f}")

    # Comparison between tuples (note: this part doesn't interact with the class, for illustration only)
    p1 = (4, 6)
    p2 = (7, 7)
    print(f"Tuple comparison using __gt__: {p1.__gt__(p2)}")

    # Experimental section to find how often two random points are equal (by distance)
    print("\nSearching for point pairs with equal distance from origin...")
    found_equal = 0
    trials = 0
    while found_equal < 10:
        point_a = Point(random.randint(-100, 100), random.randint(-100, 100))
        point_b = Point(random.randint(-100, 100), random.randint(-100, 100))
        trials += 1
        if point_a == point_b:
            print(f"Equal pair found: {point_a} and {point_b}")
            found_equal += 1

    probability_estimate = trials / found_equal
    print(f"\nEstimated probability of equality: 1 in {probability_estimate:.2f}")