#!/bin/bash
set -e

# Install Poetry if missing
if ! command -v poetry >/dev/null 2>&1; then
    python3 -m pip install --user poetry
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Use the current venv for Poetry operations
poetry config virtualenvs.create false

# Install project dependencies
poetry install --no-interaction --no-ansi
