import email
import base64
import re
import logging
from typing import List, Dict
from settings import settings

# Configurando o logger
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

class EmailParser:
    def __init__(self, raw_email: str):
        self.raw_email = raw_email
        self.parsed_email = email.message_from_string(raw_email)
    
    def get_subject(self) -> str:
        """Retorna o assunto do e-mail."""
        return self.parsed_email['Subject']
    
    def get_from(self) -> str:
        """Retorna o remetente do e-mail."""
        return self.parsed_email['From']
    
    def get_to(self) -> List[str]:
        """Retorna a lista de destinatários do e-mail."""
        to = self.parsed_email.get_all('To', [])
        return [address.strip() for address in to]

    def get_body(self) -> str:
        """Retorna o corpo do e-mail, considerando partes de texto simples e HTML."""
        body = ""
        if self.parsed_email.is_multipart():
            for part in self.parsed_email.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = part.get_payload(decode=True).decode(part.get_content_charset())
                    break
                elif content_type == 'text/html':
                    html_content = part.get_payload(decode=True).decode(part.get_content_charset())
                    body = self.extract_text_from_html(html_content)
        else:
            body = self.parsed_email.get_payload(decode=True).decode(self.parsed_email.get_content_charset())
        return body
    
    def extract_text_from_html(self, html: str) -> str:
        """Extrai texto puro de conteúdo HTML."""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', html)
    
    def get_attachments(self) -> List[Dict[str, str]]:
        """Retorna uma lista de anexos do e-mail."""
        attachments = []
        if self.parsed_email.is_multipart():
            for part in self.parsed_email.walk():
                content_disposition = str(part.get("Content-Disposition"))
                if 'attachment' in content_disposition:
                    filename = part.get_filename()
                    if filename:
                        payload = part.get_payload(decode=True)
                        file_data = base64.b64encode(payload).decode()  # Encode para base64
                        attachments.append({
                            'filename': filename,
                            'data': file_data,
                            'content_type': part.get_content_type()
                        })
        return attachments

    def parse_email(self) -> Dict[str, any]:
        """Retorna um dicionário com as informações extraídas do e-mail."""
        parsed_data = {
            'from': self.get_from(),
            'to': self.get_to(),
            'subject': self.get_subject(),
            'body': self.get_body(),
            'attachments': self.get_attachments()
        }
        logger.info("E-mail analisado com sucesso: %s", parsed_data)
        return parsed_data

# Exemplo de uso
if __name__ == "__main__":
    raw_email_string = """(Aqui você pode adicionar um exemplo de e-mail em formato de string)"""
    parser = EmailParser(raw_email_string)
    parsed_data = parser.parse_email()
    print(parsed_data)
