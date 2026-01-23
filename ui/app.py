"""
Streamlit UI for Calculator with OpenAI Integration
Provides a user-friendly interface for mathematical queries
"""

import os
import sys
import json
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.openai_integration import CalculatorAI


def initialize_session():
    """Initialize session state"""
    if "calculator_ai" not in st.session_state:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("❌ OpenAI API Key not found. Please set OPENAI_API_KEY environment variable.")
            st.stop()
        st.session_state.calculator_ai = CalculatorAI(api_key)

    if "history" not in st.session_state:
        st.session_state.history = []


def display_header():
    """Display application header"""
    st.set_page_config(
        page_title="AI Calculator", page_icon="🧮", layout="wide"
    )
    st.title("🧮 AI-Powered Calculator")
    st.markdown(
        """
    Ask me to perform any mathematical calculation! I understand natural language queries
    and use MCP tools to provide accurate results.
    
    Examples: "What is 25 plus 17?", "Calculate sine of π/2", "What's 15% of 200?"
    """
    )


def display_calculator_section():
    """Display calculator input section"""
    st.header("📝 Enter Your Query")

    col1, col2 = st.columns([4, 1])

    with col1:
        user_query = st.text_input(
            "Your mathematical question:",
            placeholder="e.g., What is 42 divided by 7?",
            label_visibility="collapsed",
        )

    with col2:
        calculate_button = st.button("🔍 Calculate", type="primary")

    if calculate_button and user_query.strip():
        with st.spinner("🤔 Processing your query..."):
            result = st.session_state.calculator_ai.process_query(
                user_query
            )

        # Add to history
        st.session_state.history.insert(0, {"query": user_query, "result": result})

        # Display result
        display_result(result)

    return user_query


def display_result(result: dict):
    """Display calculation result"""
    if result.get("success"):
        st.success("✅ Calculation completed!")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("### 📊 Result")
            if "result" in result:
                result_value = result["result"]
                if isinstance(result_value, float):
                    st.metric("Answer", f"{result_value:.4g}")
                else:
                    st.metric("Answer", result_value)

        with col2:
            st.markdown("### 📋 Details")
            if result.get("tool_used"):
                st.write(f"**Tool Used:** `{result['tool_used']}`")
                st.write(f"**Explanation:** {result.get('explanation', 'N/A')}")
                if result.get("parameters"):
                    st.write(
                        f"**Parameters:** {json.dumps(result['parameters'])}"
                    )
            else:
                st.write(result.get("result", "No result"))

    else:
        st.error(f"❌ Error: {result.get('error', 'Unknown error')}")
        if result.get("ai_response"):
            with st.expander("View AI Response"):
                st.write(result["ai_response"])


def display_history():
    """Display query history"""
    if st.session_state.history:
        st.header("📚 Query History")

        # Controls
        col1, col2 = st.columns([4, 1])
        with col2:
            if st.button("🗑️ Clear History"):
                st.session_state.history = []
                st.rerun()

        # Display history items
        for idx, item in enumerate(st.session_state.history):
            with st.expander(
                f"Query {idx + 1}: {item['query'][:50]}...",
                expanded=False,
            ):
                result = item["result"]

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Query:**")
                    st.write(item["query"])

                with col2:
                    st.write("**Status:**")
                    if result.get("success"):
                        st.success("✅ Success")
                    else:
                        st.error("❌ Failed")

                if result.get("tool_used"):
                    st.write(f"**Tool:** `{result['tool_used']}`")

                if "result" in result:
                    if isinstance(result["result"], (int, float)):
                        st.write(
                            f"**Result:** `{result['result']:.4g}`"
                        )
                    else:
                        st.write(f"**Result:** `{result['result']}`")


def display_tools_reference():
    """Display available tools reference"""
    with st.expander("📖 Available Tools Reference"):
        st.markdown("""
        **Basic Operations:**
        - `add(a, b)` - Add two numbers
        - `subtract(a, b)` - Subtract two numbers
        - `multiply(a, b)` - Multiply two numbers
        - `divide(a, b)` - Divide two numbers
        
        **Advanced Operations:**
        - `power(a, b)` - Raise a to power b
        - `square_root(a)` - Calculate square root
        - `percentage(a, b)` - Calculate a/b as percentage
        - `absolute(a)` - Get absolute value
        - `factorial(a)` - Calculate factorial
        
        **Trigonometric Functions:**
        - `sin(a)` - Sine (radians)
        - `cos(a)` - Cosine (radians)
        - `tan(a)` - Tangent (radians)
        
        **Logarithmic Functions:**
        - `log(a)` - Log base 10
        - `ln(a)` - Natural logarithm
        
        **Rounding Functions:**
        - `ceiling(a)` - Round up
        - `floor(a)` - Round down
        """)


def main():
    """Main application function"""
    display_header()
    initialize_session()

    # Main calculator section
    display_calculator_section()

    # Divider
    st.divider()

    # History section
    display_history()

    # Reference section
    display_tools_reference()

    # Footer
    st.divider()
    st.markdown(
        """
    <div style='text-align: center; color: #888; margin-top: 2rem;'>
        Powered by OpenAI & MCP Calculator Server | v1.0
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
