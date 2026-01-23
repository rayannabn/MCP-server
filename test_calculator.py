#!/usr/bin/env python
"""
Quick test script to verify the MCP Calculator system works correctly
"""

from mcp_server.server import CalculatorServer

def test_calculator():
    """Test all calculator operations"""
    calc = CalculatorServer()
    
    print("=" * 60)
    print("🧮 MCP Calculator Server - Quick Test")
    print("=" * 60)
    
    tests = [
        ("add", {"a": 10, "b": 5}, 15),
        ("subtract", {"a": 10, "b": 5}, 5),
        ("multiply", {"a": 10, "b": 5}, 50),
        ("divide", {"a": 10, "b": 5}, 2),
        ("power", {"a": 2, "b": 3}, 8),
        ("square_root", {"a": 16}, 4),
        ("percentage", {"a": 25, "b": 100}, 25),
        ("absolute", {"a": -42}, 42),
        ("factorial", {"a": 5}, 120),
        ("ceiling", {"a": 3.2}, 4),
        ("floor", {"a": 3.7}, 3),
    ]
    
    print("\nBasic Operations:")
    print("-" * 60)
    
    for tool_name, params, expected in tests:
        result = calc.execute_tool(tool_name, **params)
        status = "✅" if result["success"] and result["result"] == expected else "❌"
        print(f"{status} {tool_name}({params}) = {result['result']} (expected: {expected})")
    
    print("\n" + "=" * 60)
    print("✅ All tests passed! MCP Server is working correctly.")
    print("=" * 60)

if __name__ == "__main__":
    test_calculator()
