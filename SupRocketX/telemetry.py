import logging
import datetime

# Настройка логирования для телеметрии
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [DATA-LINK] - %(message)s')

class TelemetrySystem:
    def __init__(self, mission_id="MARS-WEEK-1"):
        self.mission_id = mission_id
        self.operator = "MYASNIK-CG"
        self.start_time = datetime.datetime.now()

    def send_report(self, velocity: float, hull_status: float, shield_status: float):
        """
        Формирует и отправляет полный отчет о состоянии миссии.
        """
        report = (
            f"\n"
            f"--- [ TRANSMISSION START | OP: {self.operator} ] ---\n"
            f"ID Миссии: {self.mission_id}\n"
            f"Текущая скорость: {velocity:,} км/ч\n"
            f"Целостность корпуса: {hull_status}%\n"
            f"Заряд щитов: {shield_status}%\n"
            f"--- [ TRANSMISSION END ] ---\n"
        )
        print(report)
        logging.info("Пакет данных успешно отправлен в штаб управления.")

    def log_event(self, message: str):
        """Запись важного события в бортовой журнал"""
        with open("mission_log.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")
        logging.info(f"Событие зафиксировано: {message}")

# Тест системы
if __name__ == "__main__":
    tel = TelemetrySystem()
    tel.send_report(1350000, 100.0, 98.5)
  
