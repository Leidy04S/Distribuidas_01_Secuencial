# Ejercicio 1: Ejecución Secuencial (Procesamiento de una Compra)

## ¿De qué trata este ejercicio?
Este programa muestra cómo funciona la **ejecución secuencial** en un caso práctico: el procesamiento de una compra en línea.

En la ejecución secuencial, las tareas se realizan en un orden único y obligatorio: **un paso debe terminar por completo para que el siguiente pueda iniciar**. No se puede cobrar sin validar la compra, ni enviar un paquete sin antes haberlo pagado y preparado.

El programa realiza los siguientes pasos en orden:
1. Validar los productos del carrito.
2. Procesar el pago con tarjeta.
3. Empaquetar el pedido en bodega.
4. Generar la guía y notificar el envío.

---

## Estructura de archivos

```text
Distribuidas_01_Secuencial/
├── 01_secuencial.py     # Script en Python con la simulación del proceso
├── docker-compose.yml   # Archivo de configuración para ejecutar en Docker
└── README.md            # Guía e instrucciones del proyecto
```

---

## Requisitos previos

Necesitas tener instalados los siguientes programas en tu computadora:

- **Git:** [Descargar Git](https://git-scm.com/)
- **Docker Desktop:** [Descargar Docker Desktop](https://www.docker.com/products/docker-desktop/) *(debe estar abierto antes de ejecutar los comandos)*

---

## Comprobar que Docker está listo (Opcional)

Si quieres verificar que Docker esté funcionando correctamente, abre la terminal y ejecuta:

```bash
docker --version
docker compose version
```

---

## Cómo ejecutar el programa paso a paso

### 1. Clonar el repositorio
Abre la terminal y descarga el proyecto desde GitHub:

```bash
git clone [https://github.com/Leidy04S/Distribuidas_01_Secuencial.git](https://github.com/Leidy04S/Distribuidas_01_Secuencial.git)
```

### 2. Entrar a la carpeta del proyecto
```bash
cd Distribuidas_01_Secuencial
```

### 3. Iniciar el programa con Docker Compose
Ejecuta este comando para arrancar el contenedor y ver el script en acción:

```bash
docker compose up
```

---

## Lo que verás en pantalla

En la consola aparecerá la simulación avanzando paso a paso en tiempo real:

```text
Iniciando: Paso 1 - Validar inventario del carrito...
Completado: Paso 1.

Iniciando: Paso 2 - Procesar pago con tarjeta...
Completado: Paso 2.

Iniciando: Paso 3 - Empaquetar producto en bodega...
Completado: Paso 3.

Iniciando: Paso 4 - Notificar envío al cliente...
Completado: Paso 4.

============================================
Proceso finalizado. Tiempo total: 8.00 segundos.
============================================
```

---

## Cómo detener y cerrar el programa

Una vez que termine la revisión, apaga y elimina el contenedor ejecutando:

```bash
docker compose down
```