import unittest
from flask import Flask
from flask_testing import TestCase
from flask_dashboard import create_app  # Certifique-se de que a função create_app esteja definida em flask_dashboard.py

class TestDashboard(TestCase):

    def create_app(self):
        """Cria uma instância do aplicativo Flask para os testes."""
        app = create_app()
        app.config['TESTING'] = True  # Ativa o modo de teste
        return app

    def test_home_page(self):
        """Teste para a página inicial do dashboard."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Verifica se o status é 200 (OK)
        self.assertIn(b'Welcome to the NetWatch XDR Dashboard', response.data)  # Verifica se a mensagem de boas-vindas está na página

    def test_login_page(self):
        """Teste para a página de login."""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_dashboard_access(self):
        """Teste para verificar o acesso ao dashboard após login (pode ser necessário ajustar para seu fluxo de login)."""
        # Simule o login, se necessário
        self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard Overview', response.data)  # Verifique um elemento que deveria estar no dashboard

    def test_logout(self):
        """Teste para verificar a funcionalidade de logout."""
        self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)  # Verifica se há redirecionamento após logout

if __name__ == '__main__':
    unittest.main()
