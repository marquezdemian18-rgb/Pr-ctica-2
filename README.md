import random
import time

# -------------------------------
# Clase base DispositivoIoT
# -------------------------------
class DispositivoIoT:
    """
    Clase base para todos los dispositivos IoT.
    """
    def __init__(self, id_dispositivo):
        self.__id_dispositivo = id_dispositivo
        self.__estado = "Apagado"
    
    def encender(self):
        self.__estado = "Encendido"
    
    def apagar(self):
        self.__estado = "Apagado"
    
    def get_estado(self):
        return self.__estado
    
    def get_id(self):
        return self.__id_dispositivo
    
    def mostrar_datos(self):
        print(f"ID: {self.__id_dispositivo} | Estado: {self.__estado}")

# -------------------------------
# Subclase SensorHumedad
# -------------------------------
class SensorHumedad(DispositivoIoT):
    """Sensor de humedad del suelo"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__humedad = 0.0
    
    def leer_humedad(self):
        self.__humedad = round(random.uniform(20.0, 80.0), 1)
    
    def get_humedad(self):
        return self.__humedad
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Humedad actual: {self.__humedad}%")

# -------------------------------
# Subclase ActuadorValvula
# -------------------------------
class ActuadorValvula(DispositivoIoT):
    """Actuador de válvula de riego"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__abierta = False
    
    def abrir_valvula(self):
        self.__abierta = True
    
    def cerrar_valvula(self):
        self.__abierta = False
    
    def get_estado_valvula(self):
        return "Abierta" if self.__abierta else "Cerrada"
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Válvula: {self.get_estado_valvula()}")

# -------------------------------
# Subclase ActuadorLuz
# -------------------------------
class ActuadorLuz(DispositivoIoT):
    """Actuador de luz para cultivo"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__intensidad = 0
    
    def ajustar_intensidad(self, valor):
        if 0 <= valor <= 100:
            self.__intensidad = valor
    
    def get_intensidad(self):
        return self.__intensidad
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Intensidad de luz: {self.__intensidad}%")

# -------------------------------
# Simulación de sistema de riego
# -------------------------------
if __name__ == "__main__":
    # Crear dispositivos
    dispositivos = [
        SensorHumedad("Hum1"),
        SensorHumedad("Hum2"),
        ActuadorValvula("Valvula1"),
        ActuadorLuz("Luz1"),
        ActuadorLuz("Luz2")
    ]
    
    # Encender todos los dispositivos
    for d in dispositivos:
        d.encender()
    
    # Ciclo de monitoreo
    for ciclo in range(5):
        print(f"\n--- Ciclo de riego {ciclo+1} ---")
        
        # Sensores leen humedad
        humedades = []
        for d in dispositivos:
            if isinstance(d, SensorHumedad):
                d.leer_humedad()
                humedades.append(d.get_humedad())
        
        promedio_humedad = sum(humedades)/len(humedades)
        
        # Controlar válvula: si humedad < 50%, abrir válvula, sino cerrar
        for d in dispositivos:
            if isinstance(d, ActuadorValvula):
                if promedio_humedad < 50:
                    d.abrir_valvula()
                else:
                    d.cerrar_valvula()
        
        # Ajustar intensidad de luz según humedad: más baja → más luz
        intensidad_luz = int(max(0, min(100, (60 - promedio_humedad)*2)))
        for d in dispositivos:
            if isinstance(d, ActuadorLuz):
                d.adjust_intensity = d.ajustar_intensidad(intensidad_luz)
        
        # Mostrar datos de todos (polimorfismo)
        for d in dispositivos:
            d.mostrar_datos()
        
        time.sleep(1)
