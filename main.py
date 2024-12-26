from twilio.rest import Client
from datetime import datetime , timedelta
import time

account_sid =''
auth_token = ''


Client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number , message_body):
    try:
        message = Client.messages.create(
            from_= 'whatsapp:',
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'Message sent Successfully! Message SID{message.sid}')
    except Exception as e:
        print('An Error Occured')


name = input('Enter the Recipient Name : ')
recipient_number = input('Enter the Recipient Whatsapp Number With country code : ')
message_body = input(f'Enter the message you want to send to {name}')



date_str = input('Enter the data to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24 Hour Format) :')


schedule_datetime = datetime.strptime(f'{date_str} {time_str}' , "%Y-%m-%d %H:%M")

current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime

delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past , Please enter a Future date and time : ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_seconds)

    send_whatsapp_message(recipient_number,message_body)

