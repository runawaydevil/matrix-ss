#!/usr/bin/env python3
import curses
import random
import time
import math

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    wave_offset = 0

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, curses.COLOR_WHITE, -1)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        wave_offset += 0.2  # velocidade da onda

        for x in range(sw):
            # calcula posição y baseada em onda senoidal
            wave_y = int(sh/2 + (sh/4) * math.sin((x + wave_offset) * 0.1))
            
            # chuva normal
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # cor baseada na proximidade com a onda
            distance_to_wave = abs(y - wave_y)
            if distance_to_wave < 3:
                color_pair = curses.color_pair(4)  # branco (próximo à onda)
            elif distance_to_wave < 6:
                color_pair = curses.color_pair(2)  # ciano
            elif distance_to_wave < 10:
                color_pair = curses.color_pair(3)  # azul
            else:
                color_pair = curses.color_pair(1)  # verde normal
            
            try:
                stdscr.addch(y, x, char, color_pair)
            except curses.error:
                pass

            # movimento da coluna com influência da onda
            wave_influence = math.sin((x + wave_offset) * 0.05)
            if wave_influence > 0.5:
                columns[x] = 0 if y >= sh - 1 else y + 2  # mais rápido
            elif wave_influence < -0.5:
                if random.randint(1, 3) == 1:  # mais lento
                    columns[x] = 0 if y >= sh - 1 else y + 1
            else:
                columns[x] = 0 if y >= sh - 1 else y + 1  # velocidade normal

        # desenha linha da onda
        for x in range(sw):
            wave_y = int(sh/2 + (sh/4) * math.sin((x + wave_offset) * 0.1))
            if 0 <= wave_y < sh:
                try:
                    stdscr.addch(wave_y, x, '~', curses.color_pair(4) | curses.A_BOLD)
                except curses.error:
                    pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass