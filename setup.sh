#!/bin/bash

# AI Quantitative Trading System - Setup Script
# Author: Rahul Yatagiri

echo "=========================================="
echo "AI Quantitative Trading System Setup"
echo "=========================================="
echo ""

# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    echo "Poetry installed successfully!"
else
    echo "✓ Poetry is already installed"
fi

echo ""
echo "Installing project dependencies..."
poetry install

echo ""
echo "Setting up environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file from .env.example"
    echo ""
    echo "⚠️  IMPORTANT: Please edit the .env file and add your API keys:"
    echo "   - OPENAI_API_KEY (required for LLM functionality)"
    echo "   - FINANCIAL_DATASETS_API_KEY (optional, for extended ticker support)"
    echo "   - Other LLM provider keys (optional, based on your preference)"
else
    echo "✓ .env file already exists"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Run the system:"
echo "   poetry run python src/main.py --ticker AAPL,MSFT,NVDA"
echo ""
echo "For more information, see README.md"
echo ""
