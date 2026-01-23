"""
Example script showing how to use the MCP Calculator programmatically
"""

import os
from dotenv import load_dotenv
from mcp_server.server import CalculatorServer
from integration.openai_integration import CalculatorAI


def example_direct_calculator():
    """Example: Using calculator directly without OpenAI"""
    print("=" * 60)
    print("Example 1: Direct Calculator Usage")
    print("=" * 60)
    
    calc = CalculatorServer()
    
    # Direct tool execution
    result1 = calc.execute_tool("add", a=10, b=20)
    print(f"10 + 20 = {result1['result']}")
    
    result2 = calc.execute_tool("power", a=2, b=8)
    print(f"2 ^ 8 = {result2['result']}")
    
    result3 = calc.execute_tool("square_root", a=144)
    print(f"√144 = {result3['result']}")


def example_openai_integration():
    """Example: Using OpenAI integration"""
    print("\n" + "=" * 60)
    print("Example 2: OpenAI Integration")
    print("=" * 60)
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ API key not found. Set OPENAI_API_KEY in .env")
        return
    
    calculator = CalculatorAI(api_key)
    
    # Process natural language query
    print("\nQuery: What is 100 divided by 4?")
    print("Processing...")
    
    try:
        result = calculator.process_query("What is 100 divided by 4?")
        
        if result.get("success"):
            print(f"✅ Result: {result['result']}")
            print(f"   Tool used: {result.get('tool_used')}")
            print(f"   Explanation: {result.get('explanation')}")
        else:
            print(f"❌ Error: {result.get('error')}")
    except Exception as e:
        print(f"⚠️  API error (quota issue?): {str(e)[:100]}")


def example_get_available_tools():
    """Example: View available tools"""
    print("\n" + "=" * 60)
    print("Example 3: Available Tools")
    print("=" * 60)
    
    calc = CalculatorServer()
    tools = calc.get_tools()
    
    print(f"\nTotal available tools: {len(tools)}\n")
    
    for tool in tools[:5]:  # Show first 5
        print(f"• {tool['name']}: {tool['description']}")
    
    print(f"... and {len(tools) - 5} more")


def example_error_handling():
    """Example: Error handling"""
    print("\n" + "=" * 60)
    print("Example 4: Error Handling")
    print("=" * 60)
    
    calc = CalculatorServer()
    
    # Division by zero
    result = calc.execute_tool("divide", a=10, b=0)
    print(f"10 / 0: {result}")
    
    # Negative square root
    result = calc.execute_tool("square_root", a=-4)
    print(f"√-4: {result}")


if __name__ == "__main__":
    print("\n🧮 MCP Calculator - Usage Examples\n")
    
    example_direct_calculator()
    example_get_available_tools()
    example_error_handling()
    example_openai_integration()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
