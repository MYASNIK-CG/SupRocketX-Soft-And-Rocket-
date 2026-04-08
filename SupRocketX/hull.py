import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [HULL-SYSTEM] - %(levelname)s - %(message)s')

class ShieldGenerator:
    def __init__(self):
        self.shield_level = 100.0  # Процент заряда щитов
        self.hull_integrity = 100.0 # Целостность корпуса
        self.magnetic_field = False

    def activate_shields(self):
        """Активация магнитного щита для защиты от радиации и пыли."""
        self.magnetic_field = True
        logging.info("МАГНИТНОЕ ПОЛЕ АКТИВИРОВАНО. Защита от микрочастиц включена.")

    def check_impact_risk(self, velocity: float):
        """
        Расчет риска повреждения в зависимости от скорости.
        Чем выше скорость, тем мощнее должен быть щит.
        """
        if velocity > 1000000:
            logging.warning("⚠️ ЭКСТРЕМАЛЬНАЯ СКОРОСТЬ: Щиты переведены в режим 'OVERDRIVE'.")
            if not self.magnetic_field:
                damage = random.uniform(5, 15)
                self.hull_integrity -= damage
                logging.critical(f"ВНИМАНИЕ! Корпус поврежден на {round(damage, 1)}% из-за отсутствия щитов!")
            else:
                self.shield_level -= 0.5 # Щиты медленно тратят энергию на такой скорости
                logging.info(f"Щиты стабильны. Заряд: {self.shield_level}%")
        
        if self.hull_integrity < 50:
            logging.error("КРИТИЧЕСКОЕ СОСТОЯНИЕ КОРПУСА! Рекомендуется немедленное торможение.")
            return False
        return True

    def repair_hull(self):
        """Запуск нано-роботов для ремонта корпуса."""
        if self.hull_integrity < 100:
            logging.info("Запуск системы регенерации корпуса...")
            self.hull_integrity = 100.0
            logging.info("Корпус полностью восстановлен.")
