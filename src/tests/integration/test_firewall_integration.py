import unittest
from firewall_manager import FirewallManager  # Certifique-se de que o caminho para FirewallManager esteja correto

class TestFirewallIntegration(unittest.TestCase):

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.firewall_manager = FirewallManager()

    def test_enable_firewall(self):
        """Teste para verificar se o firewall é ativado corretamente."""
        result = self.firewall_manager.enable_firewall()
        self.assertTrue(result)  # Verifica se o resultado é True

    def test_disable_firewall(self):
        """Teste para verificar se o firewall é desativado corretamente."""
        self.firewall_manager.enable_firewall()  # Ativa o firewall primeiro
        result = self.firewall_manager.disable_firewall()
        self.assertTrue(result)  # Verifica se o resultado é True

    def test_add_firewall_rule(self):
        """Teste para adicionar uma regra ao firewall."""
        rule = "ACCEPT tcp -- any any 80"
        result = self.firewall_manager.add_rule(rule)
        self.assertTrue(result)  # Verifica se a regra foi adicionada com sucesso

    def test_remove_firewall_rule(self):
        """Teste para remover uma regra do firewall."""
        rule = "ACCEPT tcp -- any any 80"
        self.firewall_manager.add_rule(rule)  # Adiciona a regra primeiro
        result = self.firewall_manager.remove_rule(rule)
        self.assertTrue(result)  # Verifica se a regra foi removida com sucesso

    def test_list_firewall_rules(self):
        """Teste para listar regras do firewall."""
        rule = "ACCEPT tcp -- any any 80"
        self.firewall_manager.add_rule(rule)  # Adiciona a regra primeiro
        rules = self.firewall_manager.list_rules()
        self.assertIn(rule, rules)  # Verifica se a regra está na lista

if __name__ == '__main__':
    unittest.main()
