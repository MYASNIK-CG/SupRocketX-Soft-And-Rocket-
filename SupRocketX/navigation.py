import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [NAV-COMPUTER] - %(levelname)s - %(message)s')

class MarsNavigator:
    def __init__(self):
        self.distance_to_mars = 225000000  # км
        self.current_velocity = 40000.0   # км/ч (стандартная крейсерская скорость)
        self.MAX_SAFE_VELOCITY = 150000.0 # Порог безопасности

    def set_velocity(self, target_velocity: float, override_safety: bool = False):
        """
        Настройка скорости с системой подтверждения.
        """
        if target_velocity <= 0:
            logging.error("ОШИБКА: Скорость не может быть отрицательной или нулевой.")
            return False

        # Проверка на экстремальную скорость (полет за неделю)
        if target_velocity >= 1300000:
            if not override_safety:
                logging.critical("⚠️ ВНИМАНИЕ: Запрошена скорость 'INTERSTELLAR-WEEK'.")
                logging.critical("Риск разрушения корпуса 99%. Требуется ручное подтверждение (override_safety=True).")
                return False
            else:
                logging.warning("!!! РЕЖИМ ГИПЕР-ПРЫЖКА АКТИВИРОВАН. УДАЧИ, ПИЛОТ !!!")

        self.current_velocity = target_velocity
        logging.info(f"Скорость установлена на {target_velocity:,} км/ч.")
        return True

    def get_mission_stats(self):
        """
        Рассчитывает время в пути исходя из установленной скорости.
        """
        hours = self.distance_to_mars / self.current_velocity
        days = hours / 24
        
        print(f"\n--- СТАТУС МИССИИ 'MARS-DIRECT' ---")
        print(f"Текущая скорость: {self.current_velocity:,} км/ч")
        print(f"Расчетное время прибытия (ETA): {round(days, 2)} дней")
        
        if days <= 7:
            print("Статус: ЭКСТРЕМАЛЬНО БЫСТРО (Режим 1 неделя)")
        elif days <= 60:
            print("Статус: ВЫСОКАЯ СКОРОСТЬ (Режим 2 месяца)")
        else:
            print("Статус: СТАНДАРТНЫЙ ПЕРЕЛЕТ")
        print("----------------------------------\n")

# Тест кастомной настройки
if __name__ == "__main__":
    nav = MarsNavigator()
    
    # 1. Пытаемся поставить скорость для полета за неделю без подтверждения
    print("Попытка 1: Установка скорости 1,350,000 км/ч...")
    nav.set_velocity(1350000) 
    
    # 2. Ставим скорость с подтверждением
    print("\nПопытка 2: Установка скорости с подтверждением (override_safety)...")
    if nav.set_velocity(1350000, override_safety=True):
        nav.get_mission_stats()
