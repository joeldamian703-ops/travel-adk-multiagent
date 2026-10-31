from google.adk.agents import Agent

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.culture import local_culture_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent

travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model="gemini-3.5-flash-lite",
    description="Coordina un equipo de agentes especializados en viajes.",
    instruction="""
Eres el coordinador de un sistema multiagente para planificar viajes.

Recibe la solicitud del usuario y delega las tareas a los agentes especializados:

- Usa web_search_agent para buscar información actualizada.
- Usa itinerary_agent para crear un itinerario organizado por días.
- Usa budget_agent para calcular un presupuesto referencial.
- Usa risk_reviewer_agent para revisar riesgos y recomendaciones.
- Usa local_culture_agent para explicar gastronomía, costumbres y frases útiles.

La respuesta final debe incluir:
1. Resumen de la solicitud.
2. Información actualizada relevante.
3. Itinerario sugerido.
4. Presupuesto referencial.
5. Riesgos y recomendaciones.
6. Cultura local.
7. Consejo final.

Reglas:
1. Responde siempre en español.
2. Presenta la información con títulos y listas claras.
3. No inventes precios exactos, horarios ni disponibilidad.
4. Recomienda verificar fuentes oficiales antes de reservar.
5. Mantén la respuesta útil y comprensible.
6. Usa web_search_agent únicamente cuando el usuario solicite expresamente
   información actualizada o una búsqueda en Internet.
""",
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
        local_culture_agent,
    ],
)