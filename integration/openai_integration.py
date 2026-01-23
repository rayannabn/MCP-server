"""
OpenAI Integration Module
Handles communication with OpenAI API to interpret user queries
and call appropriate MCP calculator tools
"""

import json
import re
from typing import Any, Optional

from openai import OpenAI

from mcp_server.server import CalculatorServer


class CalculatorAI:
    """Integrates OpenAI with MCP Calculator Server"""

    def __init__(self, api_key: str):
        """Initialize OpenAI client and calculator server"""
        self.client = OpenAI(api_key=api_key)
        self.calculator = CalculatorServer()
        self.model = "gpt-4o-mini"  # Using efficient model
        self.conversation_history = []

    def get_system_prompt(self) -> str:
        """Get system prompt for the AI"""
        tools_description = self._format_tools_for_prompt()
        return f"""You are a helpful calculator assistant. Your role is to:
1. Understand mathematical queries from the user
2. Identify which calculator tools to use
3. Extract the necessary parameters
4. Return the result in a clear, human-readable format

Available Calculator Tools:
{tools_description}

When you identify that a calculation is needed:
1. Determine which tool(s) to use
2. Extract the required parameters from the query
3. Format your response as JSON with the following structure:
{{
    "tool_name": "name_of_tool",
    "parameters": {{"a": value, "b": value}},
    "explanation": "Brief explanation of what calculation you're doing"
}}

If the query requires multiple steps, break it down and use appropriate tools sequentially.
Always respond with clear explanations of your calculations."""

    def _format_tools_for_prompt(self) -> str:
        """Format available tools for the system prompt"""
        tools = self.calculator.get_tools()
        formatted = ""
        for tool in tools:
            params = ", ".join(tool["inputSchema"]["properties"].keys())
            formatted += f"- {tool['name']}({params}): {tool['description']}\n"
        return formatted

    def process_query(self, user_query: str) -> dict[str, Any]:
        """Process user query and execute appropriate calculator tool"""
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_query})

        try:
            # Call OpenAI to interpret query and generate tool call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.get_system_prompt()},
                    *self.conversation_history,
                ],
                temperature=0.7,
                max_tokens=500,
            )

            assistant_message = response.choices[0].message.content
            self.conversation_history.append(
                {"role": "assistant", "content": assistant_message}
            )

            # Parse the response to extract tool calls
            result = self._parse_and_execute_tools(
                assistant_message, user_query
            )

            return result

        except Exception as e:
            return {
                "success": False,
                "error": f"Error processing query: {str(e)}",
                "query": user_query,
            }

    def _parse_and_execute_tools(
        self, assistant_response: str, original_query: str
    ) -> dict[str, Any]:
        """Parse assistant response and execute calculator tools"""
        try:
            # Try to find JSON in the response
            json_match = re.search(
                r"\{[\s\S]*\}", assistant_response
            )

            if json_match:
                tool_call = json.loads(json_match.group())
                tool_name = tool_call.get("tool_name")
                parameters = tool_call.get("parameters", {})
                explanation = tool_call.get("explanation", "")

                # Execute the tool
                execution_result = self.calculator.execute_tool(
                    tool_name, **parameters
                )

                if execution_result.get("success", False):
                    return {
                        "success": True,
                        "query": original_query,
                        "tool_used": tool_name,
                        "parameters": parameters,
                        "explanation": explanation,
                        "result": execution_result["result"],
                        "ai_response": assistant_response,
                    }
                else:
                    return {
                        "success": False,
                        "query": original_query,
                        "error": execution_result.get("error", "Unknown error"),
                        "ai_response": assistant_response,
                    }
            else:
                # If no JSON found, return the raw response
                return {
                    "success": True,
                    "query": original_query,
                    "result": assistant_response,
                    "ai_response": assistant_response,
                    "note": "Response generated without tool execution",
                }

        except json.JSONDecodeError:
            return {
                "success": True,
                "query": original_query,
                "result": assistant_response,
                "ai_response": assistant_response,
                "note": "Response provided without structured tool call",
            }

    def clear_history(self) -> None:
        """Clear conversation history"""
        self.conversation_history = []
