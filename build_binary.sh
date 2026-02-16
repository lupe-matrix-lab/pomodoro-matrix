#!/bin/bash
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed --add-data "pomodoro.html:." --name "PomodoroMatrix" pomodoro_app.py
