from travel_assistant.agent import root_agent


def test_root_agent_name() -> None:
    assert root_agent.name == "travel_coordinator_agent"


def test_root_agent_has_five_sub_agents() -> None:
    assert len(root_agent.sub_agents) == 5


def test_sub_agent_names() -> None:
    names = {agent.name for agent in root_agent.sub_agents}

    assert "web_search_agent" in names
    assert "itinerary_agent" in names
    assert "budget_agent" in names
    assert "risk_reviewer_agent" in names
    assert "local_culture_agent" in names


def test_sub_agent_names_are_unique() -> None:
    names = [agent.name for agent in root_agent.sub_agents]

    assert len(names) == len(set(names))