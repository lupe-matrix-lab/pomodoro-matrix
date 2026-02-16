#!/bin/bash
# Create virtual environment to bypass PEP 668
python3 -m venv venv
source venv/bin/activate

# Install dependencies in venv
pip install --upgrade pip
pip install -r requirements.txt

# Build binary
pyinstaller --noconfirm --onefile --windowed --add-data "pomodoro.html:." --name "PomodoroMatrix" pomodoro_app.py

# Cleanup
deactivate
echo "Build complete. Check the 'dist' folder."
