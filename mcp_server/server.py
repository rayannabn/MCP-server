"""
MCP Server for Calculator Operations
Provides tools for basic and advanced mathematical operations
"""

import json
import math
from collections import Counter
from typing import Any


class CalculatorServer:
    """MCP Server implementing calculator tools"""

    def __init__(self):
        self.tools = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
            "power": self.power,
            "square_root": self.square_root,
            "percentage": self.percentage,
            "absolute": self.absolute,
            "factorial": self.factorial,
            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,
            "log": self.log,
            "ln": self.ln,
            "ceiling": self.ceiling,
            "floor": self.floor,
            "mean": self.mean,
            "median": self.median,
            "mode": self.mode,
            "std_dev": self.std_dev,
            "variance": self.variance,
            "range": self.range,
            "sum": self.sum,
            "count": self.count,
            "min": self.min,
            "max": self.max,
        }

    def get_tools(self) -> list[dict[str, Any]]:
        """Return list of available tools with their descriptions"""
        return [
            {
                "name": "add",
                "description": "Add two numbers: a + b",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "First number"},
                        "b": {"type": "number", "description": "Second number"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "subtract",
                "description": "Subtract two numbers: a - b",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "First number"},
                        "b": {"type": "number", "description": "Second number"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "multiply",
                "description": "Multiply two numbers: a * b",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "First number"},
                        "b": {"type": "number", "description": "Second number"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "divide",
                "description": "Divide two numbers: a / b",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Numerator"},
                        "b": {"type": "number", "description": "Denominator"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "power",
                "description": "Raise a number to a power: a ^ b",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Base"},
                        "b": {"type": "number", "description": "Exponent"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "square_root",
                "description": "Calculate square root of a number",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Number to find square root of"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "percentage",
                "description": "Calculate percentage: (a / b) * 100",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Numerator"},
                        "b": {"type": "number", "description": "Denominator"},
                    },
                    "required": ["a", "b"],
                },
            },
            {
                "name": "absolute",
                "description": "Get absolute value of a number",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Number"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "factorial",
                "description": "Calculate factorial of a number (n!)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "integer", "description": "Non-negative integer"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "sin",
                "description": "Calculate sine of an angle in radians",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Angle in radians"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "cos",
                "description": "Calculate cosine of an angle in radians",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Angle in radians"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "tan",
                "description": "Calculate tangent of an angle in radians",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Angle in radians"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "log",
                "description": "Calculate logarithm base 10",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Positive number"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "ln",
                "description": "Calculate natural logarithm",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Positive number"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "ceiling",
                "description": "Get ceiling (round up) of a number",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Number"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "floor",
                "description": "Get floor (round down) of a number",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "Number"},
                    },
                    "required": ["a"],
                },
            },
            {
                "name": "mean",
                "description": "Calculate arithmetic mean (average) of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "median",
                "description": "Calculate median (middle value) of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "mode",
                "description": "Calculate mode (most frequent value) of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "std_dev",
                "description": "Calculate standard deviation of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "variance",
                "description": "Calculate variance of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "range",
                "description": "Calculate range (max - min) of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "sum",
                "description": "Calculate sum of a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "count",
                "description": "Count the number of elements in a list",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "min",
                "description": "Find minimum value in a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
            {
                "name": "max",
                "description": "Find maximum value in a list of numbers",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}, "description": "List of numbers"},
                    },
                    "required": ["numbers"],
                },
            },
        ]

    def execute_tool(self, tool_name: str, **kwargs) -> dict[str, Any]:
        """Execute a tool with the given parameters"""
        if tool_name not in self.tools:
            return {"error": f"Tool '{tool_name}' not found"}

        try:
            result = self.tools[tool_name](**kwargs)
            return {"result": result, "success": True}
        except Exception as e:
            return {"error": str(e), "success": False}

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers"""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Raise a number to a power"""
        return a ** b

    @staticmethod
    def square_root(a: float) -> float:
        """Calculate square root"""
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)

    @staticmethod
    def percentage(a: float, b: float) -> float:
        """Calculate percentage"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return (a / b) * 100

    @staticmethod
    def absolute(a: float) -> float:
        """Get absolute value"""
        return abs(a)

    @staticmethod
    def factorial(a: int) -> int:
        """Calculate factorial"""
        if a < 0:
            raise ValueError("Factorial of negative number is undefined")
        return math.factorial(a)

    @staticmethod
    def sin(a: float) -> float:
        """Calculate sine"""
        return math.sin(a)

    @staticmethod
    def cos(a: float) -> float:
        """Calculate cosine"""
        return math.cos(a)

    @staticmethod
    def tan(a: float) -> float:
        """Calculate tangent"""
        return math.tan(a)

    @staticmethod
    def log(a: float) -> float:
        """Calculate log base 10"""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is undefined")
        return math.log10(a)

    @staticmethod
    def ln(a: float) -> float:
        """Calculate natural logarithm"""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is undefined")
        return math.log(a)

    @staticmethod
    def ceiling(a: float) -> int:
        """Get ceiling value"""
        return math.ceil(a)

    @staticmethod
    def floor(a: float) -> int:
        """Get floor value"""
        return math.floor(a)

    @staticmethod
    def mean(numbers: list[float]) -> float:
        """Calculate arithmetic mean (average)"""
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: list[float]) -> float:
        """Calculate median (middle value)"""
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]

    @staticmethod
    def mode(numbers: list[float]) -> list[float]:
        """Calculate mode (most frequent value(s))"""
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")
        counts = Counter(numbers)
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return modes

    @staticmethod
    def std_dev(numbers: list[float]) -> float:
        """Calculate standard deviation"""
        if not numbers:
            raise ValueError("Cannot calculate standard deviation of empty list")
        if len(numbers) < 2:
            raise ValueError("Need at least 2 numbers for standard deviation")
        mean_val = sum(numbers) / len(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers: list[float]) -> float:
        """Calculate variance"""
        if not numbers:
            raise ValueError("Cannot calculate variance of empty list")
        if len(numbers) < 2:
            raise ValueError("Need at least 2 numbers for variance")
        mean_val = sum(numbers) / len(numbers)
        return sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)

    @staticmethod
    def range(numbers: list[float]) -> float:
        """Calculate range (max - min)"""
        if not numbers:
            raise ValueError("Cannot calculate range of empty list")
        return max(numbers) - min(numbers)

    @staticmethod
    def sum(numbers: list[float]) -> float:
        """Calculate sum of numbers"""
        if not numbers:
            raise ValueError("Cannot calculate sum of empty list")
        return sum(numbers)

    @staticmethod
    def count(numbers: list[float]) -> int:
        """Count the number of elements"""
        return len(numbers)

    @staticmethod
    def min(numbers: list[float]) -> float:
        """Find minimum value"""
        if not numbers:
            raise ValueError("Cannot find minimum of empty list")
        return min(numbers)

    @staticmethod
    def max(numbers: list[float]) -> float:
        """Find maximum value"""
        if not numbers:
            raise ValueError("Cannot find maximum of empty list")
        return max(numbers)
