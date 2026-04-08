import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [PROPULSION] - %(levelname)s - %(message)s')

class EngineControl:
    def __init__(self):
        self.engine_status = "OFFLINE"
        self.thrust_level = 0.0  # Уровень тяги в %
        self.fuel_reserve = 100.0 # Запас топлива/энергии
        self.core_temp = 25.0    # Температура ядра двигателя

    def ignite(self):
        """Запуск системы зажигания."""
        if self.fuel_reserve > 0:
            self.engine_status = "READY"
            logging.info("Система зажигания готова. Двигатели в режиме ожидания.")
        else:
            logging.error("Запуск невозможен: критический уровень топлива!")

    def set_thrust(self, level: float):
        """Установка уровня тяги (от 0 до 100)."""
        if self.engine_status == "OFFLINE":
            logging.warning("Сначала нужно провести зажигание (ignite)!")
            return

        self.thrust_level = max(0, min(100, level))
        self.engine_status = "ACTIVE"
        
        # Моделируем нагрев и расход при разгоне
        self.core_temp += self.thrust_level * 0.5
        self.fuel_reserve -= self.thrust_level * 0.01
        
        logging.info(f"Тяга установлена: {self.thrust_level}% | Температура ядра: {self.core_temp}°C")
        
        if self.core_temp > 800:
            logging.critical("⚠️ ПЕРЕГРЕВ ДВИГАТЕЛЯ! Снижайте тягу!")

    def emergency_shutdown(self):
        """Экстренная остановка всех систем тяги."""
        self.thrust_level = 0.0
        self.engine_status = "OFFLINE"
        logging.critical("!!! ЭКСТРЕННОЕ ВЫКЛЮЧЕНИЕ ДВИГАТЕЛЕЙ ВЫПОЛНЕНО !!!")

# Быстрый тест движка
if __name__ == "__main__":
    engine = EngineControl()
    engine.ignite()
    engine.set_thrust(85.0)
  
