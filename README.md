# Matrix Screen Saver

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Unix%20%7C%20macOS-lightgrey.svg)](https://www.linux.org/)
[![Terminal](https://img.shields.io/badge/Terminal-curses%20compatible-orange.svg)](https://docs.python.org/3/library/curses.html)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/yourusername/matrix-ss)

A terminal-based Matrix-style screen saver that simulates the iconic "digital rain" effect from the Matrix movies. This Python script creates falling green characters in your terminal, providing a nostalgic and visually appealing screen saver experience.

## Features

[![Matrix Style](https://img.shields.io/badge/Matrix%20Style-Authentic%20Digital%20Rain-brightgreen.svg)](https://en.wikipedia.org/wiki/The_Matrix)
[![Animation](https://img.shields.io/badge/Animation-20%20FPS-blue.svg)](https://en.wikipedia.org/wiki/Frame_rate)
[![Controls](https://img.shields.io/badge/Controls-Simple%20%28q%20to%20quit%29-orange.svg)](README.md#controls)
[![Performance](https://img.shields.io/badge/Performance-Lightweight%20%26%20Efficient-green.svg)](README.md#technical-details)

- 🌟 Authentic Matrix-style digital rain effect
- 🎨 Green text on terminal background
- ⚡ Smooth animation (~20 FPS)
- ⌨️ Simple controls (press 'q' to quit)
- 🐧 Linux/Unix compatible
- 🎯 Lightweight and efficient

## Requirements

[![Python Version](https://img.shields.io/badge/Python-3.x+-blue.svg)](https://www.python.org/downloads/)
[![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Unix%20%7C%20macOS-lightgrey.svg)](https://www.linux.org/)
[![Library](https://img.shields.io/badge/Library-curses-orange.svg)](https://docs.python.org/3/library/curses.html)

- Python 3.x
- Linux/Unix terminal
- `curses` library (usually included with Python)

## Installation

### Method 1: Direct Download
```bash
# Clone or download the repository
git clone <repository-url>
cd matrix-ss

# Make the script executable
chmod +x matrix.py
```

### Method 2: Manual Setup
```bash
# Download matrix.py to your desired location
wget <matrix.py-url>

# Make executable
chmod +x matrix.py
```

## Usage

### Basic Usage
```bash
python3 matrix.py
```

### Alternative Methods
```bash
# If made executable
./matrix.py

# Or with python directly
python matrix.py
```

### Controls
- **Press 'q'** to quit the screen saver
- **Ctrl+C** to force exit

## How It Works

The screen saver creates a full-screen terminal animation where:
- Random ASCII characters (33-126) fall from the top of the screen
- Each column has its own falling speed and position
- Characters are displayed in green color
- The effect continues until you press 'q' to exit

## Technical Details

- **Frame Rate**: ~20 FPS (50ms intervals)
- **Colors**: Green text on default terminal background
- **Characters**: Printable ASCII characters (33-126)
- **Terminal**: Uses `curses` library for terminal manipulation
- **Compatibility**: Linux, macOS, and Unix-like systems

## Troubleshooting

### Common Issues

1. **"curses module not found"**
   ```bash
   # Install python3-curses (Ubuntu/Debian)
   sudo apt-get install python3-curses
   
   # Or for CentOS/RHEL
   sudo yum install python3-curses
   ```

2. **Terminal not supported**
   - Ensure you're using a terminal emulator that supports `curses`
   - Try running in a different terminal (xterm, gnome-terminal, etc.)

3. **Permission denied**
   ```bash
   chmod +x matrix.py
   ```

### Terminal Compatibility

[![xterm](https://img.shields.io/badge/xterm-Supported-brightgreen.svg)](https://invisible-island.net/xterm/)
[![gnome-terminal](https://img.shields.io/badge/gnome--terminal-Supported-brightgreen.svg)](https://help.gnome.org/users/gnome-terminal/)
[![konsole](https://img.shields.io/badge/konsole-Supported-brightgreen.svg)](https://konsole.kde.org/)
[![iTerm2](https://img.shields.io/badge/iTerm2-Supported-brightgreen.svg)](https://iterm2.com/)
[![Alacritty](https://img.shields.io/badge/Alacritty-Supported-brightgreen.svg)](https://alacritty.org/)
[![Windows CMD](https://img.shields.io/badge/Windows%20CMD-Not%20Supported-red.svg)](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

- ✅ xterm
- ✅ gnome-terminal
- ✅ konsole
- ✅ iTerm2 (macOS)
- ✅ Alacritty
- ❌ Windows Command Prompt (not supported)

## Customization

You can modify the script to change:
- **Speed**: Adjust `time.sleep(0.05)` value
- **Colors**: Modify `curses.init_pair(1, curses.COLOR_GREEN, -1)`
- **Characters**: Change the range in `random.randint(33, 126)`
- **Frame rate**: Modify the `timeout(100)` value

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## Acknowledgments

Inspired by the iconic Matrix digital rain effect from the 1999 film "The Matrix" directed by the Wachowskis.

---

**Enjoy your Matrix screen saver experience!** 🕶️ 