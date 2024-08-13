import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail():
    def __init__(self, from_email: str, from_password: str) -> None:
        self.from_mail = from_email
        self.from_email = from_email
        self.from_password = from_password
                
    def send_email(self, body: str, subject: str, to_email: str, smtp_server: str ='smtp.office365.com', smtp_port: int =587):
        # Configura o e-mail
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Adiciona o corpo do e-mail
        msg.attach(MIMEText(body, 'plain'))

        # Conecta ao servidor SMTP e envia o e-mail
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Inicia a criptografia TLS
            server.login(self.from_email, self.from_password)
            text = msg.as_string()
            server.sendmail(self.from_email, self.to_email, text)
            server.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")