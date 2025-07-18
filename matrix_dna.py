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
    dna_pairs = {}  # pares de bases complementares por posição
    helix_offset = 0  # offset para animação da hélice

    # bases do DNA
    dna_bases = ['A', 'T', 'G', 'C']
    
    # pares complementares
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # sequências de DNA famosas/interessantes
    famous_sequences = [
        "ATCGATCGATCG",  # sequência repetitiva
        "AAATTTGGGCCC",  # blocos de bases
        "ACGTACGTACGT",  # padrão alternado
        "TTAGGGTTAGGG",  # telômero humano
        "GAATTCGAATTC",  # sítio de restrição EcoRI
    ]

    # inicializa cores para DNA
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)        # Adenina (A)
    curses.init_pair(2, curses.COLOR_BLUE, -1)       # Timina (T)
    curses.init_pair(3, curses.COLOR_GREEN, -1)      # Guanina (G)
    curses.init_pair(4, curses.COLOR_YELLOW, -1)     # Citosina (C)
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # conectores
    curses.init_pair(6, curses.COLOR_CYAN, -1)       # destaque
    curses.init_pair(7, curses.COLOR_MAGENTA, -1)    # sequências especiais

    base_colors = {
        'A': curses.color_pair(1),  # vermelho
        'T': curses.color_pair(2),  # azul
        'G': curses.color_pair(3),  # verde
        'C': curses.color_pair(4),  # amarelo
    }

    sequence_timer = 0
    current_sequence = ""
    sequence_pos = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        helix_offset += 0.1  # animação da dupla hélice

        # gerencia sequências especiais
        sequence_timer += 1
        if sequence_timer > random.randint(200, 400):
            current_sequence = random.choice(famous_sequences)
            sequence_pos = 0
            sequence_timer = 0

        for x in range(sw):
            y = columns[x]
            
            # escolhe base de DNA
            if current_sequence and x == sw // 2 and sequence_pos < len(current_sequence):
                base = current_sequence[sequence_pos]
                sequence_pos += 1
                color = curses.color_pair(7)  # magenta para sequências especiais
                attr = curses.A_BOLD | curses.A_BLINK
            else:
                base = random.choice(dna_bases)
                color = base_colors[base]
                attr = curses.A_BOLD if random.randint(1, 10) == 1 else 0
            
            # desenha a base
            try:
                stdscr.addch(y, x, base, color | attr)
            except curses.error:
                pass

            # armazena par complementar para desenhar a dupla hélice
            dna_pairs[(x, y)] = complement[base]

            columns[x] = 0 if y >= sh - 1 else y + 1

        # desenha dupla hélice (pares complementares)
        for (x, y), comp_base in list(dna_pairs.items()):
            # calcula posição do par complementar com efeito helix
            helix_x = x + int(3 * math.sin(y * 0.2 + helix_offset))
            
            if 0 <= helix_x < sw and y < sh:
                try:
                    # desenha base complementar
                    comp_color = base_colors[comp_base]
                    stdscr.addch(y, helix_x, comp_base, comp_color)
                    
                    # desenha conector (ligação de hidrogênio)
                    if abs(helix_x - x) > 1:
                        connector_x = (x + helix_x) // 2
                        if 0 <= connector_x < sw:
                            connector_char = '─' if abs(helix_x - x) <= 3 else '~'
                            stdscr.addch(y, connector_x, connector_char, 
                                       curses.color_pair(5) | curses.A_DIM)
                except curses.error:
                    pass
            
            # remove pares antigos
            if y >= sh:
                del dna_pairs[(x, y)]

        # informações de DNA no topo
        try:
            dna_info = f"DNA SEQUENCER v3.2 | Bases: A={base_colors['A']} T={base_colors['T']} G={base_colors['G']} C={base_colors['C']}"
            stdscr.addstr(0, 0, "DNA SEQUENCER v3.2", curses.color_pair(6) | curses.A_BOLD)
            
            # contador de bases
            base_count = {base: 0 for base in dna_bases}
            for (x, y) in dna_pairs.keys():
                if y < sh:
                    # conta bases na tela atual (aproximação)
                    base_count[random.choice(dna_bases)] += 1
            
            count_str = " | ".join([f"{base}:{count}" for base, count in base_count.items()])
            if len(count_str) < sw - 20:
                stdscr.addstr(1, 0, count_str, curses.color_pair(5))
        except curses.error:
            pass

        # indicador de sequência especial
        if current_sequence:
            try:
                progress = min(100, (sequence_pos * 100) // len(current_sequence))
                seq_info = f"ANALYZING: {current_sequence} ({progress}%)"
                stdscr.addstr(sh-1, 0, seq_info[:sw], curses.color_pair(7))
            except curses.error:
                pass

        # legenda das cores
        try:
            legend = "A=Red T=Blue G=Green C=Yellow"
            stdscr.addstr(sh-2, sw - len(legend), legend, curses.color_pair(6))
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        import math
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass