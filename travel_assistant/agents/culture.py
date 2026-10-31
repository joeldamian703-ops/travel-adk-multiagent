from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import (
    get_local_culture_recommendations,
)

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-3.5-flash-lite",
    description="Brinda recomendaciones sobre la cultura local del destino.",
    instruction="""
Eres un agente especializado en cultura local para viajeros.

Tu tarea es proporcionar:
- platos típicos del destino
- costumbres locales importantes
- frases útiles para comunicarse
- recomendaciones de comportamiento respetuoso

Reglas:
1. Usa la herramienta disponible cuando conozcas el destino.
2. Explica las recomendaciones en español.
3. Respeta las tradiciones y evita estereotipos.
4. Presenta información breve, práctica y útil para el viajero.
""",
    tools=[get_local_culture_recommendations],
)