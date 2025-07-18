#!/usr/bin/env python3
import curses
import random
import time
import datetime

def get_weather_data():
    """Simula dados meteorológicos (em produção, usar API real como OpenWeatherMap)"""
    
    # Condições climáticas possíveis
    conditions = [
        {'name': 'Sunny', 'icon': '☀️', 'temp_range': (20, 35), 'humidity_range': (30, 60)},
        {'name': 'Cloudy', 'icon': '☁️', 'temp_range': (15, 25), 'humidity_range': (50, 80)},
        {'name': 'Rainy', 'icon': '🌧️', 'temp_range': (10, 20), 'humidity_range': (70, 95)},
        {'name': 'Stormy', 'icon': '⛈️', 'temp_range': (12, 22), 'humidity_range': (80, 95)},
        {'name': 'Snowy', 'icon': '❄️', 'temp_range': (-5, 5), 'humidity_range': (60, 90)},
        {'name': 'Foggy', 'icon': '🌫️', 'temp_range': (5, 15), 'humidity_range': (85, 95)},
    ]
    
    # Seleciona condição aleatória
    condition = random.choice(conditions)
    
    # Gera dados baseados na condição
    temperature = random.uniform(*condition['temp_range'])
    humidity = random.randint(*condition['humidity_range'])
    pressure = random.randint(980, 1030)  # hPa
    wind_speed = random.uniform(0, 25)  # km/h
    wind_direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    uv_index = random.randint(0, 11)
    visibility = random.randint(1, 20)  # km
    
    return {
        'condition': condition['name'],
        'icon': condition['icon'],
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'wind_direction': wind_direction,
        'uv_index': uv_index,
        'visibility': visibility,
        'location': 'Matrix City'
    }

def get_weather_chars(condition):
    """Retorna caracteres específicos para cada condição climática"""
    weather_chars = {
        'Sunny': list('☀️*·°'),
        'Cloudy': list('☁️~≈∼'),
        'Rainy': list('🌧️|/\\·'),
        'Stormy': list('⛈️⚡*!'),
        'Snowy': list('❄️*·○'),
        'Foggy': list('🌫️~≈∼')
    }
    return weather_chars.get(condition, list('·~*'))

def main(stdscr):
    # configura terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    
    # inicializa cores baseadas no clima
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, -1)     # ensolarado
    curses.init_pair(2, curses.COLOR_WHITE, -1)      # nublado
    curses.init_pair(3, curses.COLOR_BLUE, -1)       # chuvoso
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)    # tempestade
    curses.init_pair(5, curses.COLOR_CYAN, -1)       # neve
    curses.init_pair(6, curses.COLOR_GREEN, -1)      # informações
    curses.init_pair(7, curses.COLOR_RED, -1)        # alertas

    weather_colors = {
        'Sunny': curses.color_pair(1),
        'Cloudy': curses.color_pair(2),
        'Rainy': curses.color_pair(3),
        'Stormy': curses.color_pair(4),
        'Snowy': curses.color_pair(5),
        'Foggy': curses.color_pair(2)
    }

    update_timer = 0
    weather_data = get_weather_data()
    weather_chars = get_weather_chars(weather_data['condition'])

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

        # atualiza dados meteorológicos periodicamente
        update_timer += 1
        if update_timer >= 200:  # a cada 10 segundos
            weather_data = get_weather_data()
            weather_chars = get_weather_chars(weather_data['condition'])
            update_timer = 0

        # chuva matrix com caracteres climáticos
        for x in range(sw):
            y = columns[x]
            
            # 70% caracteres normais, 30% caracteres climáticos
            if random.randint(1, 10) <= 7:
                char = chr(random.randint(33, 126))
                color = curses.color_pair(6)
            else:
                char = random.choice(weather_chars)
                color = weather_colors[weather_data['condition']]
            
            try:
                stdscr.addch(y, x, char, color)
            except curses.error:
                pass

            columns[x] = 0 if y >= sh - 1 else y + 1

        # painel meteorológico
        panel_width = min(sw - 4, 50)
        panel_height = min(sh - 6, 12)
        panel_x = (sw - panel_width) // 2
        panel_y = 3

        try:
            # borda do painel
            stdscr.addstr(panel_y - 1, panel_x - 1, 
                         "┌" + "─" * panel_width + "┐", 
                         curses.color_pair(6))
            stdscr.addstr(panel_y + panel_height, panel_x - 1, 
                         "└" + "─" * panel_width + "┘", 
                         curses.color_pair(6))
            
            for i in range(panel_height):
                stdscr.addch(panel_y + i, panel_x - 1, '│', curses.color_pair(6))
                stdscr.addch(panel_y + i, panel_x + panel_width, '│', curses.color_pair(6))
            
            # título
            title = f" WEATHER MATRIX - {weather_data['location']} "
            title_x = panel_x + (panel_width - len(title)) // 2
            stdscr.addstr(panel_y - 1, title_x, title, 
                         curses.color_pair(1) | curses.A_BOLD)
            
            # condição principal
            main_condition = f"{weather_data['icon']} {weather_data['condition']}"
            temp_str = f"{weather_data['temperature']:.1f}°C"
            
            # centraliza condição e temperatura
            condition_x = panel_x + (panel_width - len(main_condition)) // 2
            temp_x = panel_x + (panel_width - len(temp_str)) // 2
            
            stdscr.addstr(panel_y + 1, condition_x, main_condition, 
                         weather_colors[weather_data['condition']] | curses.A_BOLD)
            stdscr.addstr(panel_y + 2, temp_x, temp_str, 
                         curses.color_pair(1) | curses.A_BOLD)
            
            # linha separadora
            separator = "─" * panel_width
            stdscr.addstr(panel_y + 3, panel_x, separator[:panel_width], 
                         curses.color_pair(6))
            
            # detalhes meteorológicos
            details = [
                f"Humidity: {weather_data['humidity']}%",
                f"Pressure: {weather_data['pressure']} hPa",
                f"Wind: {weather_data['wind_speed']:.1f} km/h {weather_data['wind_direction']}",
                f"UV Index: {weather_data['uv_index']}/11",
                f"Visibility: {weather_data['visibility']} km"
            ]
            
            for i, detail in enumerate(details):
                if i + 4 < panel_height:
                    stdscr.addstr(panel_y + i + 4, panel_x + 2, detail, curses.color_pair(6))
            
            # timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_text = f"Updated: {timestamp}"
            stdscr.addstr(panel_y + panel_height - 1, panel_x + 2, time_text[:panel_width-4], 
                         curses.color_pair(2))
            
        except curses.error:
            pass

        # alertas meteorológicos
        try:
            alerts = []
            
            if weather_data['temperature'] > 30:
                alerts.append("HIGH TEMPERATURE WARNING")
            elif weather_data['temperature'] < 0:
                alerts.append("FREEZING TEMPERATURE ALERT")
            
            if weather_data['wind_speed'] > 20:
                alerts.append("HIGH WIND WARNING")
            
            if weather_data['uv_index'] > 8:
                alerts.append("HIGH UV INDEX ALERT")
            
            if weather_data['visibility'] < 5:
                alerts.append("LOW VISIBILITY WARNING")
            
            # mostra alertas
            for i, alert in enumerate(alerts[:2]):  # máximo 2 alertas
                alert_y = sh - 2 + i
                if alert_y < sh:
                    stdscr.addstr(alert_y, 0, f"⚠️  {alert}"[:sw], 
                                 curses.color_pair(7) | curses.A_BOLD | curses.A_BLINK)
            
        except curses.error:
            pass

        # barra de conforto térmico
        try:
            temp = weather_data['temperature']
            if temp < 10:
                comfort = "COLD"
                comfort_color = curses.color_pair(5)
            elif temp < 20:
                comfort = "COOL"
                comfort_color = curses.color_pair(3)
            elif temp < 25:
                comfort = "COMFORTABLE"
                comfort_color = curses.color_pair(6)
            elif temp < 30:
                comfort = "WARM"
                comfort_color = curses.color_pair(1)
            else:
                comfort = "HOT"
                comfort_color = curses.color_pair(7)
            
            comfort_text = f"COMFORT LEVEL: {comfort}"
            if not alerts:  # só mostra se não há alertas
                stdscr.addstr(sh-1, 0, comfort_text[:sw], comfort_color | curses.A_BOLD)
            
        except curses.error:
            pass

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass