#!/bin/bash
set -e

# Ensure Poetry is installed
if ! command -v poetry >/dev/null 2>&1; then
    pip install --upgrade pip
    pip install --user poetry
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install project dependencies without creating a virtual environment
poetry config virtualenvs.create false
poetry install --no-interaction --no-ansi

