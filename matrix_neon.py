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
    glow_intensity = [0] * sw  # intensidade do brilho por coluna
    neon_pulse = 0  # pulso global do neon

    # inicializa cores neon
    curses.start_color()
    curses.use_default_colors()
    
    # Cores neon com diferentes intensidades
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # verde escuro
    curses.init_pair(2, curses.COLOR_GREEN, -1)      # verde médio
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # verde brilhante
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # ciano (brilho)
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # branco (máximo brilho)
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # magenta neon
    curses.init_pair(7, curses.COLOR_YELLOW, -1)     # amarelo neon

    neon_colors = [
        curses.color_pair(1),  # verde escuro
        curses.color_pair(2),  # verde médio
        curses.color_pair(3),  # verde brilhante
        curses.color_pair(4),  # ciano
        curses.color_pair(5),  # branco
    ]

    special_neon = [
        curses.color_pair(6),  # magenta
        curses.color_pair(7),  # amarelo
    ]

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        neon_pulse += 0.1  # pulso do efeito neon

        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # atualiza intensidade do brilho
            if random.randint(1, 10) == 1:  # 10% chance de mudança
                glow_intensity[x] = random.randint(0, 4)
            
            # efeito de pulso senoidal
            pulse_factor = (math.sin(neon_pulse + x * 0.1) + 1) / 2
            
            # escolhe cor baseada na intensidade e pulso
            if random.randint(1, 50) == 1:  # 2% chance de cor especial
                color_pair = random.choice(special_neon)
                attr = curses.A_BOLD | curses.A_BLINK
            else:
                # intensidade baseada no brilho da coluna e pulso
                intensity = min(4, int(glow_intensity[x] + pulse_factor * 2))
                color_pair = neon_colors[intensity]
                
                # adiciona atributos baseados na intensidade
                if intensity >= 4:
                    attr = curses.A_BOLD | curses.A_STANDOUT
                elif intensity >= 3:
                    attr = curses.A_BOLD
                elif intensity >= 2:
                    attr = curses.A_DIM
                else:
                    attr = 0
            
            try:
                stdscr.addch(y, x, char, color_pair | attr)
            except curses.error:
                pass

            # movimento com variação baseada no brilho
            speed_mod = max(1, glow_intensity[x] // 2 + 1)
            if random.randint(1, speed_mod) == 1:
                columns[x] = 0 if y >= sh - 1 else y + 1

        # efeito de "flash" ocasional
        if random.randint(1, 200) == 1:  # flash raro
            try:
                flash_y = random.randint(0, sh-1)
                flash_text = "█" * sw
                stdscr.addstr(flash_y, 0, flash_text[:sw], 
                             curses.color_pair(5) | curses.A_BOLD)
            except curses.error:
                pass

        # borda neon pulsante
        try:
            border_intensity = int((math.sin(neon_pulse * 2) + 1) * 2)
            border_color = neon_colors[min(4, border_intensity)]
            
            # bordas laterais
            for y in range(sh):
                if random.randint(1, 5) == 1:  # bordas esparsas
                    stdscr.addch(y, 0, '│', border_color | curses.A_BOLD)
                    if sw > 1:
                        stdscr.addch(y, sw-1, '│', border_color | curses.A_BOLD)
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass