# Sistema Multiagente de Viajes con Google ADK

Proyecto académico que implementa un asistente inteligente de viajes mediante Google Agent Development Kit (ADK). El sistema utiliza un agente coordinador que delega solicitudes a agentes especializados.

## Integrantes

- César Joel Sirlopu Damian

## Características

El sistema cuenta con los siguientes agentes:

- **Travel Coordinator Agent:** coordina la solicitud y deriva las tareas.
- **Web Search Agent:** obtiene información actualizada mediante Google Search.
- **Itinerary Agent:** crea itinerarios organizados por días.
- **Budget Agent:** calcula presupuestos referenciales.
- **Risk Reviewer Agent:** identifica riesgos y recomendaciones.
- **Local Culture Agent:** recomienda platos, costumbres y frases útiles.

## Arquitectura

```text
travel_assistant/
├── agent.py
├── agents/
│   ├── coordinator.py
│   ├── web_search.py
│   ├── itinerary.py
│   ├── budget.py
│   ├── risk.py
│   └── culture.py
└── tools/
    ├── budget_tools.py
    ├── risk_tools.py
    └── culture_tools.py
```

El archivo `agent.py` expone al agente coordinador como `root_agent`. El coordinador analiza la solicitud y transfiere el control al agente especializado correspondiente.

## Requisitos

- Python 3.12
- Poetry
- Una API Key de Google AI Studio

## Instalación

Clonar el repositorio:

```powershell
git clone https://github.com/joeldamian703-ops/travel-adk-multiagent.git
cd travel-adk-multiagent
```

Crear o activar el entorno virtual e instalar las dependencias:

```powershell
poetry install
```

## Configuración de la API Key

Copiar el archivo de ejemplo:

```powershell
Copy-Item .env.example travel_assistant/.env
```

Editar `travel_assistant/.env` y colocar una API Key válida:

```env
GOOGLE_API_KEY="TU_API_KEY_DE_GOOGLE_AI_STUDIO"
```

El archivo `.env` está excluido mediante `.gitignore` para evitar publicar credenciales privadas.

## Ejecución en consola

```powershell
poetry run adk run travel_assistant
```

Para cerrar la aplicación, escribir:

```text
exit
```

## Ejecución en la interfaz web

```powershell
poetry run adk web --port 8000
```

Después, abrir en el navegador:

```text
http://localhost:8000
```

## Pruebas unitarias

Ejecutar las pruebas con cobertura:

```powershell
poetry run pytest --cov=travel_assistant --cov-report=term-missing --cov-report=xml
```

El proyecto contiene pruebas para:

- Estructura del sistema multiagente.
- Nombres y cantidad de agentes.
- Cálculo del presupuesto.
- Validación de datos incorrectos.
- Evaluación básica de riesgos.
- Recomendaciones culturales.

## Calidad del código

Ejecutar Ruff:

```powershell
poetry run ruff check .
```

Para corregir automáticamente errores compatibles:

```powershell
poetry run ruff check . --fix
```

## Flujo de ramas

El proyecto utiliza las siguientes ramas:

- `main`: versión estable.
- `develop`: integración de funcionalidades.
- `feature/travel-multiagent`: desarrollo del sistema multiagente.

Flujo utilizado:

```text
feature/travel-multiagent → develop → main
```

## Integración continua

GitHub Actions ejecuta automáticamente:

1. Instalación de dependencias con Poetry.
2. Análisis de calidad con Ruff.
3. Pruebas unitarias con Pytest.
4. Generación del reporte de cobertura.
5. Análisis estático con SonarQube Cloud.

## Seguridad

- La API Key no se almacena en el repositorio.
- El archivo `.env` está incluido en `.gitignore`.
- `.env.example` contiene únicamente un valor de referencia.
- Los presupuestos y recomendaciones generados son referenciales.

## Resultado

El sistema fue validado con solicitudes de viajes a Cusco y Buenos Aires. Los agentes generaron itinerarios, presupuestos, evaluaciones de riesgos y recomendaciones culturales mediante transferencias y herramientas personalizadas.