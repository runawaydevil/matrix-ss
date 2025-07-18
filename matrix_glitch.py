#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    glitch_timer = 0
    glitch_active = False
    corrupted_lines = set()

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # verde normal
    curses.init_pair(2, curses.COLOR_RED, -1)        # vermelho (erro)
    curses.init_pair(3, curses.COLOR_WHITE, -1)      # branco (glitch)
    curses.init_pair(4, curses.COLOR_YELLOW, -1)     # amarelo (aviso)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)    # magenta (corrupção)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # controla glitches aleatórios
        glitch_timer += 1
        if glitch_timer > random.randint(100, 300):  # glitch a cada 5-15 segundos
            glitch_active = True
            glitch_timer = 0
            # corrompe algumas linhas aleatórias
            corrupted_lines = set(random.randint(0, sh-1) for _ in range(random.randint(1, 5)))

        if glitch_active:
            # efeito glitch por alguns frames
            if random.randint(1, 10) > 7:  # 30% chance de parar o glitch
                glitch_active = False
                corrupted_lines.clear()

        for x in range(sw):
            y = columns[x]
            
            if glitch_active and y in corrupted_lines:
                # caracteres corrompidos durante glitch
                char = random.choice(['█', '▓', '▒', '░', '▄', '▀', '■', '□'])
                color_choice = random.choice([
                    curses.color_pair(2),  # vermelho
                    curses.color_pair(3),  # branco
                    curses.color_pair(5),  # magenta
                ])
            elif glitch_active and random.randint(1, 20) == 1:
                # caracteres piscando aleatoriamente
                char = chr(random.randint(33, 126))
                color_choice = curses.color_pair(4)  # amarelo
            else:
                # comportamento normal
                char = chr(random.randint(33, 126))
                color_choice = curses.color_pair(1)  # verde
            
            try:
                stdscr.addch(y, x, char, color_choice)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # adiciona linhas de erro ocasionais
        if glitch_active and random.randint(1, 30) == 1:
            error_y = random.randint(0, sh-1)
            error_msg = random.choice([
                "ERROR: SYSTEM BREACH DETECTED",
                "WARNING: UNAUTHORIZED ACCESS", 
                "CRITICAL: FIREWALL COMPROMISED",
                "ALERT: INTRUSION DETECTED",
                "FATAL: SECURITY VIOLATION"
            ])
            try:
                stdscr.addstr(error_y, max(0, sw//2 - len(error_msg)//2), 
                             error_msg[:sw], curses.color_pair(2))
            except curses.error:
                pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass