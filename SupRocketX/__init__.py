"""
SupRocketX — Mission Critical Aerospace Framework
Lead Developer: MYASNIK-CG
"""

def print_banner():
    banner = f"""
    ==================================================
    🚀 SupRocketX Framework v1.0.0
    🛠  LEAD DEVELOPER: MYASNIK-CG
    ⚠️  STATUS: ALL SYSTEMS MISSION READY
    ==================================================
    """
    print(banner)

# Вывод ника автора при импорте
print_banner()

# Регистрируем все модули в системе
from .safety import SafetySystem
from .navigation import MarsNavigator
from .hull import ShieldGenerator
from .telemetry import TelemetrySystem
from .propulsion import EngineControl
from .landing import LandingSystem

__all__ = [
    "SafetySystem",
    "MarsNavigator",
    "ShieldGenerator",
    "TelemetrySystem",
    "EngineControl",
    "LandingSystem"
]
