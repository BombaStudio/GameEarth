import smtplib
from email.mime.text import MIMEText

class sendEmail():
    def __init__(self, smtp_address, smtp_port, user_mail, user_pass, recipient_mails, topic, content):
        #SMTP Informations
        self.smtp_address = smtp_address
        self.smtp_port = smtp_port
        self.user_mail = user_mail
        self.user_pass = user_pass
        
        #Mail Informations
        self.recipient_mails = recipient_mails
        self.topic = topic
        self.content = content

    def send(self):
        try:
            #Maili content and set to be sent with utf-8 characters encoding
            mail = MIMEText(self.content, "html", "utf-8")
            
            #Mail sender's mail address 
            mail["From"] = self.user_mail

            mail["Subject"] = self.topic
            mail["To"] = ", ".join(self.recipient_mails)
            
            #Compiling mail informations
            mail = mail.as_string()

            s = smtplib.SMTP(self.smtp_address, self.smtp_port)

            #TLS connection (encrypted connection)
            s.starttls()

            #LOgin to SMTP server
            s.login(self.user_mail, self.user_pass)

            #Send mail
            s.sendmail(self.user_mail, self.recipient_mails, mail)

            return "Mail sent"
            
        except Exception as e:
            return "Error: " + str(e)