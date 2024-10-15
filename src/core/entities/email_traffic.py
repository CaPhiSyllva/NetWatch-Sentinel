from datetime import datetime

class EmailTraffic:
    def __init__(self, sender_email, recipient_email, total_emails=0, total_size=0, first_seen=None, last_seen=None):
        """
        Entidade que representa o tráfego de e-mails entre dois endereços de e-mail.

        :param sender_email: Endereço de e-mail do remetente.
        :param recipient_email: Endereço de e-mail do destinatário.
        :param total_emails: Total de e-mails transmitidos entre os dois endereços.
        :param total_size: Total de bytes transmitidos entre os dois endereços.
        :param first_seen: Data e hora do primeiro e-mail detectado.
        :param last_seen: Data e hora do último e-mail detectado.
        """
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.total_emails = total_emails
        self.total_size = total_size
        self.first_seen = first_seen if first_seen else datetime.now()
        self.last_seen = last_seen if last_seen else datetime.now()

    def update_traffic(self, email_size):
        """
        Atualiza o tráfego de e-mails com base em um novo e-mail.

        :param email_size: Tamanho do e-mail em bytes.
        """
        self.total_emails += 1
        self.total_size += email_size
        self.last_seen = datetime.now()

    def __repr__(self):
        return (f"<EmailTraffic sender={self.sender_email} recipient={self.recipient_email} "
                f"total_emails={self.total_emails} total_size={self.total_size} "
                f"first_seen={self.first_seen} last_seen={self.last_seen}>")

    def to_dict(self):
        """
        Converte a entidade para um dicionário para fácil armazenamento e serialização.

        :return: Dicionário com os dados do tráfego de e-mails.
        """
        return {
            "sender_email": self.sender_email,
            "recipient_email": self.recipient_email,
            "total_emails": self.total_emails,
            "total_size": self.total_size,
            "first_seen": self.first_seen.isoformat(),
            "last_seen": self.last_seen.isoformat(),
        }

    @staticmethod
    def from_email(sender_email, recipient_email, email_size):
        """
        Cria uma instância de EmailTraffic a partir dos detalhes de um e-mail.

        :param sender_email: Endereço de e-mail do remetente.
        :param recipient_email: Endereço de e-mail do destinatário.
        :param email_size: Tamanho do e-mail em bytes.
        :return: Instância de EmailTraffic.
        """
        return EmailTraffic(
            sender_email=sender_email,
            recipient_email=recipient_email,
            total_emails=1,
            total_size=email_size
        )
