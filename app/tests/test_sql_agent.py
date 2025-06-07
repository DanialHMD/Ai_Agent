from unittest.mock import patch
from app.utils.sql_agent import Agent

@patch("openai.OpenAI.chat.completions.create")
def test_ask_ai(mock_create):
    mock_create.return_value.choices[0].message.content = "SELECT * FROM users;"
    agent = Agent()
    prompt = "List all users"
    response = agent.ask_ai(prompt, dialect="sqlite")
    assert "SELECT" in response
