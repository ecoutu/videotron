#!/usr/bin/python

import argparse
import smtplib
import sys

import requests
import bs4

URL = 'https://extranet.videotron.com/services/secur/extranet/tpia/Usage.do?lang=ENGLISH&compteInternet=%s'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Videotron usage checker')
    parser.add_argument('-e', '--send-email', action='store_true', help='Gmail username')
    parser.add_argument('-l', '--gmail-username', help='Gmail username')
    parser.add_argument('-p', '--gmail-password', help='Gmail password')
    parser.add_argument('-u', '--username', help='Videotron username', required=True)
    args = parser.parse_args()

    url = URL % (args.username, )
    res = requests.get(url)
    if res.status_code != 200:
        print 'Error when contacting Videotron usage site, got status code %s.' % (res.status_code, )
        sys.exit(0)

    soup = bs4.BeautifulSoup(res.content)
    usage = soup.find_all('td', 'reg')[7].string + ' GB'

    print usage

    if not (args.send_email):
        sys.exit(1)

    sender = recipient = smtp_username = args.gmail_username
    smtp_password = args.gmail_password

    if not (smtp_username and smtp_password):
        print 'If you wish to send an email, please provide a Gmail username and password. Try %s --help for usage.' % (sys.argv[0], )
        sys.exit(0)

    subject = 'Videotron usage: ' + usage
    body = ''

    headers = [
        'from: ' + sender,
        'subject: ' + subject,
        'to: ' + sender,
        'mime-version: 1.0',
        'content-type: text/html'
    ]
    headers = '\r\n'.join(headers)

    message = headers + '\r\n\r\n' + body

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(smtp_username, smtp_password)
    session.sendmail(sender, recipient, message)
