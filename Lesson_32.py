import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")

        self.number1 = tk.StringVar()
        self.number2 = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.number1).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.number2).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="+", command=self.add).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.root, text="-", command=self.subtract).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="*", command=self.multiply).grid(row=2, column=2, padx=10, pady=10)
        tk.Button(self.root, text="/", command=self.divide).grid(row=2, column=3, padx=10, pady=10)

        tk.Label(self.root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.result, state='readonly').grid(row=3, column=1, padx=10, pady=10)

    def get_numbers(self):
        try:
            num1 = float(self.number1.get())
            num2 = float(self.number2.get())
            return Calculator(num1), Calculator(num2)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 and num2:
            self.result.set(str(num1 + num2))

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 and num2:
            self.result.set(str(num1 - num2))

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 and num2:
            self.result.set(str(num1 * num2))

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 and num2:
            try:
                self.result.set(str(num1 / num2))
            except ZeroDivisionError:
                messagebox.showerror("Math Error", "Cannot divide by zero.")


root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()


class Calculator:
    def __init__(self, number):
        if isinstance(number, (int, float)):
            self.__number = number
        else:
            raise TypeError("The number must be an int or float.")

    # Getter method
    def get_number(self):
        return self.__number

    # Magic methods for arithmetic operations
    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number + other.__number)
        return Calculator(self.__number + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number - other.__number)
        return Calculator(self.__number - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number * other.__number)
        return Calculator(self.__number * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number / other.__number)
        return Calculator(self.__number / other)

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number // other.__number)
        return Calculator(self.__number // other)

    def __mod__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number % other.__number)
        return Calculator(self.__number % other)

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__number ** other.__number)
        return Calculator(self.__number ** other)

    # Magic methods for in-place arithmetic operations
    def __iadd__(self, other):
        if isinstance(other, Calculator):
            self.__number += other.__number
        else:
            self.__number += other
        return self

    def __isub__(self, other):
        if isinstance(other, Calculator):
            self.__number -= other.__number
        else:
            self.__number -= other
        return self

    def __imul__(self, other):
        if isinstance(other, Calculator):
            self.__number *= other.__number
        else:
            self.__number *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            self.__number /= other.__number
        else:
            self.__number /= other
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            self.__number //= other.__number
        else:
            self.__number //= other
        return self

    def __imod__(self, other):
        if isinstance(other, Calculator):
            self.__number %= other.__number
        else:
            self.__number %= other
        return self

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            self.__number **= other.__number
        else:
            self.__number **= other
        return self

    # Magic methods for comparison operations
    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.__number == other.__number
        return self.__number == other

    def __ne__(self, other):
        if isinstance(other, Calculator):
            return self.__number != other.__number
        return self.__number != other

    def __gt__(self, other):
        if isinstance(other, Calculator):
            return self.__number > other.__number
        return self.__number > other

    def __ge__(self, other):
        if isinstance(other, Calculator):
            return self.__number >= other.__number
        return self.__number >= other

    def __lt__(self, other):
        if isinstance(other, Calculator):
            return self.__number < other.__number
        return self.__number < other

    def __le__(self, other):
        if isinstance(other, Calculator):
            return self.__number <= other.__number
        return self.__number <= other

    # Magic methods for string representations
    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return f"{self.__number} ({type(self.__number).__name__})"
