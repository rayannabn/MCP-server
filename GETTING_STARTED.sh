#!/bin/bash

# 🎯 MCP Calculator - Getting Started Guide
# This file provides a quick reference for getting the application running

cat << 'EOF'

╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║           🚀 MCP CALCULATOR - QUICK START REFERENCE                   ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝

📋 CONTENTS:
  1. Prerequisites
  2. Installation
  3. Testing
  4. Running the Application
  5. Using the Calculator
  6. Troubleshooting
  7. Additional Resources

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  PREREQUISITES

   ✓ Python 3.8 or higher
   ✓ OpenAI API key (already provided)
   ✓ Internet connection
   ✓ pip package manager

   Check Python version:
   $ python --version

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣  INSTALLATION (First Time Only)

   Step 1: Navigate to project directory
   $ cd /workspaces/MCP-server

   Step 2: Install dependencies
   $ pip install -r requirements.txt

   Step 3: Verify installation
   $ python -c "import openai, streamlit; print('✅ Dependencies installed')"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣  TESTING (Verify Everything Works)

   Test 1: Test Calculator Functions
   $ python test_calculator.py

   Expected Output:
   ✅ All tests passed! MCP Server is working correctly.

   Test 2: Test OpenAI Integration (Optional)
   $ python test_integration.py

   Note: May fail with quota error - that's normal with test API keys

   Test 3: View Usage Examples
   $ python examples.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4️⃣  RUNNING THE APPLICATION

   Option A: Using the Startup Script (Recommended)
   $ ./start.sh

   Option B: Direct Streamlit Command
   $ streamlit run ui/app.py

   Option C: Custom Port
   $ streamlit run ui/app.py --server.port 9000

   The application will open at:
   → http://localhost:8501

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5️⃣  USING THE CALCULATOR

   Once the application is running, you can:

   a) Enter a Query
      • Click on the input field
      • Type your mathematical question
      • Example: "What is 25 plus 17?"

   b) Get Result
      • Click "Calculate" button
      • Wait for processing (1-3 seconds)
      • View the result with details

   c) View History
      • Scroll down to see previous calculations
      • Click on any calculation for details
      • Use trash icon to clear history

   d) Reference Tools
      • Expand "Available Tools Reference" section
      • See all 16 calculator tools
      • Understand their parameters

   EXAMPLE QUERIES TO TRY:

   Basic Arithmetic:
   • "What is 25 plus 17?"
   • "Calculate 100 divided by 4"
   • "Multiply 15 by 8"

   Advanced Operations:
   • "What's the square root of 144?"
   • "Calculate 15% of 200"
   • "What's 5 factorial?"

   Scientific:
   • "Calculate sine of π/2"
   • "Log base 10 of 1000"
   • "2 to the power of 10"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6️⃣  TROUBLESHOOTING

   Problem: "ModuleNotFoundError: No module named 'openai'"
   Solution: Run "pip install -r requirements.txt"

   Problem: "Port 8501 already in use"
   Solution: Run "streamlit run ui/app.py --server.port 8502"

   Problem: "OPENAI_API_KEY environment variable is not set"
   Solution: Check that .env file exists with API key

   Problem: "OpenAI API error: insufficient_quota"
   Solution: Check your OpenAI account billing/quota at:
            https://platform.openai.com/account/billing/overview

   Problem: "API response parsing error"
   Solution: Try upgrading OpenAI: pip install --upgrade openai

   Problem: Application not responding
   Solution: Check internet connection and firewall settings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7️⃣  ADDITIONAL RESOURCES

   📖 Documentation Files:
   • README.md              - Complete feature documentation
   • QUICKSTART.md          - Quick start guide
   • ARCHITECTURE.md        - System architecture & diagrams
   • DEPLOYMENT_INFO.py     - Detailed deployment info
   • PROJECT_SUMMARY.md     - Project completion summary

   📝 Code Examples:
   • examples.py            - Usage examples

   🧪 Testing:
   • test_calculator.py     - Unit tests
   • test_integration.py    - Integration tests

   📚 External Resources:
   • OpenAI Docs:    https://platform.openai.com/docs
   • Streamlit Docs: https://docs.streamlit.io
   • Python Math:    https://docs.python.org/3/library/math.html

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TYPICAL WORKFLOW

   1. Install dependencies (first time):
      $ pip install -r requirements.txt

   2. Test calculator:
      $ python test_calculator.py

   3. Start application:
      $ ./start.sh

   4. Open browser to http://localhost:8501

   5. Enter your mathematical query

   6. View result and continue

   7. Stop application with Ctrl+C

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ QUICK COMMANDS REFERENCE

   # Navigation
   cd /workspaces/MCP-server

   # Installation
   pip install -r requirements.txt

   # Testing
   python test_calculator.py
   python test_integration.py
   python examples.py

   # Running
   ./start.sh
   streamlit run ui/app.py

   # System Info
   python DEPLOYMENT_INFO.py

   # Utilities
   python --version
   pip list | grep openai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎉 YOU'RE ALL SET!

   To get started right now:

   $ cd /workspaces/MCP-server
   $ ./start.sh

   Then open: http://localhost:8501

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Questions? Check the documentation files or run:
$ python DEPLOYMENT_INFO.py

═════════════════════════════════════════════════════════════════════════

EOF
