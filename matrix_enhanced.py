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
    columns = [0] * sw  # posição y para cada coluna
    speeds = [random.randint(1, 4) for _ in range(sw)]  # velocidade individual por coluna
    trails = [[' ' for _ in range(sh)] for _ in range(sw)]  # rastro de caracteres
    trail_ages = [[0 for _ in range(sh)] for _ in range(sw)]  # idade dos caracteres

    # caracteres japoneses/katakana para autenticidade
    katakana_chars = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    ascii_chars = "".join([chr(i) for i in range(33, 127)])
    all_chars = katakana_chars + ascii_chars

    # inicializa cores com diferentes intensidades
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # verde brilhante
    curses.init_pair(2, curses.COLOR_GREEN, -1)      # verde médio  
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # verde escuro
    curses.init_pair(4, curses.COLOR_WHITE, -1)      # branco (ponta)

    frame_count = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        stdscr.clear()
        
        for x in range(sw):
            # atualiza posição baseada na velocidade da coluna
            if frame_count % (5 - speeds[x]) == 0:  # colunas mais rápidas atualizam mais frequentemente
                y = columns[x]
                
                # escolhe caractere (70% katakana, 30% ASCII)
                if random.random() < 0.7:
                    char = random.choice(katakana_chars)
                else:
                    char = random.choice(ascii_chars)
                
                # adiciona ao rastro
                if y < sh:
                    trails[x][y] = char
                    trail_ages[x][y] = 0
                
                # atualiza posição
                columns[x] = 0 if y >= sh - 1 else y + 1
            
            # desenha rastro com fade
            for y in range(sh):
                if trails[x][y] != ' ':
                    age = trail_ages[x][y]
                    
                    # escolhe cor baseada na idade
                    if age == 0:
                        color = curses.color_pair(4)  # branco (mais novo)
                    elif age < 3:
                        color = curses.color_pair(1)  # verde brilhante
                    elif age < 8:
                        color = curses.color_pair(2)  # verde médio
                    elif age < 15:
                        color = curses.color_pair(3)  # verde escuro
                    else:
                        trails[x][y] = ' '  # remove caractere muito antigo
                        continue
                    
                    try:
                        stdscr.addch(y, x, trails[x][y], color)
                    except curses.error:
                        pass
                    
                    # envelhece caractere
                    trail_ages[x][y] += 1

        stdscr.refresh()
        frame_count += 1
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass