#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)  # espera de input e taxa de atualização do loop (ms)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw  # posição y para cada coluna

    # inicializa cor
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)

    while True:
        # detecta tecla 'q' para sair
        key = stdscr.getch()
        if key == ord('q'):
            break

        # não limpa a tela para acumular caracteres
        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            try:
                stdscr.addch(y, x, char, curses.color_pair(1))
            except curses.error:
                pass

            # atualiza posição, reinicia no topo se ultrapassar altura
            columns[x] = 0 if y >= sh - 1 else y + 1

        stdscr.refresh()
        time.sleep(0.05)  # ajusta taxa de quadros (~20 fps)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
