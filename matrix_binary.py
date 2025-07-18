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
    binary_streams = [[] for _ in range(sw)]  # streams de dados binários por coluna

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # verde normal
    curses.init_pair(2, curses.COLOR_WHITE, -1)      # branco (destaque)
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # verde escuro
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # ciano (dados especiais)

    # mensagens ocultas em binário
    hidden_messages = [
        "01001000 01100101 01101100 01101100 01101111",  # "Hello"
        "01001101 01100001 01110100 01110010 01101001 01111000",  # "Matrix"
        "01001110 01100101 01101111",  # "Neo"
        "01010111 01100001 01101011 01100101 00100000 01110101 01110000",  # "Wake up"
    ]

    message_timer = 0
    current_message = ""
    message_pos = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # gerencia mensagens ocultas
        message_timer += 1
        if message_timer > random.randint(300, 600):  # a cada 15-30 segundos
            current_message = random.choice(hidden_messages)
            message_pos = 0
            message_timer = 0

        for x in range(sw):
            y = columns[x]
            
            # escolhe apenas 0 ou 1
            char = random.choice(['0', '1'])
            
            # 90% dos caracteres são 0 ou 1 normais
            if random.randint(1, 100) <= 90:
                color_pair = curses.color_pair(1)  # verde normal
                attr = 0
            # 8% são destacados em branco
            elif random.randint(1, 100) <= 98:
                color_pair = curses.color_pair(2)  # branco
                attr = curses.A_BOLD
            # 2% são dados especiais em ciano
            else:
                color_pair = curses.color_pair(4)  # ciano
                attr = curses.A_BOLD
            
            # insere mensagem oculta ocasionalmente
            if current_message and x == sw // 2 and random.randint(1, 20) == 1:
                if message_pos < len(current_message):
                    char = current_message[message_pos]
                    message_pos += 1
                    color_pair = curses.color_pair(2)
                    attr = curses.A_BOLD | curses.A_BLINK
            
            try:
                stdscr.addch(y, x, char, color_pair | attr)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # efeito de "data stream" - linhas horizontais ocasionais
        if random.randint(1, 100) == 1:
            try:
                stream_y = random.randint(0, sh-1)
                stream_data = ''.join(random.choice(['0', '1']) for _ in range(sw))
                stdscr.addstr(stream_y, 0, stream_data[:sw], 
                             curses.color_pair(4) | curses.A_BOLD)
            except curses.error:
                pass

        # contador binário no canto
        try:
            frame_count = int(time.time()) % 256
            binary_count = format(frame_count, '08b')
            stdscr.addstr(0, 0, f"[{binary_count}]", 
                         curses.color_pair(2) | curses.A_BOLD)
        except curses.error:
            pass

        # indicador de mensagem oculta
        if current_message:
            try:
                progress = min(100, (message_pos * 100) // len(current_message))
                indicator = f"DECODING: {progress:3d}%"
                stdscr.addstr(sh-1, sw - len(indicator), indicator, 
                             curses.color_pair(4))
            except curses.error:
                pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass