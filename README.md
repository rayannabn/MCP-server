# 🧮 AI Calculator with MCP Server

A sophisticated calculator application that leverages OpenAI's language model with MCP (Model Context Protocol) server architecture to understand natural language mathematical queries and execute precise calculations.

## 🌟 Features

- **Natural Language Processing**: Ask questions in plain English like "What's 25 plus 17?" or "Calculate sine of π/2"
- **16 Mathematical Tools**: Basic operations, trigonometry, logarithms, and more
- **MCP Server Architecture**: Clean separation of concerns with dedicated calculator tools
- **OpenAI Integration**: Uses OpenAI's GPT-4 Mini model to interpret queries accurately
- **Streamlit UI**: User-friendly web interface for entering queries and viewing results
- **Query History**: Keep track of all calculations in your session
- **Real-time Processing**: Instant feedback with detailed calculation breakdowns

## 📋 Available Tools

### Basic Operations
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers

### Advanced Operations
- `power(a, b)` - Raise a to power b
- `square_root(a)` - Calculate square root
- `percentage(a, b)` - Calculate a/b as percentage
- `absolute(a)` - Get absolute value
- `factorial(a)` - Calculate factorial

### Trigonometric Functions
- `sin(a)` - Sine (radians)
- `cos(a)` - Cosine (radians)
- `tan(a)` - Tangent (radians)

### Logarithmic Functions
- `log(a)` - Log base 10
- `ln(a)` - Natural logarithm

### Rounding Functions
- `ceiling(a)` - Round up
- `floor(a)` - Round down

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Installation Steps

1. **Clone the repository**
   ```bash
   cd /workspaces/MCP-server
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   The `.env` file is already configured with your API key. Ensure it contains:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 📁 Project Structure

```
MCP-server/
├── mcp_server/
│   ├── __init__.py
│   └── server.py           # MCP Calculator Server with 16 tools
├── integration/
│   ├── __init__.py
│   └── openai_integration.py  # OpenAI integration module
├── ui/
│   ├── __init__.py
│   └── app.py              # Streamlit UI application
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .streamlit/config.toml  # Streamlit configuration
└── README.md              # This file
```

## 🎯 How It Works

1. **User Input**: You enter a mathematical query in natural language
2. **OpenAI Processing**: The query is sent to OpenAI GPT-4 Mini
3. **Query Interpretation**: OpenAI identifies the appropriate calculator tool(s)
4. **Tool Execution**: The MCP server executes the calculator operation
5. **Result Display**: The answer is displayed with full calculation details

### Example Flow
```
User Query: "What is 42 divided by 7?"
   ↓
OpenAI: Interprets as divide(42, 7)
   ↓
MCP Server: Executes division operation
   ↓
Result: 6.0
```

## 🏃 Running the Application

### Start the Streamlit UI
```bash
streamlit run ui/app.py
```

The application will open in your default browser at `http://localhost:8501`

### Example Queries
- "What is 25 plus 17?"
- "Calculate 15% of 200"
- "What's the square root of 144?"
- "Calculate sine of π divided by 2"
- "What's 5 factorial?"
- "Log base 10 of 100"
- "Multiply 123 by 456"

## 🔧 Architecture

### MCP Server (`mcp_server/server.py`)
- **CalculatorServer**: Main class that implements all calculator operations
- **get_tools()**: Returns list of available tools with JSON schemas
- **execute_tool()**: Executes any calculator operation safely
- 16 static methods for different mathematical operations

### OpenAI Integration (`integration/openai_integration.py`)
- **CalculatorAI**: Main integration class
- Maintains conversation history for context
- Parses OpenAI responses to extract tool calls
- Automatically executes identified tools
- Returns structured results with explanations

### Streamlit UI (`ui/app.py`)
- Responsive interface with real-time processing
- Query history tracking
- Tool reference guide
- Error handling and user feedback
- Professional styling and layout

## 🛡️ Error Handling

The application includes robust error handling for:
- Division by zero
- Negative square roots
- Invalid logarithm inputs
- Negative factorials
- API failures
- Invalid tool usage

## 📊 Response Structure

Success response:
```json
{
  "success": true,
  "query": "user's original query",
  "tool_used": "calculator_tool_name",
  "parameters": {"a": value, "b": value},
  "explanation": "what calculation was performed",
  "result": 42.0
}
```

Error response:
```json
{
  "success": false,
  "query": "user's original query",
  "error": "description of what went wrong"
}
```

## 🔐 Security Notes

- Keep your `.env` file secure and never commit it to version control
- The API key in `.env` should be treated as confidential
- Consider using Streamlit secrets management for production deployments

## 🧪 Testing

The system is designed to handle:
- Complex multi-step calculations
- Trigonometric functions with radian inputs
- Large numbers and factorials
- Floating-point arithmetic
- Error cases with helpful messages

## 📝 Example Use Cases

- **Educational**: Learn mathematics with instant feedback
- **Quick Calculations**: Fast answers to mathematical questions
- **Scientific Computing**: Trigonometric and logarithmic calculations
- **Percentage Calculations**: Business and financial applications
- **Engineering**: Complex calculations with detailed breakdowns

## 🎨 Customization

You can customize:
- Available calculator tools in `mcp_server/server.py`
- AI model in `integration/openai_integration.py` (change `self.model`)
- UI styling in `.streamlit/config.toml`
- System prompt in `CalculatorAI.get_system_prompt()`

## 🐛 Troubleshooting

### API Key Issues
```
Error: OPENAI_API_KEY environment variable is not set
Solution: Add OPENAI_API_KEY to .env file
```

### Module Not Found
```
Error: ModuleNotFoundError: No module named 'openai'
Solution: Run: pip install -r requirements.txt
```

### Port Already in Use
```
Error: Address already in use
Solution: streamlit run ui/app.py --server.port 8502
```

## 📦 Dependencies

- **openai** (1.3.0): OpenAI API client
- **streamlit** (1.28.0): Web UI framework
- **python-dotenv** (1.0.0): Environment variable management

## 🚢 Production Deployment

For production use:
1. Use environment variables instead of `.env` file
2. Implement rate limiting
3. Add request logging and monitoring
4. Use Streamlit Cloud or Docker for deployment
5. Secure your API key with proper secret management

## 📄 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Development

To extend the calculator with new tools:
1. Add a new static method to `CalculatorServer` class
2. Add the tool definition to `get_tools()` method
3. The system will automatically make it available

## 🤝 Support

For issues or questions about the MCP Server Calculator:
- Review the error messages carefully
- Check the tools reference in the Streamlit UI
- Ensure all dependencies are installed correctly

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Status**: Production Ready ✅