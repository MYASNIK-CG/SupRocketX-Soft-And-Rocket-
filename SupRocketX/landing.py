import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LANDING-MODULE] - %(levelname)s - %(message)s')

class LandingSystem:
    def __init__(self):
        self.gear_deployed = False
        self.altitude = 10000.0  # Высота в метрах до поверхности
        self.descent_speed = 500.0 # Скорость снижения (м/с)

    def deploy_gear(self):
        """Выпуск посадочных опор."""
        logging.info("Инициализация выпуска шасси...")
        time.sleep(1)
        self.gear_deployed = True
        logging.info("✅ ПОСАДОЧНЫЕ ОПОРЫ ВЫПУЩЕНЫ И ЗАФИКСИРОВАНЫ.")

    def final_approach(self, current_velocity_kmh: float):
        """Алгоритм финального торможения."""
        logging.info(f"Начало торможения. Входная скорость: {current_velocity_kmh} км/ч")
        
        # На Марсе нужно тормозить двигателями, так как атмосфера тонкая
        if current_velocity_kmh > 1000:
            logging.warning("⚠️ СЛИШКОМ ВЫСОКАЯ СКОРОСТЬ ДЛЯ ПОСАДКИ! Активация реверсивной тяги...")
            time.sleep(1)
            
        logging.info("Мягкая посадка: Активация тормозных двигателей на высоте 50м...")
        print("🌍 [STATUS]: TOUCHDOWN CONFIRMED. WELCOME TO MARS!")
        print(f"Developed by MYASNIK-CG. Mission Success.")

# Тест модуля
if __name__ == "__main__":
    ls = LandingSystem()
    ls.deploy_gear()
    ls.final_approach(800)
