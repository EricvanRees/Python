#
# coding: utf-8
#
# In[ ]:

import requests
import smtplib

def get_emails():
    # Reading emails from a file
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip() #creates entries in dict, see also:
            # https://developmentality.wordpress.com/2012/03/30/three-ways-of-creating-dictionaries-in-python/

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    # Reading a schedule from a file
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    return schedule

def get_weather_forecast():
    #Connecting to the weather API
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Orlando,Fl&units=imperial&appid=###' #number doesn´t work...
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast

def send_emails(emails, schedule, forecast):
    # Connect to SMTP server
    server = smtplib.SMTP('smpt.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    #Login
    password = input("What´s your password?")
    from_email = 'youremailaddress@gmail.com'
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Circus!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email, to_email, message)

    server.quit()

def main():
    emails = get_emails()

    schedule = get_schedule()

    forecast = get_weather_forecast()

    send_emails(emails, schedule, forecast)

main()

