# Matrix Screen Saver

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Unix%20%7C%20macOS-lightgrey.svg)](https://www.linux.org/)
[![Terminal](https://img.shields.io/badge/Terminal-curses%20compatible-orange.svg)](https://docs.python.org/3/library/curses.html)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/yourusername/matrix-ss)
[![Versions](https://img.shields.io/badge/Versions-3%20Variants-blue.svg)](README.md#versions)

A collection of terminal-based Matrix-style screen savers that simulate the iconic "digital rain" effect from the Matrix movies. Multiple color variants available for different moods and occasions.

## Features

[![Matrix Style](https://img.shields.io/badge/Matrix%20Style-Authentic%20Digital%20Rain-brightgreen.svg)](https://en.wikipedia.org/wiki/The_Matrix)
[![Animation](https://img.shields.io/badge/Animation-20%20FPS-blue.svg)](https://en.wikipedia.org/wiki/Frame_rate)
[![Controls](https://img.shields.io/badge/Controls-Simple%20%28q%20to%20quit%29-orange.svg)](README.md#controls)
[![Performance](https://img.shields.io/badge/Performance-Lightweight%20%26%20Efficient-green.svg)](README.md#technical-details)
[![Variants](https://img.shields.io/badge/Variants-3%20Color%20Themes-purple.svg)](README.md#versions)

- 🌟 Authentic Matrix-style digital rain effect
- 🎨 Multiple color variants (Green, Red+Green, Rainbow)
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

# Make all scripts executable
chmod +x matrix.py matrix_red.py matrix_rainbow.py
```

### Method 2: Manual Setup
```bash
# Download all scripts to your desired location
wget <matrix.py-url>
wget <matrix_red.py-url>
wget <matrix_rainbow.py-url>

# Make executable
chmod +x matrix.py matrix_red.py matrix_rainbow.py
```

## Usage

### Basic Usage
```bash
# Classic Matrix (green only)
python3 matrix.py

# Dramatic Matrix (green + red)
python3 matrix_red.py

# Rainbow Matrix (all colors)
python3 matrix_rainbow.py
```

### Alternative Methods
```bash
# If made executable
./matrix.py
./matrix_red.py
./matrix_rainbow.py

# Or with python directly
python matrix.py
python matrix_red.py
python matrix_rainbow.py
```

### Controls
- **Press 'q'** to quit the screen saver
- **Ctrl+C** to force exit

## Versions

### 🟢 Classic Matrix (`matrix.py`)
The original Matrix screen saver with authentic green digital rain effect.

```bash
python3 matrix.py
```

**Features:**
- 🌟 Authentic Matrix movie experience
- 🟢 Green characters only
- 🎬 Nostalgic classic look

### 🔴 Dramatic Matrix (`matrix_red.py`)
Enhanced version with red characters mixed with green for a more dramatic effect.

```bash
python3 matrix_red.py
```

**Features:**
- 🟢 80% green characters
- 🔴 20% red characters
- ⚡ Dramatic visual impact
- 🎭 Perfect for intense moments

### 🌈 Rainbow Matrix (`matrix_rainbow.py`)
Vibrant rainbow version with all colors of the spectrum for festive occasions.

```bash
python3 matrix_rainbow.py
```

**Features:**
- 🌈 7 rainbow colors (Red, Yellow, Green, Cyan, Blue, Magenta, White)
- 🎉 Perfect for celebrations and events
- ✨ Vibrant and eye-catching
- 🎪 Great for demonstrations

### Version Comparison

| Version | Colors | Effect | Best For |
|---------|--------|--------|----------|
| `matrix.py` | Green only | Classic Matrix | Nostalgia, authentic experience |
| `matrix_red.py` | Green + Red | Dramatic | Intense moments, alerts |
| `matrix_rainbow.py` | 7 rainbow colors | Festive | Celebrations, demonstrations |

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

You can modify any of the scripts to change:
- **Speed**: Adjust `time.sleep(0.05)` value
- **Colors**: Modify the color pairs in each script
- **Characters**: Change the range in `random.randint(33, 126)`
- **Frame rate**: Modify the `timeout(100)` value
- **Color distribution**: Adjust the probability ratios in `matrix_red.py`
- **Rainbow colors**: Add/remove colors from the `rainbow_colors` list in `matrix_rainbow.py`

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