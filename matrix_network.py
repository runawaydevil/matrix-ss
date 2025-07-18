#!/usr/bin/env python3
import curses
import random
import time
import socket
import subprocess
import sys

def get_network_info():
    """Coleta informações de rede"""
    try:
        # IP local
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        # Tenta obter informações de rede mais detalhadas
        try:
            # Conexões ativas (simulado para compatibilidade)
            active_connections = random.randint(5, 25)
            
            # Tráfego simulado (em produção, usar psutil.net_io_counters())
            bytes_sent = random.randint(1000000, 10000000)
            bytes_recv = random.randint(2000000, 20000000)
            
            # Portas abertas simuladas
            open_ports = [22, 80, 443, 8080, 3306, 5432]
            active_ports = random.sample(open_ports, random.randint(2, 4))
            
            return {
                'hostname': hostname,
                'local_ip': local_ip,
                'connections': active_connections,
                'bytes_sent': bytes_sent,
                'bytes_recv': bytes_recv,
                'ports': active_ports,
                'status': 'ONLINE'
            }
        except:
            return {
                'hostname': hostname,
                'local_ip': local_ip,
                'connections': 0,
                'bytes_sent': 0,
                'bytes_recv': 0,
                'ports': [],
                'status': 'LIMITED'
            }
    except Exception as e:
        return {
            'hostname': 'unknown',
            'local_ip': '127.0.0.1',
            'connections': 0,
            'bytes_sent': 0,
            'bytes_recv': 0,
            'ports': [],
            'status': 'ERROR'
        }

def format_bytes(bytes_val):
    """Formata bytes em unidades legíveis"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.1f}{unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.1f}TB"

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    
    # simulação de pacotes de rede
    network_packets = []
    packet_types = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'SSH', 'FTP', 'DNS', 'ICMP']
    
    # IPs simulados para tráfego
    ip_ranges = [
        '192.168.1.', '10.0.0.', '172.16.0.', '8.8.8.', '1.1.1.', 
        '208.67.222.', '74.125.224.', '151.101.193.'
    ]

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # tráfego normal
    curses.init_pair(2, curses.COLOR_YELLOW, -1)     # tráfego médio
    curses.init_pair(3, curses.COLOR_RED, -1)        # tráfego alto
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # informações
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # destaque
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # alertas
    curses.init_pair(7, curses.COLOR_BLUE, -1)       # dados

    update_timer = 0
    network_info = get_network_info()

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # atualiza informações de rede periodicamente
        update_timer += 1
        if update_timer >= 100:  # a cada 5 segundos
            network_info = get_network_info()
            update_timer = 0

        # chuva matrix com caracteres de rede
        network_chars = list("0123456789ABCDEF.:/-")
        
        for x in range(sw):
            y = columns[x]
            
            # 70% caracteres normais, 30% caracteres de rede
            if random.randint(1, 10) <= 7:
                char = chr(random.randint(33, 126))
                color = curses.color_pair(1)
            else:
                char = random.choice(network_chars)
                # cor baseada no tipo de tráfego
                traffic_level = random.randint(1, 100)
                if traffic_level > 80:
                    color = curses.color_pair(3)  # vermelho (alto)
                elif traffic_level > 50:
                    color = curses.color_pair(2)  # amarelo (médio)
                else:
                    color = curses.color_pair(1)  # verde (normal)
            
            try:
                stdscr.addch(y, x, char, color)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # simula pacotes de rede atravessando a tela
        if random.randint(1, 20) == 1:
            packet_type = random.choice(packet_types)
            src_ip = random.choice(ip_ranges) + str(random.randint(1, 254))
            dst_ip = random.choice(ip_ranges) + str(random.randint(1, 254))
            port = random.choice([22, 80, 443, 8080, 21, 53, 25])
            
            packet_info = f"{packet_type} {src_ip}:{port} -> {dst_ip}"
            packet_y = random.randint(2, sh-3)
            
            try:
                stdscr.addstr(packet_y, 0, packet_info[:sw], 
                             curses.color_pair(4) | curses.A_BOLD)
            except curses.error:
                pass

        # painel de informações de rede
        try:
            # título
            title = "NETWORK MONITOR v1.0"
            stdscr.addstr(0, 0, title, curses.color_pair(5) | curses.A_BOLD)
            
            # informações básicas
            info_lines = [
                f"HOST: {network_info['hostname']}",
                f"IP: {network_info['local_ip']}",
                f"STATUS: {network_info['status']}",
                f"CONNECTIONS: {network_info['connections']}",
                f"SENT: {format_bytes(network_info['bytes_sent'])}",
                f"RECV: {format_bytes(network_info['bytes_recv'])}",
            ]
            
            for i, line in enumerate(info_lines):
                if i + 1 < sh:
                    color = curses.color_pair(4) if network_info['status'] == 'ONLINE' else curses.color_pair(6)
                    stdscr.addstr(i + 1, 0, line[:sw], color)
            
            # portas abertas
            if network_info['ports']:
                ports_str = "PORTS: " + ",".join(map(str, network_info['ports']))
                if len(info_lines) + 1 < sh:
                    stdscr.addstr(len(info_lines) + 1, 0, ports_str[:sw], curses.color_pair(7))
            
            # indicador de atividade
            activity_chars = ['|', '/', '-', '\\']
            activity_char = activity_chars[int(time.time() * 4) % 4]
            activity_text = f"ACTIVITY {activity_char}"
            stdscr.addstr(0, sw - len(activity_text), activity_text, 
                         curses.color_pair(2) | curses.A_BOLD)
            
        except curses.error:
            pass

        # barra de tráfego na parte inferior
        try:
            traffic_level = random.randint(0, 100)
            bar_width = min(sw - 20, 50)
            filled_width = (traffic_level * bar_width) // 100
            
            traffic_bar = "█" * filled_width + "░" * (bar_width - filled_width)
            traffic_text = f"TRAFFIC: {traffic_level:3d}% [{traffic_bar}]"
            
            color = curses.color_pair(1)
            if traffic_level > 80:
                color = curses.color_pair(3)
            elif traffic_level > 50:
                color = curses.color_pair(2)
            
            stdscr.addstr(sh-1, 0, traffic_text[:sw], color)
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass