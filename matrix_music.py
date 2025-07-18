#!/usr/bin/env python3
import curses
import random
import time
import sys

# Try to import audio libraries
AUDIO_AVAILABLE = False
audio_lib = None

try:
    import sounddevice as sd
    import numpy as np
    audio_lib = "sounddevice"
    AUDIO_AVAILABLE = True
except ImportError:
    try:
        import pyaudio
        import numpy as np
        audio_lib = "pyaudio"
        AUDIO_AVAILABLE = True
    except ImportError:
        pass

def get_audio_level():
    """Get real audio level if libraries available, otherwise simulate"""
    if not AUDIO_AVAILABLE:
        # Simulação mais realista
        base_level = random.randint(10, 40)
        if random.randint(1, 20) == 1:  # 5% chance de pico
            return random.randint(70, 100)
        elif random.randint(1, 10) == 1:  # 10% chance de nível médio
            return random.randint(50, 70)
        return base_level
    
    try:
        if audio_lib == "sounddevice":
            # Using sounddevice (easier method)
            duration = 0.1  # 100ms sample
            sample_rate = 44100
            recording = sd.rec(int(duration * sample_rate), 
                             samplerate=sample_rate, channels=1, dtype='float64')
            sd.wait()  # Wait until recording is finished
            
            # Calculate RMS (Root Mean Square) for volume level
            rms = np.sqrt(np.mean(recording**2))
            # Convert to percentage (0-100)
            level = min(100, int(rms * 1000))
            return level
            
        elif audio_lib == "pyaudio":
            # Using pyaudio (more complex but more control)
            chunk = 1024
            format = pyaudio.paInt16
            channels = 1
            rate = 44100
            
            p = pyaudio.PyAudio()
            stream = p.open(format=format, channels=channels, rate=rate, 
                          input=True, frames_per_buffer=chunk)
            
            data = stream.read(chunk, exception_on_overflow=False)
            stream.stop_stream()
            stream.close()
            p.terminate()
            
            # Convert to numpy array and calculate RMS
            audio_data = np.frombuffer(data, dtype=np.int16)
            rms = np.sqrt(np.mean(audio_data**2))
            # Normalize to 0-100 range
            level = min(100, int(rms / 100))
            return level
            
    except Exception as e:
        # Fall back to simulation if real audio fails
        return random.randint(0, 100)
    
    return random.randint(0, 100)

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    audio_history = [0] * 10  # histórico de níveis de áudio
    
    # Show audio mode for 3 seconds
    audio_mode_timer = 60  # 3 seconds at 20fps

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # baixo
    curses.init_pair(2, curses.COLOR_YELLOW, -1)     # médio
    curses.init_pair(3, curses.COLOR_RED, -1)        # alto
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)    # muito alto
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # pico
    curses.init_pair(6, curses.COLOR_CYAN, -1)       # beat

    beat_threshold = 70
    last_beat_time = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # obtém nível de áudio atual
        current_audio = get_audio_level()
        audio_history.append(current_audio)
        audio_history.pop(0)
        
        # detecta beat (aumento súbito no áudio)
        avg_audio = sum(audio_history) / len(audio_history)
        is_beat = current_audio > beat_threshold and current_audio > avg_audio * 1.5
        
        current_time = time.time()
        if is_beat:
            last_beat_time = current_time

        # efeito baseado no áudio
        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # velocidade baseada no áudio
            if current_audio > 80:
                speed_multiplier = 3
            elif current_audio > 60:
                speed_multiplier = 2
            else:
                speed_multiplier = 1
            
            # cor baseada no nível de áudio
            if current_time - last_beat_time < 0.2:  # efeito beat recente
                color_pair = curses.color_pair(6)  # ciano
            elif current_audio > 90:
                color_pair = curses.color_pair(5)  # branco
            elif current_audio > 70:
                color_pair = curses.color_pair(4)  # magenta
            elif current_audio > 50:
                color_pair = curses.color_pair(3)  # vermelho
            elif current_audio > 30:
                color_pair = curses.color_pair(2)  # amarelo
            else:
                color_pair = curses.color_pair(1)  # verde
            
            try:
                stdscr.addch(y, x, char, color_pair)
            except curses.error:
                pass

            # movimento baseado no áudio
            if random.randint(1, 4 - speed_multiplier) == 1:
                columns[x] = 0 if y >= sh - 1 else y + 1

        # visualizador de áudio no topo
        try:
            audio_bar = "♪" * (current_audio // 5)
            audio_text = f"AUDIO: {current_audio:3d}% {audio_bar}"
            stdscr.addstr(0, 0, audio_text[:sw], curses.color_pair(6))
            
            # indicador de beat
            if current_time - last_beat_time < 0.1:
                beat_text = "BEAT!"
                stdscr.addstr(0, sw - len(beat_text), beat_text, 
                             curses.color_pair(5) | curses.A_BOLD)
            
            # mostra modo de áudio por 3 segundos
            if audio_mode_timer > 0:
                if AUDIO_AVAILABLE:
                    mode_text = f"REAL AUDIO MODE: {audio_lib.upper()}"
                    color = curses.color_pair(5)  # branco
                else:
                    mode_text = "SIMULATED AUDIO MODE - Install sounddevice/pyaudio for real audio"
                    color = curses.color_pair(2)  # amarelo
                
                mode_y = sh // 2
                mode_x = max(0, (sw - len(mode_text)) // 2)
                stdscr.addstr(mode_y, mode_x, mode_text[:sw], color | curses.A_BOLD)
                audio_mode_timer -= 1
                
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass