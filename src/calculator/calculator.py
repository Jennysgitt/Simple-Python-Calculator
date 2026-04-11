import math


class Calculator:
    """
    Calculator class with methods to sum, subtract,
    multiply, divide square and find square root.
    """

    def __init__(self, memory=0):
        self.memory = memory

    def reset_memory(self):
        """
        Resets the memory back to zero.
        """
        self.memory = 0

    def sum(self, a, b=None):
        """
        Returns sum of two numeric values.

        Args:
            a (float): The first number.
            b (float): The second number. If None, uses
                the current memory.

        Returns:
            float: The sum of the provided numbers.
        """
        try:
            if b is None:
                b = self.memory

            self.memory = float(a) + float(b)
            return self.memory
        except Exception:
            return 'Invalid input'

    def subtract(self, a, b=None):
        """
        Returns subtraction result of two numeric values.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract. If None,
                uses the current memory.

        Returns:
            float: The subtraction result.
        """
        try:
            if b is None:
                b = a
                a = self.memory

            self.memory = float(a) - float(b)
            return self.memory
        except Exception:
            return 'Invalid input'

    def multiply(self, a, b=None):
        """
        Returns multiplication result of two numeric values.

        Args:
            a (float): The first factor.
            b (float): The second factor. If None,
                uses the current memory.

        Returns:
            float: The product of the numbers.
        """
        try:
            if b is None:
                b = self.memory

            self.memory = float(a) * float(b)
            return self.memory
        except Exception:
            return 'Invalid input'

    def divide(self, a, b=None):
        """
        Returns division result of two numeric values.

        Args:
            a (float): The dividend.
            b (float): The divisor. If None,
                uses the current memory.

        Returns:
            float: The quotient.
        """
        try:
            if b is None:
                b = a
                a = self.memory

            self.memory = float(a) / float(b)
            return self.memory
        except ZeroDivisionError:
            return 'Can not divide by zero.'
        except Exception:
            return 'Invalid input'

    def square(self, a=None):
        """
        Returns square of provided numeric value.

        Args:
            a (float, optional): The number to be squared.
                If None, uses the current memory.

        Returns:
            float: The square result.
        """
        try:
            if a is None:
                a = self.memory

            self.memory = float(a) ** 2
            return self.memory
        except Exception:
            return 'Invalid input'

    def sqrt(self, a=None):
        """
        Returns square root of provided numeric value.

        Args:
            a (float, optional): The number to find square
                root of. If None, uses the current memory.

        Returns:
            float: The square root result.
        """
        try:
            if a is None:
                a = self.memory

            self.memory = math.sqrt(float(a))
            return self.memory
        except Exception:
            return 'Invalid input'
