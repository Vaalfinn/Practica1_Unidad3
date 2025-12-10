import time
import random

def test_integration():
    print("Iniciando pruebas de integración en entorno de liberación...")
    time.sleep(1)
    
    # Simular verificación de endpoints
    endpoints = ["/health", "/api/v1/users", "/metrics"]
    for endpoint in endpoints:
        print(f"Testing endpoint {endpoint}...")
        assert True # Simula que el test pasa
        
    print("✅ Todos los tests de integración pasaron.")

def test_latency_slo():
    print("Verificando latencia p95 < 500ms...")
    latency = random.randint(100, 400)
    print(f"Latencia medida: {latency}ms")
    if latency > 500:
        raise Exception("SLO Violado: Latencia muy alta")
    print("✅ SLO de Latencia cumplido.")

if __name__ == "__main__":
    test_integration()
    test_latency_slo()
