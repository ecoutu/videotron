Videotron Usage Checker
=======================

This tool will retrieve your monthly usage of a Videotron based service, optionally sending yourself an email. The -u switch specifies the Videotron account number to check (you're vlxxxxxx number). The -e, -l and -p switches provide the Gmail account used to send and receive emails.

    usage: usage_checker.py [-h] [-e] [-l GMAIL_USERNAME] [-p GMAIL_PASSWORD] -u
                            USERNAME

    Videotron usage checker

    optional arguments:
      -h, --help            show this help message and exit
      -e, --send-email      Gmail username
      -l GMAIL_USERNAME, --gmail-username GMAIL_USERNAME
                            Gmail username
      -p GMAIL_PASSWORD, --gmail-password GMAIL_PASSWORD
                            Gmail password
      -u USERNAME, --username USERNAME
                            Videotron username
