import time

def procesar_paso(paso, descripcion, duracion):
    print(f"Iniciando: {paso} - {descripcion}...")
    time.sleep(duracion)  # Simula el tiempo que tarda la operación
    print(f"Completado: {paso}.\n")

inicio = time.perf_counter()

# Ejecución lineal paso a paso
procesar_paso("Paso 1", "Validar inventario del carrito", 2)
procesar_paso("Paso 2", "Procesar pago con tarjeta", 3)
procesar_paso("Paso 3", "Empaquetar producto en bodega", 2)
procesar_paso("Paso 4", "Notificar envío al cliente", 1)

fin = time.perf_counter()

print("=" * 45)
print(f"Proceso finalizado. Tiempo total: {fin - inicio:.2f} segundos.")
print("=" * 45)