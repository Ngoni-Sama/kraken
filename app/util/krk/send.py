from os import system as ss
import argparse
from subprocess import Popen, PIPE, STDOUT
import time


def send_sms(phone, message):
    """

    Args:
        phone:
        message:

    Returns:

    """
    print("[+] Sender PHONE:{}, MESSAGE:{}".format(phone, message))
    ss('echo "' + message.replace("'", "") + '" | sudo gammu sendsms TEXT ' + phone + ' > outt.txt')

    with open("outt.txt", "r") as fout:
        response = fout.read()
        print("[+] response:", response)
        if "busy or no permissions" in response:
            return False
        else:
            return True


def try_send_sms(phone, message, delay=3, limit_trying=5):
    """

    Args:
        phone:
        message:
        delay:
        limit_trying:

    Returns:

    """
    r = send_sms(phone, message)
    count_trying = 1
    while not r:
        print("[+] Failed to send message, retrying...")
        time.sleep(delay)
        r = send_sms(phone, message)
        if count_trying >= limit_trying:
            print("[+] Tried count exceed, the device has a problem or is not well connected !")
            break


if __name__ == '__main__':
    # Initialize the arguments
    # Example test : python send.py -p 6******* -m "This is a test message, for fun"
    prs = argparse.ArgumentParser()
    prs.add_argument('-p', '--phone', help='The phone number', type=str, required=True)
    prs.add_argument('-m', '--message', help='The message you want to send in SMS', type=str, required=True)
    prs.add_argument('-i', '--iteration', help='The number of time you want to send this message', type=int, default=1)
    prs = prs.parse_args()

    for i in range(prs.iteration):
        try_send_sms(prs.phone, prs.message)
