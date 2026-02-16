# TODO: Pomodoro Matrix - Physical Integration

## Phase 1: Persistence & Desktop (Completed)
- [x] LocalStorage persistence (survives refreshes).
- [x] Auto-resume on reload (if timer was running).
- [x] Python Wrapper (desktop app via `pywebview`).
- [x] Cross-platform build setup (PyInstaller).

## Phase 2: Arduino/Physical Device
- [ ] **Hardware:** Arduino Nano/ESP32 + OLED Display + Buzzer.
- [ ] **Serial Bridge:** Add a Python bridge to send `timeLeft` via Serial to the Arduino.
- [ ] **Network Sync (Optional):** Use ESP32 to fetch the current state from a simple API (FastAPI) to sync web/desktop/physical device.

## Phase 3: Analytics
- [ ] Backend to save completed sessions.
- [ ] Daily/Weekly focus reports.
