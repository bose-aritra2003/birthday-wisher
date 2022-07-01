# Program to send happy birthday message to automated happy birthday wish to mentioned people
import pandas
import datetime as dt
import random
import smtplib

LETTER_FORMATS_PATH = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

sender_email = "world.hello2003@gmail.com"
sender_password = "123aritra@#$"

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")

for i in range(len(birthdays_dict)):
    if dt.datetime.now().day == birthdays_dict[i]["day"] and dt.datetime.now().month == birthdays_dict[i]["month"]:
        with open(file=random.choice(LETTER_FORMATS_PATH), mode="r") as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace("[NAME]", birthdays_dict[i]["name"])
            recipient_email = birthdays_dict[i]["email"]
            with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(user=sender_email, password=sender_password)
                server.sendmail(
                    from_addr=sender_email,
                    to_addrs=recipient_email,
                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{new_letter}".encode("utf-8"))
