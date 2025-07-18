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
    heat_levels = [0] * sw  # nível de "calor" por coluna

    # inicializa cores do fogo
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, -1)       # azul (frio)
    curses.init_pair(2, curses.COLOR_CYAN, -1)       # ciano
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # verde
    curses.init_pair(4, curses.COLOR_YELLOW, -1)     # amarelo
    curses.init_pair(5, curses.COLOR_RED, -1)        # vermelho
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # magenta (muito quente)
    curses.init_pair(7, curses.COLOR_WHITE, -1)      # branco (máximo calor)

    fire_colors = [
        curses.color_pair(1),  # azul
        curses.color_pair(2),  # ciano  
        curses.color_pair(3),  # verde
        curses.color_pair(4),  # amarelo
        curses.color_pair(5),  # vermelho
        curses.color_pair(6),  # magenta
        curses.color_pair(7),  # branco
    ]

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # atualiza nível de calor da coluna
            heat_change = random.randint(-1, 2)  # pode esfriar ou esquentar
            heat_levels[x] = max(0, min(6, heat_levels[x] + heat_change))
            
            # escolhe cor baseada no calor
            color_pair = fire_colors[heat_levels[x]]
            
            try:
                stdscr.addch(y, x, char, color_pair)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass