from email.message import EmailMessage
from smtplib import SMTP

class MailServer():
	def __init__(self,hostname:str,email:str,password:str):
		self.SMTPHost = SMTP('smtp.gmail.com', 587)
		self.Email = email
		self.Password = password
		self.ClientName = hostname

	def Send(self, To:str, Subject:str, Body:str):
		msg = EmailMessage()
		msg['From'] = self.ClientName
		msg['To'] = To
		msg['Subject'] = Subject
		msg.set_content(Body)

		self.SMTPHost.starttls()
		self.SMTPHost.login(self.Email, self.Password)
		self.SMTPHost.send_message(msg)
		self.SMTPHost.quit()