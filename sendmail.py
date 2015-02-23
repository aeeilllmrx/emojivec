# gmail through python!

import smtplib
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()

username = "" # set
password = "" # set
session.login(username, password)

recipient = "" # set

headers = "\r\n".join(["from: " + username, \
		       "to: " + recipient, \
		       "mime-version: 1.0", \
		       "content-type: text/html"])

body = "i'm sending this email from python" # change
content = headers + "\r\n\r\n" + body
session.sendmail(username, recipient, body)
