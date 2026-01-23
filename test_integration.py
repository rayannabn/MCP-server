#!/usr/bin/env python
"""
Test the OpenAI Integration with MCP Calculator
This script tests that OpenAI can properly interpret queries and call the right tools
"""

import os
from dotenv import load_dotenv
from integration.openai_integration import CalculatorAI

def test_openai_integration():
    """Test OpenAI integration with sample queries"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not set in .env file")
        return False
    
    print("=" * 60)
    print("🤖 OpenAI Integration Test")
    print("=" * 60)
    print(f"\n✅ API Key loaded (length: {len(api_key)})")
    
    # Initialize the calculator AI
    calculator = CalculatorAI(api_key)
    print("✅ CalculatorAI initialized")
    
    # Test queries
    test_queries = [
        "What is 10 plus 5?",
        "Calculate 100 divided by 4",
        "What's the square root of 144?",
    ]
    
    print("\n" + "-" * 60)
    print("Testing sample queries:")
    print("-" * 60)
    
    for query in test_queries:
        print(f"\n📝 Query: {query}")
        try:
            result = calculator.process_query(query)
            
            if result.get("success"):
                print(f"✅ Success!")
                if result.get("result"):
                    print(f"   Result: {result['result']}")
                if result.get("tool_used"):
                    print(f"   Tool: {result['tool_used']}")
                if result.get("explanation"):
                    print(f"   Explanation: {result['explanation']}")
            else:
                print(f"⚠️  {result.get('error', 'Unknown error')}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 60)
    print("✅ Integration test completed!")
    print("=" * 60)

if __name__ == "__main__":
    test_openai_integration()
