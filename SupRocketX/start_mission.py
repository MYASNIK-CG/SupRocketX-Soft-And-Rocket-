from SupRocketX import (
    SafetySystem, 
    MarsNavigator, 
    ShieldGenerator, 
    TelemetrySystem, 
    EngineControl
)
import time

def run_mission():
    # 1. Инициализация всех систем под управлением MYASNIK-CG
    telemetry = TelemetrySystem(mission_id="FAST-MARS-01")
    safety = SafetySystem()
    nav = MarsNavigator()
    shields = ShieldGenerator()
    engines = EngineControl()

    print("--- НАЧАЛО ПРЕДПОЛЕТНОЙ ПОДГОТОВКИ ---")
    
    # 2. Запуск двигателей и щитов
    engines.ignite()
    shields.activate_shields()
    
    # 3. Установка экстремальной скорости (Полет за 1 неделю)
    # Используем override_safety=True, как мы и программировали
    target_speed = 1350000 
    if nav.set_velocity(target_speed, override_safety=True):
        engines.set_thrust(100.0)
        
    # 4. Проверка безопасности и телеметрия
    if safety.check_telemetry(pitch=2.0, roll=1.5, yaw=0.0):
        print("🚀 СТАРТ ПРОИЗВЕДЕН УСПЕШНО!")
        
    # Имитация полета и отчет
    telemetry.send_report(
        velocity=nav.current_velocity, 
        hull_status=shields.hull_integrity, 
        shield_status=shields.shield_level
    )
    
    print(f"\n[INFO]: Миссия управляется софтом от MYASNIK-CG.")
    print("До Марса осталось: 7 дней.")

if __name__ == "__main__":
    run_mission()
