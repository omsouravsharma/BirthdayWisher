import pandas as pd
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################
my_email = 'enter_email'
password = 'password'
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        data = letter_file.read()
        contents = data.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday\n\n{contents}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
