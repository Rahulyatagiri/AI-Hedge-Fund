# AI-Powered Quantitative Trading System

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-active-success)]()
[![LangChain](https://img.shields.io/badge/LangChain-0.3.7-blue)](https://langchain.com/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An advanced AI-driven quantitative trading system that leverages multiple expert agents to analyze markets and make informed trading decisions. This project combines modern AI techniques with traditional investment philosophies to create a comprehensive market analysis framework.

**Note:** This is a research and educational project designed to explore the intersection of artificial intelligence and quantitative finance. Not intended for actual trading or investment purposes.

This system employs several agents working together:

1. Aswath Damodaran Agent - The Dean of Valuation, focuses on story, numbers, and disciplined valuation
2. Ben Graham Agent - The godfather of value investing, only buys hidden gems with a margin of safety
3. Bill Ackman Agent - An activist investor, takes bold positions and pushes for change
4. Cathie Wood Agent - The queen of growth investing, believes in the power of innovation and disruption
5. Charlie Munger Agent - Warren Buffett's partner, only buys wonderful businesses at fair prices
6. Michael Burry Agent - The Big Short contrarian who hunts for deep value
7. Mohnish Pabrai Agent - The Dhandho investor, who looks for doubles at low risk
8. Peter Lynch Agent - Practical investor who seeks "ten-baggers" in everyday businesses
9. Phil Fisher Agent - Meticulous growth investor who uses deep "scuttlebutt" research 
10. Rakesh Jhunjhunwala Agent - The Big Bull of India
11. Stanley Druckenmiller Agent - Macro legend who hunts for asymmetric opportunities with growth potential
12. Warren Buffett Agent - The oracle of Omaha, seeks wonderful companies at a fair price
13. Valuation Agent - Calculates the intrinsic value of a stock and generates trading signals
14. Sentiment Agent - Analyzes market sentiment and generates trading signals
15. Fundamentals Agent - Analyzes fundamental data and generates trading signals
16. Technicals Agent - Analyzes technical indicators and generates trading signals
17. Risk Manager - Calculates risk metrics and sets position limits
18. Portfolio Manager - Makes final trading decisions and generates orders

<img width="1042" alt="Screenshot 2025-03-22 at 6 19 07 PM" src="https://github.com/user-attachments/assets/cbae3dcf-b571-490d-b0ad-3f0f035ac0d4" />

**Important:** The system performs analysis and generates recommendations but does not execute actual trades.

## Key Features & Enhancements

This implementation includes several enhancements and customizations:

- **Multi-Agent Architecture**: Coordinated system of specialized investment agents
- **Flexible LLM Support**: Compatible with multiple AI providers (OpenAI, Anthropic, Groq, DeepSeek, and more)
- **Advanced Backtesting**: Comprehensive performance analysis with custom metrics
- **Real-time Analysis**: Live market data integration and sentiment analysis
- **Modular Design**: Easily extensible architecture for adding new agents and strategies
- **CLI & Web Interface**: Multiple interfaces for different use cases
- **Risk Management**: Built-in position sizing, stop-loss, and portfolio risk controls
- **Configuration System**: YAML-based configuration for easy customization

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                           │
│                   (CLI / Web Application)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Portfolio Manager                             │
│              (Aggregates signals & makes decisions)              │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Analyst    │    │   Signal     │    │     Risk     │
│   Agents     │    │  Generators  │    │   Manager    │
│              │    │              │    │              │
│ • Buffett    │    │ • Valuation  │    │ • Position   │
│ • Graham     │    │ • Sentiment  │    │   Limits     │
│ • Munger     │    │ • Technical  │    │ • Stop Loss  │
│ • Lynch      │    │ • Fundamental│    │ • Portfolio  │
│ • Fisher     │    │              │    │   Risk       │
│ • Burry      │    │              │    │              │
│ • Damodaran  │    │              │    │              │
│ • And more...│    │              │    │              │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Data Layer         │
                │ • Market Data API    │
                │ • Financial Metrics  │
                │ • News & Sentiment   │
                │ • Cache System       │
                └──────────────────────┘
```

## Disclaimer

This project is for **educational and research purposes only**.

- Not intended for real trading or investment
- No investment advice or guarantees provided
- Creator assumes no liability for financial losses
- Consult a financial advisor for investment decisions
- Past performance does not indicate future results

By using this software, you agree to use it solely for learning purposes.

## Table of Contents
- [How to Install](#how-to-install)
- [How to Run](#how-to-run)
  - [⌨️ Command Line Interface](#️-command-line-interface)
  - [🖥️ Web Application](#️-web-application)
- [How to Contribute](#how-to-contribute)
- [Feature Requests](#feature-requests)
- [License](#license)

## How to Install

Before you can run the system, you'll need to install it and set up your API keys. These steps are common to both the full-stack web application and command line interface.

### Quick Setup (Recommended)

```bash
git clone https://github.com/Rahulyatagiri/AI-Hedge-Fund.git
cd AI-Hedge-Fund
./setup.sh
```

The setup script will:
- Install Poetry (if not already installed)
- Install all project dependencies
- Create a `.env` file from the template
- Provide next steps for configuration

### Manual Installation

If you prefer to set up manually:

#### 1. Clone the Repository

```bash
git clone https://github.com/Rahulyatagiri/AI-Hedge-Fund.git
cd AI-Hedge-Fund
```

#### 2. Set up API keys

Create a `.env` file for your API keys:
```bash
# Create .env file for your API keys (in the root directory)
cp .env.example .env
```

Open and edit the `.env` file to add your API keys:
```bash
# For running LLMs hosted by openai (gpt-4o, gpt-4o-mini, etc.)
OPENAI_API_KEY=your-openai-api-key

# For getting financial data to power the hedge fund
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
```

**Important**: You must set at least one LLM API key (e.g. `OPENAI_API_KEY`, `GROQ_API_KEY`, `ANTHROPIC_API_KEY`, or `DEEPSEEK_API_KEY`) for the hedge fund to work. 

**Financial Data**: Data for AAPL, GOOGL, MSFT, NVDA, and TSLA is free and does not require an API key. For any other ticker, you will need to set the `FINANCIAL_DATASETS_API_KEY` in the .env file.

## How to Run

### ⌨️ Command Line Interface

You can run the AI Hedge Fund directly via terminal. This approach offers more granular control and is useful for automation, scripting, and integration purposes.

<img width="992" alt="Screenshot 2025-01-06 at 5 50 17 PM" src="https://github.com/user-attachments/assets/e8ca04bf-9989-4a7d-a8b4-34e04666663b" />

#### Quick Start

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

#### Run the AI Hedge Fund
```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA
```

You can also specify a `--ollama` flag to run the AI hedge fund using local LLMs.

```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA --ollama
```

You can optionally specify the start and end dates to make decisions over a specific time period.

```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01
```

#### Run the Backtester
```bash
poetry run python src/backtester.py --ticker AAPL,MSFT,NVDA
```

**Example Output:**
<img width="941" alt="Screenshot 2025-01-06 at 5 47 52 PM" src="https://github.com/user-attachments/assets/00e794ea-8628-44e6-9a84-8f8a31ad3b47" />


Note: The `--ollama`, `--start-date`, and `--end-date` flags work for the backtester, as well!

### 🖥️ Web Application

The new way to run the AI Hedge Fund is through our web application that provides a user-friendly interface. This is recommended for users who prefer visual interfaces over command line tools.

Please see detailed instructions on how to install and run the web application [here](https://github.com/Rahulyatagiri/AI-Hedge-Fund/tree/main/app).

<img width="1721" alt="Screenshot 2025-06-28 at 6 41 03 PM" src="https://github.com/user-attachments/assets/b95ab696-c9f4-416c-9ad1-51feb1f5374b" />


## How to Contribute

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to contribute to this project.

**Quick Start for Contributors:**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes and test thoroughly
4. Commit your changes (`git commit -m 'Add: AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

**Important**: Please keep your pull requests small and focused. Make sure all tests pass before submitting.

## Feature Requests

If you have a feature request, please open an [issue](https://github.com/Rahulyatagiri/AI-Hedge-Fund/issues) and make sure it is tagged with `enhancement`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
