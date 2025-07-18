#!/usr/bin/env python3
import curses
import random
import time
import json

def get_crypto_data():
    """Simula dados de criptomoedas (em produção, usar API real)"""
    # Dados simulados realistas
    cryptos = {
        'BTC': {
            'name': 'Bitcoin',
            'price': random.uniform(40000, 70000),
            'change': random.uniform(-5, 5),
            'symbol': '₿'
        },
        'ETH': {
            'name': 'Ethereum', 
            'price': random.uniform(2500, 4000),
            'change': random.uniform(-8, 8),
            'symbol': 'Ξ'
        },
        'ADA': {
            'name': 'Cardano',
            'price': random.uniform(0.3, 1.2),
            'change': random.uniform(-10, 10),
            'symbol': '₳'
        },
        'DOT': {
            'name': 'Polkadot',
            'price': random.uniform(5, 15),
            'change': random.uniform(-12, 12),
            'symbol': '●'
        },
        'LINK': {
            'name': 'Chainlink',
            'price': random.uniform(8, 25),
            'change': random.uniform(-15, 15),
            'symbol': '⬢'
        },
        'XRP': {
            'name': 'Ripple',
            'price': random.uniform(0.4, 1.5),
            'change': random.uniform(-20, 20),
            'symbol': '◊'
        }
    }
    
    return cryptos

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    
    # símbolos relacionados a crypto
    crypto_chars = list("₿ΞΞ₳●⬢◊$€¥£₹₽₩₪₫₡₦₨₱₴₵₶₷₸₹₺₻₼₽₾₿")
    
    # inicializa cores
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)      # alta (positivo)
    curses.init_pair(2, curses.COLOR_RED, -1)        # baixa (negativo)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)     # neutro
    curses.init_pair(4, curses.COLOR_CYAN, -1)       # informações
    curses.init_pair(5, curses.COLOR_WHITE, -1)      # destaque
    curses.init_pair(6, curses.COLOR_MAGENTA, -1)    # símbolos crypto
    curses.init_pair(7, curses.COLOR_BLUE, -1)       # dados

    update_timer = 0
    crypto_data = get_crypto_data()
    price_history = {symbol: [] for symbol in crypto_data.keys()}

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # atualiza dados de crypto periodicamente
        update_timer += 1
        if update_timer >= 60:  # a cada 3 segundos
            crypto_data = get_crypto_data()
            
            # mantém histórico de preços
            for symbol, data in crypto_data.items():
                price_history[symbol].append(data['price'])
                if len(price_history[symbol]) > 20:  # mantém últimos 20 valores
                    price_history[symbol].pop(0)
            
            update_timer = 0

        # chuva matrix com símbolos crypto
        for x in range(sw):
            y = columns[x]
            
            # 60% caracteres normais, 40% símbolos crypto
            if random.randint(1, 10) <= 6:
                char = chr(random.randint(33, 126))
                color = curses.color_pair(1)
            else:
                char = random.choice(crypto_chars)
                color = curses.color_pair(6)  # magenta para símbolos crypto
            
            try:
                stdscr.addch(y, x, char, color)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # painel de preços de criptomoedas
        panel_width = min(sw - 2, 60)
        panel_height = min(sh - 4, len(crypto_data) + 4)
        panel_x = (sw - panel_width) // 2
        panel_y = 2

        try:
            # borda do painel
            stdscr.addstr(panel_y - 1, panel_x - 1, 
                         "┌" + "─" * panel_width + "┐", 
                         curses.color_pair(5))
            stdscr.addstr(panel_y + panel_height, panel_x - 1, 
                         "└" + "─" * panel_width + "┘", 
                         curses.color_pair(5))
            
            for i in range(panel_height):
                stdscr.addch(panel_y + i, panel_x - 1, '│', curses.color_pair(5))
                stdscr.addch(panel_y + i, panel_x + panel_width, '│', curses.color_pair(5))
            
            # título
            title = " CRYPTO MATRIX TRACKER "
            title_x = panel_x + (panel_width - len(title)) // 2
            stdscr.addstr(panel_y - 1, title_x, title, 
                         curses.color_pair(6) | curses.A_BOLD)
            
            # cabeçalho
            header = f"{'COIN':<8} {'PRICE':<12} {'CHANGE':<10} {'TREND':<8}"
            stdscr.addstr(panel_y, panel_x, header[:panel_width], 
                         curses.color_pair(5) | curses.A_BOLD)
            
            # linha separadora
            separator = "─" * panel_width
            stdscr.addstr(panel_y + 1, panel_x, separator[:panel_width], 
                         curses.color_pair(5))
            
            # dados das criptomoedas
            for i, (symbol, data) in enumerate(crypto_data.items()):
                if i + 2 < panel_height:
                    # formata preço
                    if data['price'] > 1000:
                        price_str = f"${data['price']:,.0f}"
                    elif data['price'] > 1:
                        price_str = f"${data['price']:.2f}"
                    else:
                        price_str = f"${data['price']:.4f}"
                    
                    # formata mudança
                    change_str = f"{data['change']:+.2f}%"
                    
                    # determina tendência
                    if len(price_history[symbol]) >= 2:
                        if price_history[symbol][-1] > price_history[symbol][-2]:
                            trend = "↗ UP"
                            trend_color = curses.color_pair(1)
                        elif price_history[symbol][-1] < price_history[symbol][-2]:
                            trend = "↘ DOWN"
                            trend_color = curses.color_pair(2)
                        else:
                            trend = "→ FLAT"
                            trend_color = curses.color_pair(3)
                    else:
                        trend = "─ NEW"
                        trend_color = curses.color_pair(3)
                    
                    # cor baseada na mudança
                    if data['change'] > 0:
                        change_color = curses.color_pair(1)  # verde
                    elif data['change'] < 0:
                        change_color = curses.color_pair(2)  # vermelho
                    else:
                        change_color = curses.color_pair(3)  # amarelo
                    
                    # linha da moeda
                    coin_line = f"{symbol:<8} {price_str:<12}"
                    stdscr.addstr(panel_y + i + 2, panel_x, coin_line, curses.color_pair(4))
                    
                    # mudança percentual
                    stdscr.addstr(panel_y + i + 2, panel_x + 21, change_str, change_color | curses.A_BOLD)
                    
                    # tendência
                    stdscr.addstr(panel_y + i + 2, panel_x + 32, trend, trend_color | curses.A_BOLD)
            
            # timestamp
            timestamp = time.strftime("%H:%M:%S")
            time_text = f"Last Update: {timestamp}"
            stdscr.addstr(panel_y + panel_height - 1, panel_x, time_text, curses.color_pair(7))
            
        except curses.error:
            pass

        # indicadores de mercado na parte inferior
        try:
            # calcula índice geral do mercado
            total_change = sum(data['change'] for data in crypto_data.values())
            avg_change = total_change / len(crypto_data)
            
            if avg_change > 2:
                market_status = "BULL MARKET 🚀"
                market_color = curses.color_pair(1)
            elif avg_change < -2:
                market_status = "BEAR MARKET 📉"
                market_color = curses.color_pair(2)
            else:
                market_status = "SIDEWAYS 📊"
                market_color = curses.color_pair(3)
            
            market_text = f"MARKET: {market_status} | AVG: {avg_change:+.2f}%"
            stdscr.addstr(sh-1, 0, market_text[:sw], market_color | curses.A_BOLD)
            
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass