import json
import smtplib
from smtplib import SMTPAuthenticationError
from random import choice
import pandas
import datetime as dt
from email.mime.text import MIMEText
import os


def _get_random_template():
    with open("data/templates.json", "r", encoding="utf-8") as file:
        templates = json.load(file)
        random_key = choice(list(templates.keys()))
        random_template = templates[random_key]
        return random_template


def _get_birthdays_list():
    with open("data/birthdays.csv", "r", encoding="utf-8") as file:
        bd_list = pandas.read_csv(file)
        return bd_list.to_dict(orient="records")


def _load_credentials():
    try:
        with open("data/credentials.json", "r") as file:
            credentials = json.load(file)

    except FileNotFoundError:
        error_message = "Credential Error: Required information is missing." \
                        "Please enter your email provider credentials.\n" \
                        "For Gmail users, it is necessary to create an app password." \
                        "For more information on this process, refer to the following link:\n" \
                        "https://support.google.com/accounts/answer/185833?visit_id=638107597085752106-702683512&" \
                        "p=InvalidSecondFactor&rd=1#zippy=%2Cwhy-you-may-need-an-app-password"
        print(error_message)
        try:
            username = input("Your email username: ")
            password = input("Your email password: ")
        except EOFError:
            print("Terminating program...")
            exit()
        credentials = {
            "username": f"{username}",
            "password": f"{password}"
        }
        with open("data/credentials.json", "w") as file:
            json.dump(credentials, file, indent=4)
    return credentials


class BDSender:
    def __init__(self):
        super().__init__()
        self.credentials = _load_credentials()
        self._validate_credentials()

    def check_birthdays_and_send_emails(self):
        bd_list = _get_birthdays_list()
        now = dt.datetime.now()
        for person in bd_list:
            person_bd = dt.datetime(year=person["year"], month=person["month"], day=person["day"])
            if now.month == person_bd.month and now.day == person_bd.day:
                message_template: str = _get_random_template()["text"]
                message_template = message_template.replace("[PREFIX]", person["prefix"])
                message_template = message_template.replace("[NAME]", person["name"])
                message = MIMEText(message_template, "plain", "utf-8")
                message["Subject"] = "Všetko najlepšie k narodeninám!"

                self._send_email(person["email"], message)
                print(f"Email sent to {person['name']}")

    def _send_email(self, to_address, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.credentials["username"], password=self.credentials["password"])
            connection.sendmail(from_addr=self.credentials["username"],
                                to_addrs=to_address,
                                msg=message.as_bytes())

    def _validate_credentials(self):
        valid_smtps = {
            "aol.com": "smtp.aol.com",
            "att.net": "smtp.mail.att.net",
            "comcast.net": "smtp.comcast.net",
            "icloud.com/mail": "smtp.mail.me.com",
            "gmail.com": "smtp.gmail.com",
            "outlook.com": "smtp-mail.outlook.com",
            "mail.yahoo.com": "smtp.mail.yahoo.com"
        }
        try:
            smtp = valid_smtps[self.credentials["username"].split("@", 1)[1]]

            with smtplib.SMTP(smtp) as connection:
                connection.starttls()
                connection.login(user=self.credentials["username"], password=self.credentials["password"])

        except (KeyError, IndexError, SMTPAuthenticationError) as e:
            if isinstance(e, SMTPAuthenticationError):
                print("The server didn't accept the username/password combination. Enter username and password again.\n")
            if isinstance(e, KeyError) or isinstance(e, IndexError):
                print("Unsupported or invalid email address. Enter username and password again.\n")
            os.remove("data/credentials.json")
            self.credentials = _load_credentials()
            self._validate_credentials()

        else:
            print("Authentication was successful.")
