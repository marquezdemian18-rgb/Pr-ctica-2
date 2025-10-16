import random
import time

# -------------------------------
# Clase base DispositivoIoT
# -------------------------------
class DispositivoIoT:
    """
    Clase base para todos los dispositivos IoT.
    Define los atributos y métodos comunes.
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
# Subclase SensorTemperatura
# -------------------------------
class SensorTemperatura(DispositivoIoT):
    """Sensor de temperatura en °C"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__temperatura = 0.0
    
    def leer_temperatura(self):
        """Simula lectura de temperatura"""
        self.__temperatura = round(random.uniform(20.0, 40.0), 1)
    
    def get_temperatura(self):
        return self.__temperatura
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Temperatura actual: {self.__temperatura}°C")

# -------------------------------
# Subclase SensorHumedad
# -------------------------------
class SensorHumedad(DispositivoIoT):
    """Sensor de humedad del suelo (%)"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__humedad = 0.0
    
    def leer_humedad(self):
        """Simula lectura de humedad"""
        self.__humedad = round(random.uniform(20.0, 80.0), 1)
    
    def get_humedad(self):
        return self.__humedad
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Humedad actual: {self.__humedad}%")

# -------------------------------
# Subclase ActuadorLuz
# -------------------------------
class ActuadorLuz(DispositivoIoT):
    """Actuador de luz con intensidad variable (0–100%)"""
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.__intensidad = 0
    
    def ajustar_intensidad(self, valor):
        """Ajusta la intensidad de luz"""
        if 0 <= valor <= 100:
            self.__intensidad = valor
    
    def get_intensidad(self):
        return self.__intensidad
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Intensidad de luz: {self.__intensidad}%")

# -------------------------------
# Simulación de sistema IoT
# -------------------------------
if __name__ == "__main__":
    # Crear dispositivos
    dispositivos = [
        SensorTemperatura("Temp1"),
        SensorTemperatura("Temp2"),
        SensorHumedad("Hum1"),
        ActuadorLuz("Luz1"),
        ActuadorLuz("Luz2")
    ]
    
    # Encender todos
    for d in dispositivos:
        d.encender()
    
    # Simular 5 ciclos
    for ciclo in range(5):
        print(f"\n--- Ciclo {ciclo+1} ---")
        temp_total, hum_total = 0, 0
        n_temp, n_hum = 0, 0
        
        # Leer sensores
        for d in dispositivos:
            if isinstance(d, SensorTemperatura):
                d.leer_temperatura()
                temp_total += d.get_temperatura()
                n_temp += 1
            elif isinstance(d, SensorHumedad):
                d.leer_humedad()
                hum_total += d.get_humedad()
                n_hum += 1
        
        temp_prom = temp_total / n_temp
        hum_prom = hum_total / n_hum
        
        # Control de luz según temperatura
        for d in dispositivos:
            if isinstance(d, ActuadorLuz):
                if temp_prom > 30:
                    d.ajustar_intensidad(80)
                else:
                    d.ajustar_intensidad(40)
        
        # Mostrar datos
        for d in dispositivos:
            d.mostrar_datos()
        
        print(f"\nPromedio temperatura: {temp_prom:.1f}°C | Promedio humedad: {hum_prom:.1f}%")
        time.sleep(1)
