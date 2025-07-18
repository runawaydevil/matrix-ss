#!/usr/bin/env python3
import curses
import random
import time

def create_ascii_art():
    """Cria uma arte ASCII simples para revelar"""
    art = [
        "    ╔══════════════════╗    ",
        "    ║   MATRIX  CODE   ║    ",
        "    ║                  ║    ",
        "    ║ ┌─────────────┐  ║    ",
        "    ║ │ WAKE UP NEO │  ║    ",
        "    ║ └─────────────┘  ║    ",
        "    ║                  ║    ",
        "    ║  THE MATRIX HAS  ║    ",
        "    ║      YOU...      ║    ",
        "    ║                  ║    ",
        "    ╚══════════════════╝    "
    ]
    return art

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    
    # arte ASCII para revelar
    ascii_art = create_ascii_art()
    art_height = len(ascii_art)
    art_width = max(len(line) for line in ascii_art)
    
    # posição central da arte
    art_start_y = max(0, (sh - art_height) // 2)
    art_start_x = max(0, (sw - art_width) // 2)
    
    # controle de revelação
    reveal_progress = 0
    max_reveal = art_height * art_width
    revealed_pixels = set()

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # chuva
    curses.init_pair(2, curses.COLOR_WHITE, -1)      # arte revelada
    curses.init_pair(3, curses.COLOR_YELLOW, -1)     # arte sendo revelada
    curses.init_pair(4, curses.COLOR_RED, -1)        # destaque

    frame_count = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # chuva matrix normal
        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # verifica se está na área da arte
            art_y = y - art_start_y
            art_x = x - art_start_x
            
            is_art_area = (0 <= art_y < art_height and 
                          0 <= art_x < art_width and
                          art_x < len(ascii_art[art_y]))
            
            if is_art_area:
                # área da arte - pode revelar pixel
                pixel_id = (art_y, art_x)
                if pixel_id not in revealed_pixels and random.randint(1, 100) <= 2:
                    revealed_pixels.add(pixel_id)
                    reveal_progress += 1
            else:
                # área normal - chuva verde
                try:
                    stdscr.addch(y, x, char, curses.color_pair(1))
                except curses.error:
                    pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # desenha arte revelada
        for art_y in range(art_height):
            for art_x in range(len(ascii_art[art_y])):
                pixel_id = (art_y, art_x)
                if pixel_id in revealed_pixels:
                    screen_y = art_start_y + art_y
                    screen_x = art_start_x + art_x
                    
                    if 0 <= screen_y < sh and 0 <= screen_x < sw:
                        char = ascii_art[art_y][art_x]
                        
                        # cor baseada no progresso
                        if reveal_progress > max_reveal * 0.8:
                            color = curses.color_pair(4)  # vermelho (completo)
                        elif reveal_progress > max_reveal * 0.5:
                            color = curses.color_pair(2)  # branco
                        else:
                            color = curses.color_pair(3)  # amarelo
                        
                        try:
                            stdscr.addch(screen_y, screen_x, char, color)
                        except curses.error:
                            pass

        # barra de progresso
        progress_percent = min(100, (reveal_progress * 100) // max_reveal)
        progress_bar = "█" * (progress_percent // 5)
        progress_text = f"DECODING: {progress_percent:3d}% [{progress_bar:<20}]"
        
        try:
            stdscr.addstr(sh-1, 0, progress_text[:sw], curses.color_pair(3))
        except curses.error:
            pass

        # mensagem quando completamente revelado
        if reveal_progress >= max_reveal:
            try:
                complete_msg = "DECODING COMPLETE - PRESS 'Q' TO EXIT"
                msg_x = max(0, (sw - len(complete_msg)) // 2)
                stdscr.addstr(sh-2, msg_x, complete_msg, 
                             curses.color_pair(4) | curses.A_BOLD)
            except curses.error:
                pass

        stdscr.refresh()
        frame_count += 1
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass