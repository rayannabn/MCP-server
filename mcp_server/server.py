"""
MCP Server for Calculator Operations
Provides tools for basic and advanced mathematical operations
"""

import json
import math
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
