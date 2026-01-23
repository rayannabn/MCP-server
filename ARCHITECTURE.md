# 📊 MCP Calculator - Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web UI (ui/app.py)              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  User Query Input (Natural Language)                │   │
│  │  e.g., "What is 25 plus 17?"                       │   │
│  └──────────────────┬───────────────────────────────────┘   │
└─────────────────────┼───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│        OpenAI Integration (integration/openai_integration.py)│
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Query sent to OpenAI GPT-4 Mini with:              │   │
│  │  • Available tools (add, subtract, multiply, etc.)   │   │
│  │  • System prompt (instructions)                      │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                    │                                         │
│                    ▼                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  OpenAI Response: {"tool_name": "add",               │   │
│  │                    "parameters": {"a": 25, "b": 17}} │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                    │                                         │
│                    ▼                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Parse response and extract tool call               │   │
│  └──────────────────┬───────────────────────────────────┘   │
└─────────────────────┼───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│         MCP Server (mcp_server/server.py)                    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  CalculatorServer.execute_tool("add",                │   │
│  │                   a=25, b=17)                        │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                    │                                         │
│         ┌──────────┴──────────┬──────────┬─────────────┐    │
│         ▼                     ▼          ▼             ▼    │
│    add() function,    multiply(),   divide(),   power()    │
│    subtract(),        square_root(), percentage(),         │
│    and 9 more tools...                                     │
│         │                                                   │
│         └──────────────────┬──────────────────────────────┘ │
│                            ▼                                │
│                    Return Result: 42                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web UI (Result)                │
│                                                              │
│  ✅ Success!                                                │
│  📊 Result: 42                                              │
│  🔧 Tool Used: add                                          │
│  📝 Explanation: Adding 25 and 17                          │
│                                                              │
│  [Query History]  [Clear History]                          │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

```
User Input (String)
    ↓
[Streamlit UI]
    ↓
[CalculatorAI.process_query()]
    ↓
[OpenAI API Call]
    ↓
[JSON Response Parsing]
    ↓
[CalculatorServer.execute_tool()]
    ↓
[Calculation Result]
    ↓
[Format Response]
    ↓
[Display in Streamlit]
```

## Component Interaction

```
┌─────────────────────────────────────────────────────────┐
│                  Application Layer                       │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Streamlit (ui/app.py)                           │  │
│  │  • Web interface                                  │  │
│  │  • User input/output                             │  │
│  │  • History management                            │  │
│  └──────────────────┬────────────────────────────────┘  │
└─────────────────────┼──────────────────────────────────┘
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
┌──────────────────┐      ┌────────────────────┐
│  Integration     │      │  Configuration     │
│  (config.py)     │      │  (config.py)       │
│                  │      │  (.env file)       │
│  Bridges OpenAI  │      │  API keys          │
│  with Calculator │      │  Settings          │
└────────┬─────────┘      └────────────────────┘
         │
         ▼
┌──────────────────────────────────────────┐
│    OpenAI Integration Layer               │
│  ┌──────────────────────────────────┐   │
│  │  CalculatorAI                    │   │
│  │  • Query interpretation          │   │
│  │  • Tool selection                │   │
│  │  • Response parsing              │   │
│  │  • Conversation history          │   │
│  └──────────────┬───────────────────┘   │
└─────────────────┼──────────────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
    ┌────────────┐   ┌──────────────┐
    │ OpenAI API │   │ Calculator   │
    │   (Cloud)  │   │   Server     │
    └────────────┘   │ (Local)      │
                     └──────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         ┌─────────┐ ┌──────────┐ ┌────────────┐
         │Arithmetic│ │Advanced   │ │Trigonometry│
         │Tools     │ │Tools      │ │ & Logs    │
         └─────────┘ └──────────┘ └────────────┘
```

## Tool Execution Flow

```
Input: "What is 25 plus 17?"
   │
   ▼
[OpenAI Interpretation]
   │
   ├─ Identifies: Addition operation
   ├─ Extracts: a=25, b=17
   └─ Selects Tool: "add"
   │
   ▼
[Tool Call JSON]
{
  "tool_name": "add",
  "parameters": {"a": 25, "b": 17},
  "explanation": "Adding 25 and 17"
}
   │
   ▼
[CalculatorServer Execution]
   │
   ├─ Validation: Parameters valid? ✓
   ├─ Execution: add(25, 17)
   └─ Result: 42
   │
   ▼
[Formatted Response]
{
  "success": true,
  "result": 42,
  "tool_used": "add",
  "parameters": {"a": 25, "b": 17},
  "explanation": "Adding 25 and 17"
}
   │
   ▼
[Display in UI]
✅ Result: 42
```

## Error Handling Flow

```
Invalid Input: "What is 5 divided by 0?"
   │
   ▼
[OpenAI Processing]
   │ Recognizes: Division by zero
   └─ Attempts: divide(5, 0)
   │
   ▼
[MCP Server Validation]
   │ Check: b == 0?
   └─ Result: True - ERROR
   │
   ▼
[Exception Handling]
   │ Catch: ValueError
   ├─ Message: "Cannot divide by zero"
   └─ Return: {"success": false, "error": "..."}
   │
   ▼
[User Feedback]
❌ Error: Cannot divide by zero
```

## Supported Operations Summary

```
┌──────────────────┬──────────────────┬──────────────────┐
│   Arithmetic     │    Advanced      │   Specialized    │
├──────────────────┼──────────────────┼──────────────────┤
│ add(a, b)        │ power(a, b)      │ sin(a)           │
│ subtract(a, b)   │ square_root(a)   │ cos(a)           │
│ multiply(a, b)   │ percentage(a, b) │ tan(a)           │
│ divide(a, b)     │ absolute(a)      │ log(a)           │
│                  │ factorial(a)     │ ln(a)            │
│                  │ ceiling(a)       │                  │
│                  │ floor(a)         │                  │
└──────────────────┴──────────────────┴──────────────────┘
```

## Request/Response Examples

### Example 1: Simple Addition
```
Input:   "What is 25 plus 17?"
Process: OpenAI → add(25, 17) → 42
Output:  ✅ Result: 42
```

### Example 2: Advanced Calculation
```
Input:   "Calculate sine of π/2"
Process: OpenAI → sin(1.5708) → 1.0
Output:  ✅ Result: 1.0
```

### Example 3: Error Case
```
Input:   "What's square root of -4?"
Process: OpenAI → square_root(-4) → ERROR
Output:  ❌ Cannot take square root of negative number
```

## Performance Characteristics

```
Query → Processing → Result
  ↓        1-3 sec      ↓
Input    (OpenAI       Output
Text     Latency)      JSON
  │                      │
  └─ 50-100 tokens       └─ 20-50 tokens
     (on average)           (on average)
```

## Security Model

```
┌─────────────────────────────┐
│    Secure API Key Storage    │
│  (Environment Variables)     │
└──────────────┬───────────────┘
               │
               ├─ .env file (development)
               ├─ Environment variables (production)
               └─ Secret management (deployment)
               │
               ▼
    ┌──────────────────────────┐
    │   OpenAI API Key         │
    │   (Encrypted in transit) │
    └──────────────────────────┘
```

## Deployment Architecture

```
┌──────────────────────────────────────────┐
│         Development Environment          │
├──────────────────────────────────────────┤
│ Streamlit (Local)    [Port 8501]        │
│ ↓                                        │
│ CalculatorAI         [Local Instance]   │
│ ↓                                        │
│ CalculatorServer     [Local Instance]   │
│ ↓                                        │
│ OpenAI API           [Cloud Service]    │
└──────────────────────────────────────────┘

                   OR

┌──────────────────────────────────────────┐
│      Production Environment              │
├──────────────────────────────────────────┤
│ Streamlit Cloud/Docker [Port 8501]      │
│ ↓                                        │
│ CalculatorAI         [Container/Server] │
│ ↓                                        │
│ CalculatorServer     [Container/Server] │
│ ↓                                        │
│ OpenAI API           [Cloud Service]    │
│                                          │
│ Load Balancer (if needed)               │
│ Rate Limiter (recommended)              │
│ Monitoring & Logging (recommended)      │
└──────────────────────────────────────────┘
```

---

**For detailed implementation, see the Python source files in the repository.**
