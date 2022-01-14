import os
import logging
import smtplib, ssl
import jsonpickle
import ebbs

class email(ebbs.Builder):
    def __init__(this, name="Send an email"):
        super().__init__(name)
    
        this.supportedProjectTypes = []

        this.requiredKWArgs.append("--email-config")
        this.requiredKWArgs.append("--message")

    def PreBuild(this, **kwargs):
        this.email = jsonpickle.decode(open(kwargs.get('--email-config'), 'r').read()) | jsonpickle.decode(open(kwargs.get('--message'), 'r').read())

    #Required Builder method. See that class for details.
    def Build(this):
        email_text = f'''From: {this.email['mail_from']}
To: {this.email['mail_to']}
Subject: {this.email['subject']}

{this.email['message']}
'''
        logging.debug(f'Trying to send: \n{email_text}')
        context = ssl.create_default_context()
        server = smtplib.SMTP(this.email['smtp_server'], this.email['smtp_port'])
        server.ehlo()
        server.starttls(context=context)
        server.login(this.email['username'], this.email['password'])
        server.sendmail(this.email['mail_from'], this.email['mail_to'], email_text)
        server.close()
        logging.info('Email sent!')