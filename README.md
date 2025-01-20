# WhatsApp Message Scheduler

A Python script to schedule and send WhatsApp messages at a specific date and time using the Twilio API.

## What It Does

- Allows you to send WhatsApp messages programmatically.
- Lets you schedule messages to be sent at a specific future date and time.
- Uses the Twilio API for sending WhatsApp messages.

## Features

- **Scheduled Messaging:** Send messages at a specified date and time.
- **Simple Input:** Enter recipient details, message, and schedule time via the command line.
- **Error Handling:** Basic error handling for failed message delivery.

## Technologies Used

- **Python:** The scripting language used.
- **Twilio API:** For sending WhatsApp messages.
- **datetime and time modules:** For scheduling and timing the message delivery.

## How to Use

1. **Set Up Twilio:**
   - Create a Twilio account and get your `Account SID` and `Auth Token`.
   - Verify your WhatsApp number in Twilio.

2. **Configure the Script:**
   - Replace the placeholders in the script with your Twilio credentials:
     ```python
     account_sid = 'your_account_sid'
     auth_token = 'your_auth_token'
     ```

3. **Run the Script:**
   - Execute the script and provide the required inputs:
     - Recipient's name
     - Recipient's WhatsApp number (with country code)
     - Message body
     - Scheduled date and time (in `YYYY-MM-DD` and `HH:MM` format)

4. **Sit Back and Relax:**
   - The script will send the message at the scheduled time.

---

Feel free to contribute or modify the script to suit your needs!


## Connect With Me

- [![X](https://img.shields.io/badge/X-@alkayesrifat-blue)](https://x.com/alkayesrifat)
- [![Facebook](https://img.shields.io/badge/Facebook-@alkayesrifat-blue)](https://www.facebook.com/alkayesrifat)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-@alkayesrifat-blue)](https://linkedin.com/in/alkayesrifat)
- [![Instagram](https://img.shields.io/badge/Instagram-@alkayesrifat-blue)](https://instagram.com/alkayesrifat)
- [![Website](https://img.shields.io/badge/Website-alkayesrifat.netlify.app-blue)](https://alkayesrifat.netlify.app/)
