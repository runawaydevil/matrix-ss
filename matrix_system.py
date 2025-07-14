#!/usr/bin/env python3
import curses
import random
import time
import psutil
import socket
import datetime
import os

def get_system_info():
    """Coleta informações do sistema"""
    try:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        
        # Memory usage
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        # Disk usage
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        
        # IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        # Current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Current date
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        # Username
        username = os.getlogin()
        
        # System load (Linux only)
        try:
            load_avg = os.getloadavg()
            load_1min = load_avg[0]
        except:
            load_1min = "N/A"
        
        return {
            'cpu': f"CPU: {cpu_percent}%",
            'memory': f"MEM: {memory_percent}%",
            'disk': f"DISK: {disk_percent}%",
            'ip': f"IP: {ip_address}",
            'time': f"TIME: {current_time}",
            'date': f"DATE: {current_date}",
            'user': f"USER: {username}",
            'load': f"LOAD: {load_1min:.2f}" if load_1min != "N/A" else "LOAD: N/A"
        }
    except Exception as e:
        return {
            'cpu': "CPU: ERROR",
            'memory': "MEM: ERROR",
            'disk': "DISK: ERROR",
            'ip': "IP: ERROR",
            'time': "TIME: ERROR",
            'date': "DATE: ERROR",
            'user': "USER: ERROR",
            'load': "LOAD: ERROR"
        }

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)  # espera de input e taxa de atualização do loop (ms)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw  # posição y para cada coluna

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)   # verde para chuva
    curses.init_pair(2, curses.COLOR_RED, -1)     # vermelho para info do sistema
    curses.init_pair(3, curses.COLOR_YELLOW, -1)  # amarelo para destaque

    # define área central para informações do sistema
    center_x = sw // 2
    center_y = sh // 2
    info_width = 20
    info_start_x = center_x - info_width // 2

    # lista de informações do sistema
    system_info_keys = ['cpu', 'memory', 'disk', 'ip', 'time', 'date', 'user', 'load']
    
    # contador para atualizar informações
    update_counter = 0
    system_info = get_system_info()

    while True:
        # detecta tecla 'q' para sair
        key = stdscr.getch()
        if key == ord('q'):
            break

        # atualiza informações do sistema a cada 20 frames (~1 segundo)
        update_counter += 1
        if update_counter >= 20:
            system_info = get_system_info()
            update_counter = 0

        # não limpa a tela para acumular caracteres
        for x in range(sw):
            y = columns[x]
            char = chr(random.randint(33, 126))
            
            # verifica se está na área central de informações
            if (info_start_x <= x < info_start_x + info_width and 
                center_y - 4 <= y <= center_y + 4):
                # pula esta posição para não interferir com as informações
                continue
            
            try:
                stdscr.addch(y, x, char, curses.color_pair(1))
            except curses.error:
                pass

            # atualiza posição, reinicia no topo se ultrapassar altura
            columns[x] = 0 if y >= sh - 1 else y + 1

        # desenha informações do sistema no centro
        try:
            # título
            title = "SYSTEM STATUS"
            title_x = center_x - len(title) // 2
            stdscr.addstr(center_y - 4, title_x, title, curses.color_pair(3))
            
            # informações do sistema
            y_offset = center_y - 2
            for i, key in enumerate(system_info_keys):
                if y_offset + i < sh - 1:  # evita sair da tela
                    info_text = system_info[key]
                    x_pos = info_start_x
                    stdscr.addstr(y_offset + i, x_pos, info_text, curses.color_pair(2))
            
            # borda decorativa
            border_top = "=" * info_width
            border_bottom = "=" * info_width
            stdscr.addstr(center_y - 5, info_start_x, border_top, curses.color_pair(3))
            stdscr.addstr(center_y + 3, info_start_x, border_bottom, curses.color_pair(3))
            
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)  # ajusta taxa de quadros (~20 fps)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass 