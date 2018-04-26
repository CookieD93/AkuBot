# import our wrapper class for reference
import time
from imapclient import IMAPClient, SEEN
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

SEEN_FLAG = 'SEEN'
UNSEEN_FLAG = 'UNSEEN'

class GmailWrapper:
    def __init__(self, host, userName, password):
        #   force the user to pass along username and password to log in as
        self.host = host
        self.userName = userName
        self.password = password
        self.login()

    def login(self):
        print('Logging in as ' + self.userName)
        server = IMAPClient(self.host, use_uid=True, ssl=True)
        server.login(self.userName, self.password)
        self.server = server

    #   The IMAPClient search returns a list of Id's that match the given criteria.
    #   An Id in this case identifies a specific email
    def getUnseen(self, folder='INBOX' ):
        self.setFolder(folder)

        self.searchCriteria = [UNSEEN_FLAG]


        return self.server.search(self.searchCriteria)

    def markAsRead(self, mailIds, folder='INBOX'):
        self.setFolder(folder)
        self.server.set_flags(mailIds, [SEEN])

    def setFolder(self, folder):
        self.server.select_folder(folder)


gmailWrapper = GmailWrapper('imap.gmail.com', 'my@email.com', 'myPassword')


MAIL_CHECK_FREQ = 60 # check mail every 60 seconds
NEWMAIL_OFFSET = gmailWrapper.getUnseen()


def MoveArm():
    pwm = GPIO.PWM(11, 50)

    pwm.start(5)
    time.sleep(1)

    pwm.ChangeDutyCycle(12)
    time.sleep(2)

    pwm.ChangeDutyCycle(5)
    time.sleep(1)
    pwm.ChangeDutyCycle(5)


if __name__ == '__main__':
    try:
        print ('Press Ctrl-C to quit.')
        while True:
            newmails = gmailWrapper.getUnseen()
            numbermails = len(newmails)

            if numbermails != NEWMAIL_OFFSET:
                MoveArm()
                print('ny mail')
            else:
                print('ikke ny mail')
            NEWMAIL_OFFSET = numbermails
            time.sleep(20)
            print('kører stadig')
    finally:
        GPIO.cleanup()
        time.sleep(1)
