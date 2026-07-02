"""
Application configuration.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

DATABASE_DIR = ROOT_DIR / "database"
