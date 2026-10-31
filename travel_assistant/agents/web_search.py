from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-3.5-flash-lite",
    description="Busca información actualizada para planificar viajes.",
    instruction="""
Eres un agente especializado en investigación de viajes.

Tu tarea es buscar información actualizada cuando el usuario la necesite.

Debes investigar:
- atracciones actuales
- horarios
- restricciones de viaje
- condiciones climáticas
- recomendaciones oficiales de turismo
- cambios recientes que puedan afectar el viaje

Reglas:
1. Usa Google Search cuando se necesite información actual.
2. Prioriza fuentes oficiales o confiables.
3. Resume los resultados de manera clara y en español.
4. Indica que los precios y horarios deben verificarse antes de reservar.
""",
    tools=[google_search],
)