import email
from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'username'
PASSWORD = 'password'
ssl = True

## Connect, login and select the INBOX
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)
select_info = server.select_folder('INBOX')

## Search for relevant messages
messages = server.search(
    ['FROM "sender"', 'SINCE 1-Feb-2014'])
response = server.fetch(messages, ['RFC822', 'BODY[TEXT]'])

print "hello?"

for msgid, data in response.iteritems():
    parsedEmail = email.message_from_string(data['RFC822'])
    print 'From: ', parsedEmail['From']
    print 'Date: ', parsedEmail['date']
    print 'Subject: ', parsedEmail['Subject']

    #still some nonsense first few lines of email
    body = email.message_from_string(data['BODY[TEXT]'])
    parsedBody = parsedEmail.get_payload(0)
    print parsedBody
