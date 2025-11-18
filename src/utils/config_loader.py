"""
Configuration Loader Utility
Custom utility for loading and managing system configuration
Author: Rahul Yatagiri
"""

import yaml
import os
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigLoader:
    """Load and manage configuration settings for the trading system"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the configuration loader

        Args:
            config_path: Path to the configuration file. If None, uses default config.yaml
        """
        if config_path is None:
            # Default to config.yaml in the project root
            project_root = Path(__file__).parent.parent.parent
            config_path = project_root / "config.yaml"

        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from YAML file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    self._config = yaml.safe_load(f) or {}
            else:
                print(f"Warning: Config file not found at {self.config_path}. Using defaults.")
                self._config = self._get_default_config()
        except Exception as e:
            print(f"Error loading config: {e}. Using defaults.")
            self._config = self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration if file is not found"""
        return {
            "system": {
                "name": "AI-Powered Quantitative Trading System",
                "version": "1.0.0"
            },
            "trading": {
                "default_tickers": ["AAPL", "GOOGL", "MSFT", "NVDA", "TSLA"],
                "risk_management": {
                    "max_position_size": 0.20,
                    "stop_loss_percentage": 0.10,
                    "max_portfolio_risk": 0.02
                }
            }
        }

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by dot-notation key

        Args:
            key: Configuration key (e.g., 'trading.risk_management.max_position_size')
            default: Default value if key is not found

        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self._config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default

        return value

    def get_all(self) -> Dict[str, Any]:
        """Get all configuration as dictionary"""
        return self._config.copy()

    def update(self, key: str, value: Any) -> None:
        """
        Update configuration value

        Args:
            key: Configuration key (dot notation)
            value: New value
        """
        keys = key.split('.')
        config = self._config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value


# Global configuration instance
_config_instance: Optional[ConfigLoader] = None


def get_config() -> ConfigLoader:
    """Get global configuration instance"""
    global _config_instance
    if _config_instance is None:
        _config_instance = ConfigLoader()
    return _config_instance


def reload_config(config_path: Optional[str] = None) -> ConfigLoader:
    """Reload configuration from file"""
    global _config_instance
    _config_instance = ConfigLoader(config_path)
    return _config_instance
