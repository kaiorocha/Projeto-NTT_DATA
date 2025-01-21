import pytest
from my_flask_app.app.main import app

@pytest.fixture
def client():
    # Configuração do cliente de teste do Flask
    app.testing = True  # Modo de teste ativado
    client = app.test_client()
    return client

def test_home_page(client):
    """Testa se a rota '/' retorna a mensagem correta"""
    response = client.get('/')
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida
    assert b'Hello, NTT DATA' in response.data  # Verifica se o conteúdo esperado está presente