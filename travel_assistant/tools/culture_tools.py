def get_local_culture_recommendations(destination: str) -> dict:
    """Return cultural recommendations for a travel destination."""
    destination_normalized = destination.lower().strip()

    if not destination_normalized:
        return {
            "status": "error",
            "message": "The destination must not be empty.",
        }

    recommendations = {
        "cusco": {
            "typical_foods": [
                "Chiri uchu",
                "Sopa de quinua",
                "Cuy al horno",
            ],
            "customs": [
                "Respect archaeological sites and protected areas.",
                "Ask permission before photographing local people.",
            ],
            "useful_phrases": [
                "Buenos días",
                "Gracias",
                "Allin p'unchay",
            ],
        },
        "arequipa": {
            "typical_foods": [
                "Rocoto relleno",
                "Adobo arequipeño",
                "Chupe de camarones",
            ],
            "customs": [
                "Visit traditional picanterías respectfully.",
                "Protect historical buildings and natural areas.",
            ],
            "useful_phrases": [
                "Buenos días",
                "Por favor",
                "Muchas gracias",
            ],
        },
        "buenos aires": {
            "typical_foods": [
                "Empanadas",
                "Asado",
                "Dulce de leche",
            ],
            "customs": [
                "Dinner is commonly eaten later in the evening.",
                "Greet people politely when entering small businesses.",
            ],
            "useful_phrases": [
                "Buen día",
                "Por favor",
                "Gracias",
            ],
        },
        "parís": {
            "typical_foods": [
                "Croissant",
                "Crêpes",
                "Soupe à l'oignon",
            ],
            "customs": [
                "Greet staff before asking for assistance.",
                "Keep a respectful tone in museums and public places.",
            ],
            "useful_phrases": [
                "Bonjour",
                "S'il vous plaît",
                "Merci",
            ],
        },
    }

    selected = recommendations.get(
        destination_normalized,
        {
            "typical_foods": ["Research traditional local dishes."],
            "customs": ["Respect local rules, traditions and public spaces."],
            "useful_phrases": ["Hello", "Please", "Thank you"],
        },
    )

    return {
        "status": "success",
        "destination": destination,
        **selected,
    }