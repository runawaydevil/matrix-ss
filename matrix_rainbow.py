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

    # inicializa cores do arco-íris
    curses.start_color()
    curses.use_default_colors()
    
    # define pares de cores do arco-íris
    curses.init_pair(1, curses.COLOR_RED, -1)        # vermelho
    curses.init_pair(2, curses.COLOR_YELLOW, -1)     # amarelo
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # verde
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # ciano
    curses.init_pair(5, curses.COLOR_BLUE, -1)       # azul
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # magenta
    curses.init_pair(7, curses.COLOR_WHITE, -1)      # branco (brilho)

    # lista de cores do arco-íris
    rainbow_colors = [
        curses.color_pair(1),  # vermelho
        curses.color_pair(2),  # amarelo
        curses.color_pair(3),  # verde
        curses.color_pair(4),  # ciano
        curses.color_pair(5),  # azul
        curses.color_pair(6),  # magenta
        curses.color_pair(7),  # branco
    ]

    while True:
        # detecta tecla 'q' para sair
        key = stdscr.getch()
        if key == ord('q'):
            break

        # não limpa a tela para acumular caracteres
        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # escolhe cor aleatória do arco-íris
            color_pair = random.choice(rainbow_colors)
            
            try:
                stdscr.addch(y, x, char, color_pair)
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