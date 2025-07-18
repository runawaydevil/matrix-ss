# Matrix Screen Saver Collection

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Unix%20%7C%20macOS-lightgrey.svg)](https://www.linux.org/)
[![Terminal](https://img.shields.io/badge/Terminal-curses%20compatible-orange.svg)](https://docs.python.org/3/library/curses.html)
[![Status](https://img.shields.io/badge/Status-Enhanced-brightgreen.svg)](https://github.com/yourusername/matrix-ss)
[![Versions](https://img.shields.io/badge/Versions-17%20Variants-blue.svg)](README.md#versions)
[![Effects](https://img.shields.io/badge/Effects-Advanced%20Visual-purple.svg)](README.md#advanced-effects)
[![Interactive](https://img.shields.io/badge/Interactive-Audio%20Reactive-red.svg)](README.md#interactive-features)

A comprehensive collection of terminal-based Matrix-style screen savers featuring the iconic "digital rain" effect with advanced visual enhancements, interactive features, and multiple themed variants for every occasion.

## Features

[![Matrix Style](https://img.shields.io/badge/Matrix%20Style-Authentic%20Digital%20Rain-brightgreen.svg)](https://en.wikipedia.org/wiki/The_Matrix)
[![Animation](https://img.shields.io/badge/Animation-20%20FPS-blue.svg)](https://en.wikipedia.org/wiki/Frame_rate)
[![Controls](https://img.shields.io/badge/Controls-Simple%20%28q%20to%20quit%29-orange.svg)](README.md#controls)
[![Performance](https://img.shields.io/badge/Performance-Lightweight%20%26%20Efficient-green.svg)](README.md#technical-details)
[![Variants](https://img.shields.io/badge/Variants-10%20Unique%20Themes-purple.svg)](README.md#versions)
[![Advanced](https://img.shields.io/badge/Advanced-Fade%20%26%20Trail%20Effects-cyan.svg)](README.md#advanced-effects)
[![Interactive](https://img.shields.io/badge/Interactive-Audio%20%26%20Visual-red.svg)](README.md#interactive-features)
[![Katakana](https://img.shields.io/badge/Katakana-Authentic%20Japanese-yellow.svg)](README.md#enhanced-characters)

### Core Features
- 🌟 Authentic Matrix-style digital rain effect
- 🎨 17 unique variants with different themes and effects
- ⚡ Smooth animation (~20 FPS)
- ⌨️ Simple controls (press 'q' to quit)
- 🐧 Linux/Unix/macOS compatible
- 🎯 Lightweight and efficient

### Advanced Effects
- 🔥 Fire gradient effects (blue → red → white)
- 🌊 Wave motion patterns with color transitions
- ⚡ Glitch effects with system error messages
- 🎭 Trail fade effects for realistic motion blur
- 🖼️ Progressive image revelation through Matrix rain
- 🎵 Audio-reactive visual responses (simulated)

### Enhanced Characters
- 🇯🇵 Authentic Japanese Katakana characters
- 🔤 Mixed ASCII and Unicode character sets
- 🎲 Dynamic character selection algorithms
- ⚡ Variable speed columns for realistic flow

## Requirements

[![Python Version](https://img.shields.io/badge/Python-3.x+-blue.svg)](https://www.python.org/downloads/)
[![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Unix%20%7C%20macOS-lightgrey.svg)](https://www.linux.org/)
[![Library](https://img.shields.io/badge/Library-curses-orange.svg)](https://docs.python.org/3/library/curses.html)
[![Dependencies](https://img.shields.io/badge/Dependencies-psutil%20%28optional%29-yellow.svg)](https://pypi.org/project/psutil/)
[![Audio](https://img.shields.io/badge/Audio-pyaudio%20%28optional%29-red.svg)](https://pypi.org/project/PyAudio/)

### Core Requirements
- Python 3.x
- Linux/Unix/macOS terminal
- `curses` library (usually included with Python)

### Optional Dependencies
- `psutil` library (for system monitoring in `matrix_system.py`)
- `pyaudio` or `sounddevice` (for real audio input in `matrix_music.py`)

### Unicode Support
- Terminal with Unicode/UTF-8 support (for Katakana characters in `matrix_enhanced.py`)

## Installation

### Dependencies Installation
```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install psutil  # For system monitoring (matrix_system.py)

# Optional: For real audio input (matrix_music.py)
# pip install pyaudio
# pip install sounddevice
```

### Method 1: Direct Download
```bash
# Clone or download the repository
git clone <repository-url>
cd matrix-ss

# Make all scripts executable
chmod +x *.py
```

### Method 2: Manual Setup
```bash
# Download all scripts to your desired location
# (All 10 matrix variants)

# Make executable
chmod +x matrix*.py
```

## Usage

### Basic Usage
```bash
# Classic Collection
python3 matrix.py              # Original green Matrix
python3 matrix_red.py          # Dramatic green + red
python3 matrix_rainbow.py      # Festive rainbow colors
python3 matrix_system.py       # System monitoring

# Enhanced Collection
python3 matrix_enhanced.py     # Katakana + fade effects
python3 matrix_fire.py         # Fire gradient effects
python3 matrix_glitch.py       # Glitch + error messages
python3 matrix_wave.py         # Wave motion patterns
python3 matrix_image.py        # Progressive image reveal
python3 matrix_music.py        # Audio-reactive (simulated)
```

### Quick Start
```bash
# Make all executable and run your favorite
chmod +x *.py
./matrix_enhanced.py           # Recommended for best experience
```

### Controls
- **Press 'q'** to quit the screen saver
- **Ctrl+C** to force exit

## Versions

### Classic Collection

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

### 🖥️ System Monitor Matrix (`matrix_system.py`)
Advanced version that displays real-time system information in the center while Matrix rain falls around it.

```bash
python3 matrix_system.py
```

**Features:**
- 🖥️ Real-time system monitoring (CPU, Memory, Disk, IP, Time, Date, User, Load)
- 🔴 System info displayed in red at center
- 🟢 Matrix rain falls around the information panel
- ⏰ Updates every second
- 🎯 Perfect for system administrators and monitoring

---

### Enhanced Collection

### ⭐ Enhanced Matrix (`matrix_enhanced.py`) - **RECOMMENDED**
[![New](https://img.shields.io/badge/NEW-Enhanced%20Version-brightgreen.svg)](matrix_enhanced.py)
[![Katakana](https://img.shields.io/badge/Katakana-Authentic%20Japanese-yellow.svg)](matrix_enhanced.py)
[![Fade](https://img.shields.io/badge/Fade-Trail%20Effects-cyan.svg)](matrix_enhanced.py)

The most advanced version with authentic Japanese characters and realistic fade effects.

```bash
python3 matrix_enhanced.py
```

**Features:**
- 🇯🇵 Authentic Katakana characters (70%) + ASCII (30%)
- 🎭 Realistic trail fade effects
- ⚡ Variable speed columns
- 🌟 Most authentic Matrix experience
- 💫 Character aging and disappearing effects

### 🔥 Fire Matrix (`matrix_fire.py`)
[![New](https://img.shields.io/badge/NEW-Fire%20Effects-red.svg)](matrix_fire.py)

Matrix rain with dynamic fire gradient effects that change temperature over time.

```bash
python3 matrix_fire.py
```

**Features:**
- 🔥 Dynamic fire gradient (Blue → Cyan → Green → Yellow → Red → Magenta → White)
- 🌡️ Heat levels that change over time
- ❄️ Cool and hot zones
- 🎨 7-stage color temperature system

### ⚡ Glitch Matrix (`matrix_glitch.py`)
[![New](https://img.shields.io/badge/NEW-Glitch%20Effects-purple.svg)](matrix_glitch.py)

Matrix with random glitch effects and system error messages for a cyberpunk feel.

```bash
python3 matrix_glitch.py
```

**Features:**
- ⚡ Random glitch effects every 5-15 seconds
- 🚨 System error messages ("ERROR: SYSTEM BREACH DETECTED")
- 🎭 Corrupted character blocks (█▓▒░)
- 💥 Flashing and color corruption effects
- 🔴 Red alert colors during glitches

### 🌊 Wave Matrix (`matrix_wave.py`)
[![New](https://img.shields.io/badge/NEW-Wave%20Motion-blue.svg)](matrix_wave.py)

Matrix rain influenced by sine wave patterns with dynamic color transitions.

```bash
python3 matrix_wave.py
```

**Features:**
- 🌊 Sine wave motion patterns
- 🎨 Color zones based on wave proximity (White → Cyan → Blue → Green)
- ⚡ Variable speed influenced by wave position
- 〰️ Visible wave line indicator
- 🌀 Fluid, organic movement patterns

### 🖼️ Image Reveal Matrix (`matrix_image.py`)
[![New](https://img.shields.io/badge/NEW-Image%20Reveal-orange.svg)](matrix_image.py)

Matrix rain that gradually reveals hidden ASCII art with progress tracking.

```bash
python3 matrix_image.py
```

**Features:**
- 🖼️ Progressive ASCII art revelation
- 📊 Real-time decoding progress bar
- 🎨 Color-coded revelation stages (Yellow → White → Red)
- 💬 "WAKE UP NEO" hidden message
- 🎯 Interactive discovery experience

### 🎵 Music Matrix (`matrix_music.py`)
[![New](https://img.shields.io/badge/NEW-Audio%20Reactive-red.svg)](matrix_music.py)
[![Real Audio](https://img.shields.io/badge/Audio-Real%20%2B%20Simulated-brightgreen.svg)](matrix_music.py)
[![Smart Detection](https://img.shields.io/badge/Detection-Auto%20Library-blue.svg)](matrix_music.py)

Audio-reactive Matrix that responds to real microphone input or simulated audio with dynamic effects.

```bash
# Basic usage (simulated audio)
python3 matrix_music.py

# For real audio, install dependencies first:
pip install sounddevice numpy
# OR
pip install pyaudio numpy

# Then run with real audio input
python3 matrix_music.py
```

**Features:**
- 🎤 **Real microphone input** (when libraries installed)
- 🎭 **Automatic fallback** to realistic simulation
- 🎵 Audio level visualization with progress bar
- 🎨 Color intensity based on sound (Green → Yellow → Red → Magenta → White → Cyan)
- 💓 Intelligent beat detection with special effects
- ⚡ Speed changes based on audio intensity
- 📊 Real-time audio level display
- 🎶 "BEAT!" indicator for rhythm detection
- 🔧 **Auto-detection** of available audio libraries (sounddevice/pyaudio)
- 💬 **Status display** showing audio mode for 3 seconds

**Audio Libraries Supported:**
- `sounddevice` + `numpy` (recommended - easier installation)
- `pyaudio` + `numpy` (alternative - more control)
- Automatic simulation if no libraries available

---

### Themed Collection

### 💎 Neon Matrix (`matrix_neon.py`)
[![New](https://img.shields.io/badge/NEW-Neon%20Effects-cyan.svg)](matrix_neon.py)
[![Glow](https://img.shields.io/badge/Glow-Pulsing%20Brightness-magenta.svg)](matrix_neon.py)

Matrix with neon glow effects and pulsing brightness for a cyberpunk aesthetic.

```bash
python3 matrix_neon.py
```

**Features:**
- 💎 Neon glow effects with variable intensity
- 🌟 Pulsing brightness based on sine waves
- ⚡ Flash effects and border illumination
- 🎨 Multi-intensity color gradients (Dark → Bright → White)
- 💫 Special neon colors (Magenta, Yellow highlights)
- 🔆 Column-based glow intensity system

### 🔢 Binary Matrix (`matrix_binary.py`)
[![New](https://img.shields.io/badge/NEW-Binary%20Only-green.svg)](matrix_binary.py)
[![Authentic](https://img.shields.io/badge/Authentic-Movie%20Style-yellow.svg)](matrix_binary.py)

Pure binary Matrix using only 0s and 1s like in the original movie scenes.

```bash
python3 matrix_binary.py
```

**Features:**
- 🔢 **Only 0s and 1s** - true to the movie
- 💬 Hidden binary messages ("Hello", "Matrix", "Neo", "Wake up")
- 📊 Real-time binary counter display
- 🎯 Data stream effects with horizontal flows
- 🔍 Progressive message decoding with progress indicator
- 💻 Authentic computer code aesthetic

### 💻 Terminal Matrix (`matrix_terminal.py`)
[![New](https://img.shields.io/badge/NEW-Hacker%20Terminal-red.svg)](matrix_terminal.py)
[![Interactive](https://img.shields.io/badge/Interactive-Command%20Simulation-orange.svg)](matrix_terminal.py)

Simulates a hacker terminal with realistic command execution in the center of Matrix rain.

```bash
python3 matrix_terminal.py
```

**Features:**
- 💻 **Realistic hacker commands** (nmap, hydra, metasploit, etc.)
- ⌨️ Simulated typing with realistic speed
- 📟 System responses and command output
- 🕐 Real-time timestamp display
- 🎭 Terminal window with borders and title
- 🔒 Cybersecurity tool simulation (ethical hacking commands)

### 🧬 DNA Matrix (`matrix_dna.py`)
[![New](https://img.shields.io/badge/NEW-DNA%20Sequences-green.svg)](matrix_dna.py)
[![Scientific](https://img.shields.io/badge/Scientific-Genetic%20Code-blue.svg)](matrix_dna.py)

Matrix displaying DNA sequences with complementary base pairs and genetic information.

```bash
python3 matrix_dna.py
```

**Features:**
- 🧬 **DNA bases only** (A, T, G, C) with authentic color coding
- 🔗 **Double helix visualization** with complementary base pairs
- 🧪 Famous DNA sequences (telomeres, restriction sites)
- 📊 Real-time base counting and analysis
- 🌀 Animated helix structure with connecting bonds
- 🔬 Scientific sequencer interface

### 🌐 Network Matrix (`matrix_network.py`)
[![New](https://img.shields.io/badge/NEW-Network%20Monitor-blue.svg)](matrix_network.py)
[![Live Data](https://img.shields.io/badge/Live%20Data-Network%20Traffic-cyan.svg)](matrix_network.py)

Matrix displaying real network information and simulated traffic data.

```bash
python3 matrix_network.py
```

**Features:**
- 🌐 **Real network information** (hostname, IP, connections)
- 📊 Network traffic visualization and statistics
- 🔌 Active port monitoring
- 📡 Simulated packet flows (TCP, UDP, HTTP, SSH, etc.)
- 📈 Real-time traffic level indicator
- 🖥️ Network status monitoring

### 💰 Crypto Matrix (`matrix_crypto.py`)
[![New](https://img.shields.io/badge/NEW-Cryptocurrency-yellow.svg)](matrix_crypto.py)
[![Market Data](https://img.shields.io/badge/Market%20Data-Price%20Tracking-gold.svg)](matrix_crypto.py)

Matrix displaying cryptocurrency prices and market data with trading symbols.

```bash
python3 matrix_crypto.py
```

**Features:**
- 💰 **Cryptocurrency price tracking** (BTC, ETH, ADA, DOT, LINK, XRP)
- 📈 **Price trends** with up/down indicators
- 💹 Market sentiment analysis (Bull/Bear/Sideways)
- 🎯 Crypto symbols rain (₿, Ξ, ₳, etc.)
- 📊 Real-time price changes and percentage tracking
- 🚀 Market status indicators with emojis

### 🌤️ Weather Matrix (`matrix_weather.py`)
[![New](https://img.shields.io/badge/NEW-Weather%20Data-blue.svg)](matrix_weather.py)
[![Meteorological](https://img.shields.io/badge/Meteorological-Climate%20Info-lightblue.svg)](matrix_weather.py)

Matrix displaying weather information with climate-appropriate character effects.

```bash
python3 matrix_weather.py
```

**Features:**
- 🌤️ **Complete weather information** (temperature, humidity, pressure, wind)
- 🌧️ **Weather-specific characters** (☀️, ☁️, 🌧️, ⛈️, ❄️, 🌫️)
- 🎨 **Dynamic colors** based on weather conditions
- ⚠️ **Weather alerts** (temperature, wind, UV, visibility warnings)
- 🌡️ **Comfort level indicators** (Cold, Cool, Comfortable, Warm, Hot)
- 📊 Detailed meteorological panel with real-time updates

---

### Complete Version Comparison

| Version | Colors | Special Effects | Best For | Difficulty |
|---------|--------|----------------|----------|------------|
| **Classic Collection** |
| `matrix.py` | Green only | Classic rain | Nostalgia, simplicity | ⭐ |
| `matrix_red.py` | Green + Red | Dramatic mix | Alerts, intensity | ⭐ |
| `matrix_rainbow.py` | 7 rainbow colors | Festive colors | Celebrations, demos | ⭐ |
| `matrix_system.py` | Green + Red + Yellow | System monitoring | Admin work | ⭐⭐ |
| **Enhanced Collection** |
| `matrix_enhanced.py` | Green gradients | Katakana + fade | **Best overall** | ⭐⭐⭐ |
| `matrix_fire.py` | Fire gradient | Heat simulation | Visual impact | ⭐⭐ |
| `matrix_glitch.py` | Multi + corruption | Error messages | Cyberpunk feel | ⭐⭐ |
| `matrix_wave.py` | Wave-based | Sine motion | Fluid animation | ⭐⭐⭐ |
| `matrix_image.py` | Progressive reveal | ASCII art | Interactive fun | ⭐⭐⭐ |
| `matrix_music.py` | Audio-reactive | Beat detection | Parties, music | ⭐⭐⭐⭐ |
| **Themed Collection** |
| `matrix_neon.py` | Neon gradients | Pulsing glow | Cyberpunk aesthetic | ⭐⭐ |
| `matrix_binary.py` | Green + White | Binary only | Movie authenticity | ⭐ |
| `matrix_terminal.py` | Multi-colored | Hacker simulation | Educational/Demo | ⭐⭐⭐ |
| `matrix_dna.py` | Scientific colors | DNA sequences | Science/Education | ⭐⭐⭐ |
| `matrix_network.py` | Traffic-based | Network monitoring | IT/Networking | ⭐⭐ |
| `matrix_crypto.py` | Market-based | Price tracking | Finance/Trading | ⭐⭐ |
| `matrix_weather.py` | Weather-based | Climate data | Weather monitoring | ⭐⭐ |

## How It Works

### Basic Algorithm
The screen saver creates a full-screen terminal animation where:
- Random characters fall from the top of the screen
- Each column has its own falling speed and position
- Characters are displayed with various color schemes
- The effect continues until you press 'q' to exit

### Advanced Features
- **Trail Effects**: Characters fade over time for realistic motion blur
- **Variable Speeds**: Different columns fall at different rates
- **Dynamic Colors**: Color changes based on effects (fire, wave, audio)
- **Interactive Elements**: Progress bars, system info, error messages
- **Unicode Support**: Authentic Japanese Katakana characters

## Technical Details

### Performance
- **Frame Rate**: ~20 FPS (50ms intervals)
- **Memory Usage**: Minimal (< 10MB for most variants)
- **CPU Usage**: Low impact on system performance
- **Terminal**: Uses `curses` library for efficient terminal manipulation

### Character Sets
- **ASCII**: Printable characters (33-126) for compatibility
- **Katakana**: Authentic Japanese characters (アイウエオ...)
- **Special**: Block characters for glitch effects (█▓▒░)
- **Unicode**: Full UTF-8 support where available

### Color Systems
- **8-Color**: Standard terminal colors (Red, Green, Blue, etc.)
- **Gradients**: Smooth transitions between color states
- **Dynamic**: Real-time color changes based on effects
- **Compatibility**: Works with all curses-compatible terminals

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