# codesage-ai
AI agent that reviews GitHub code automatically using LangChain and GPT-4

# 🤖 CodeSage - AI Code Review Agent

An intelligent AI agent that automatically reviews GitHub repositories and provides detailed feedback on code quality, security issues, and improvements.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🔍 **Automatic Code Analysis** - Reviews any public GitHub repository
- 🔒 **Security Scanning** - Identifies potential vulnerabilities
- 📊 **Quality Assessment** - Rates code quality and structure
- 💡 **Smart Suggestions** - Provides actionable improvements
- 📝 **Detailed Reports** - Generates comprehensive reports

## 🚀 Quick Demo

```python
# Review any GitHub repository
await review_code_simple("https://github.com/pallets/flask")

Sample Output:


📥 Downloading code...
✓ Found 15 files

🤖 Analyzing...

============================================================
1. WHAT IT DOES:
Flask is a lightweight web framework for Python...

2. GOOD THINGS:
✓ Clean, modular code structure
✓ Well-documented functions

3. PROBLEMS FOUND:
⚠ Missing error handling in some functions
⚠ Some hardcoded values should be in config

4. TOP 3 IMPROVEMENTS:
1. Add comprehensive error handling
2. Implement type hints
3. Add more unit tests
============================================================

✓ Review saved to code_review.txt
