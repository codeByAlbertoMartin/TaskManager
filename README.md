# TaskManager

TaskManager es una aplicación en Python para la gestión de tareas, diseñada para facilitar la organización, seguimiento y automatización de tareas mediante integración con servicios de IA.

## Características

- Añadir, listar, actualizar y eliminar tareas.
- Persistencia de tareas en formato JSON.
- Integración con servicios de IA para sugerencias o automatización (ver `ai_service.py`).
- Interfaz de línea de comandos sencilla.

## Requisitos

- Python 3.10 o superior
- Paquetes listados en `requirements.txt`

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL-del-repositorio>
   cd TaskManager
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta la aplicación principal:

```bash
python main.py
```

Sigue las instrucciones en pantalla para gestionar tus tareas.

## Estructura del proyecto

- `main.py`: Punto de entrada de la aplicación.
- `task_manager.py`: Lógica principal para la gestión de tareas.
- `ai_service.py`: Integración con servicios de IA.
- `tasks.json`: Archivo donde se almacenan las tareas.
- `test_task_manager.py`: Pruebas unitarias.
- `requirements.txt`: Dependencias del proyecto.

## Ejemplo de uso

1. Añadir una tarea:

   ```
   > Añadir tarea: "Preparar presentación IA"
   ```

2. Listar tareas:

   ```
   > Listar tareas
   1. Preparar presentación IA [pendiente]
   ```

3. Eliminar una tarea:
   ```
   > Eliminar tarea 1
   ```

## Pruebas

Para ejecutar los tests:

```bash
python -m unittest test_task_manager.py
```

## Licencia

MIT License.
