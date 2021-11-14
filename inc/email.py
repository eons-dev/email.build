import os
import logging
import smtplib, ssl
import jsonpickle
import ebbs

class email(ebbs.Builder):
    def __init__(self, name="Send an email"):
        super().__init__(name)
    
        self.supportedProjectTypes = []

        self.requiredKWArgs.append("--email-config")
        self.requiredKWArgs.append("--message")

    def PreBuild(self, **kwargs):
        self.email = jsonpickle.decode(open(kwargs.get('--email-config'), 'r').read()) | jsonpickle.decode(open(kwargs.get('--message'), 'r').read())

    #Required Builder method. See that class for details.
    def Build(self):
        email_text = f'''From: {self.email['mail_from']}
To: {self.email['mail_to']}
Subject: {self.email['subject']}

{self.email['message']}
'''
        logging.debug(f'Trying to send: \n{email_text}')
        context = ssl.create_default_context()
        server = smtplib.SMTP(self.email['smtp_server'], self.email['smtp_port'])
        server.ehlo()
        server.starttls(context=context)
        server.login(self.email['username'], self.email['password'])
        server.sendmail(self.email['mail_from'], self.email['mail_to'], email_text)
        server.close()
        logging.info('Email sent!')