from travel_assistant.tools.culture_tools import (
    get_local_culture_recommendations,
)


def test_culture_recommendations_for_cusco() -> None:
    result = get_local_culture_recommendations("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert "Chiri uchu" in result["typical_foods"]
    assert len(result["customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1


def test_culture_recommendations_default_destination() -> None:
    result = get_local_culture_recommendations("Roma")

    assert result["status"] == "success"
    assert len(result["typical_foods"]) == 1
    assert len(result["customs"]) == 1
    assert len(result["useful_phrases"]) == 3


def test_culture_recommendations_empty_destination() -> None:
    result = get_local_culture_recommendations("")

    assert result["status"] == "error"
    assert "destination" in result["message"].lower()