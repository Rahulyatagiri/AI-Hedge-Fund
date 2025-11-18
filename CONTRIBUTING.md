# Contributing to AI Quantitative Trading System

Thank you for your interest in contributing to this AI-powered quantitative trading system! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [Issues](https://github.com/Rahulyatagiri/AI-Hedge-Fund/issues) section
2. If not, create a new issue with a clear title and description
3. Include steps to reproduce (for bugs) or detailed explanation (for features)
4. Add relevant labels (bug, enhancement, documentation, etc.)

### Submitting Changes

1. **Fork the Repository**
   ```bash
   git clone https://github.com/Rahulyatagiri/AI-Hedge-Fund.git
   cd AI-Hedge-Fund
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   poetry run pytest
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes

## Code Style Guidelines

### Python

- Follow PEP 8 style guide
- Use type hints where applicable
- Maximum line length: 420 characters (as per project configuration)
- Use meaningful variable and function names

### Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions and classes
- Include inline comments for complex logic

### Commit Messages

Use clear, descriptive commit messages:

- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for updates to existing features
- `Refactor:` for code refactoring
- `Docs:` for documentation changes
- `Test:` for test-related changes

Examples:
```
Add: New momentum-based trading agent
Fix: Portfolio rebalancing calculation error
Update: Improve sentiment analysis accuracy
Docs: Add configuration file documentation
```

## Development Setup

1. **Install Poetry** (if not already installed)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install Dependencies**
   ```bash
   poetry install
   ```

3. **Set Up Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run Tests**
   ```bash
   poetry run pytest
   ```

## Adding New Agents

To add a new investment agent:

1. Create a new file in `src/agents/`
2. Implement the agent following the existing agent patterns
3. Update the agent registry in `src/agents/__init__.py`
4. Add tests for your agent
5. Update documentation

## Project Structure

```
AI-Hedge-Fund/
├── src/
│   ├── agents/          # Investment strategy agents
│   ├── backtesting/     # Backtesting framework
│   ├── data/            # Data models and cache
│   ├── graph/           # State management
│   ├── llm/             # LLM integration
│   ├── tools/           # Utility tools
│   └── utils/           # Helper utilities
├── app/                 # Web application
├── tests/               # Test files
├── config.yaml          # System configuration
└── pyproject.toml       # Project dependencies
```

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Review existing documentation
- Check closed issues for similar questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping improve this project!
