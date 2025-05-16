from color_point import ColorPoint


class AdvancedPoint(ColorPoint):
    """
    An enhanced version of the ColorPoint class that introduces additional
    validation, encapsulation, and utility methods.
    """
    COLORS = ["red", "green", "blue", "black", "white"]

    def __init__(self, x, y, color):
        """
        Initializes an instance of AdvancedPoint while ensuring that inputs
        are valid types and that the color is supported.

        Parameters:
            x (int | float): The x-coordinate of the point.
            y (int | float): The y-coordinate of the point.
            color (str): The color of the point. Must be in the COLORS list.

        Raises:
            TypeError: If x or y are not int or float.
            ValueError: If color is not in the predefined COLORS list.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Expected a numerical type for x (int or float).")
        if not isinstance(y, (int, float)):
            raise TypeError("Expected a numerical type for y (int or float).")
        if color not in self.COLORS:
            raise ValueError(f"Unsupported color. Choose from: {self.COLORS}")

        # Call to parent constructor is commented out, using manual initialization.
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Retrieves the x-coordinate of the point.

        Returns:
            int | float: The x-coordinate.
        """
        return self._x

    @property
    def y(self):
        """
        Retrieves the y-coordinate of the point.

        Returns:
            int | float: The y-coordinate.
        """
        return self._y

    @property
    def color(self):
        """
        Accesses the color of the point.

        Returns:
            str: The current color.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Updates the point's color if the new color is valid.

        Parameters:
            new_color (str): The new color to apply to the point.

        Raises:
            ValueError: If new_color is not in the valid COLORS list.
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"Invalid color. Choose from: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        """
        Adds a new allowable color to the AdvancedPoint class's shared COLORS list.

        Parameters:
            new_color (str): The new color to be added.

        Returns:
            None
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Computes the Euclidean distance between two AdvancedPoint instances.

        Parameters:
            p1 (AdvancedPoint): The first point.
            p2 (AdvancedPoint): The second point.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def from_dictionary(data):
        """
        Constructs an AdvancedPoint from a dictionary. Useful for creating
        points from config files, APIs, etc.

        Parameters:
            data (dict): A dictionary that may contain keys: 'x', 'y', and 'color'.
                         Defaults are used if keys are missing.

        Returns:
            AdvancedPoint: A new instance with the specified or default attributes.
        """
        x = data.get("x", 10)
        y = data.get("y", 20)
        color = data.get("color", "black")
        return AdvancedPoint(x, y, color)


# Example usage and test cases

AdvancedPoint.add_color("amber")  # Add a custom color to the allowed list

p2 = AdvancedPoint(1, 2, "amber")
print(p2)  # Output will be the object representation
print(p2.color)  # amber
print(p2.color)  # redundant but tests repeated access
print(p2)
print(p2.x)  # 1
print(p2.y)  # 2

p2.color = "blue"  # Update color using the setter
print(p2)  # Color should now be blue

p3 = AdvancedPoint(-1, -2, "blue")
print(AdvancedPoint.distance_2_points(p2, p3))  # Calculate distance between p2 and p3

p4 = AdvancedPoint.from_dictionary({})  # Uses all defaults: x=10, y=20, color=black
print(p4)

p5 = AdvancedPoint.from_dictionary({"x": 44})  # Overrides x only
print(p5)