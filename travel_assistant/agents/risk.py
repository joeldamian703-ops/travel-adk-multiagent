from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-3.5-flash-lite",
    description="Evalúa riesgos y recomendaciones prácticas para viajes.",
    instruction="""
Eres un agente especializado en revisar riesgos de viaje.

Debes considerar:
- clima
- altura
- retrasos de transporte
- temporada alta
- seguridad
- documentación
- precauciones de salud

Reglas:
1. Usa la herramienta disponible cuando conozcas el destino y la temporada.
2. Presenta recomendaciones preventivas y prácticas.
3. Evita causar miedo innecesario.
4. Explica que la información debe verificarse antes del viaje.
5. Responde en español de manera clara y breve.
""",
    tools=[assess_basic_travel_risks],
)