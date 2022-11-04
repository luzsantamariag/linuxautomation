#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 8 17:14:01 2022
@author: Luz Santamaría Granados
This class is based on Rohit Shrestha's code to send a message to Gmail. 
In the new version, the script receives two parameters: a log file and an SQL file. 
These files are sent to destination emails when the backup is completed.
"""

import smtplib
import sys
import os

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

class Mail:
    """ This class receives two parameters: a log file and SQL file. 
    These files are sent to the destination emails when the backup is finished.
    """

    def __init__(self, log, sql):
        self._logfile = log
        self._sqlfile = sql

    def run(self):
        names = ['user1', 'user2']
        emails  = ['user1@gmail.com', 'user2@uptc.edu.co']

        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('user@gmail.com', 'xxxxxxxxxxxxxxx')

        # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()       # create a message

            # setup the parameters of the message
            msg['From'] = name
            msg['To'] = email
            msg['Subject'] = "Backup: " + self._sqlfile
            
            # add in the message body
            msg.attach(MIMEText("Hi, this is the today backup!", 'plain'))

            # Add the log file in the email attachment
            attach1 = MIMEApplication(open(self._logfile).read(), _subtype="txt")
            attach1.add_header('Content-Disposition', 'attachment', filename=str(
                os.path.basename(self._logfile)))
            msg.attach(attach1)
            
            # Add the sql file in the email attachment
            attach2 = MIMEApplication(open(self._sqlfile).read(), _subtype="txt")
            attach2.add_header('Content-Disposition', 'attachment', filename=str(
                os.path.basename(self._sqlfile)))
            msg.attach(attach2)
            
            # send the message via the server set up earlier.
            s.send_message(msg)
            del msg
            
        # Terminate the SMTP session and close the connection
        s.quit()
    
if __name__ == '__main__':
    m = Mail(log=sys.argv[1], sql=sys.argv[2]) 
    m.run()
