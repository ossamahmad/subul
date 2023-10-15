class Calculator:
    def add(self, x, y):
        """
        Args:
            x (number): first argumentt
            y (number): second argument

        Returns:
            number: the sum of the two argument
        """
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        if x == 0:
            return 0
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
