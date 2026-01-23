#!/bin/bash

# Startup script for MCP Calculator Application
# This script sets up the environment and starts the Streamlit UI

echo "======================================"
echo "🧮 AI Calculator with MCP Server"
echo "======================================"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found"
    echo "Please create .env with your OpenAI API key:"
    echo "OPENAI_API_KEY=your_key_here"
    exit 1
fi

# Check if dependencies are installed
echo "Checking dependencies..."
python -c "import openai, streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "✅ Starting MCP Calculator Application..."
echo ""
echo "🌐 Streamlit UI will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Streamlit application
streamlit run ui/app.py
