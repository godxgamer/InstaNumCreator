print("This is an example to use api in python manually , You can connect any sms site and proxy and automate the account creation process faster without any issue in any language\n\n\n")

import requests

# API headers
apikey=str(input("enter your apikey : "))
headers = {
    "Content-Type": "application/json",
    "X-API-Key": apikey,  # Replace with your actual API key
}

# Base URL of the API
base_url = 'http://128.140.99.16:5623'

# number for Instagram registration
number = str(input("enter your number : "))  # Note Always Use least Flagged Domains for email like gmail,outlook,hotmailInstagram Is Very Strict With Email Account Registratin They Block or susspend Account Registered With Temp Mails


# Proxy details for making requests
proxy_path = str(input("enter your proxy : ")) # Replace with your actual proxy details. username of your paid proxy " : " password of Your proxy " @ " Host of proxy " : " Port of proxy  " example =   smartuser:ERvccvRRTgfd@gate.smartptoxy.com:7777 You Can Also Use Free Proxy Of Any Country " Only Proxy Should Be alive

# Data payload for the API request
data = {
    "number": number,
    "proxy": proxy_path,
    # "country_code": country_code
}

#Guys If Want to pass Your Username And Password
# add two parameters data =
"""{
    "full_name":'gamer', 
    "password":'gamerrrrr',
    "number": email,
    "proxy": proxy_path,
}
"""

# Sending an SMS containing OTP to the provided number
sendsms = requests.post(
    url=f'{base_url}/api/insta/android/number/send',
    json=data,
    headers=headers,
    timeout=200
)

# Checking if 6 digit confirmation code sent is in the response text
if '6 digit confirmation code sent' in sendsms.text:
    print(sendsms.json()['response'])
    otp = str(input("Enter OTP: "))

    # Data for the second API request, including the response from the first API
    data = {
        "otp": otp,
        "proxy": proxy_path,
        "client_data": sendsms.json()
    }

    # Verifying OTP and creating an account using number
    create = requests.post(
        url=f'{base_url}/api/insta/android/number/create',
        json=data,
        headers=headers,
        timeout=200
    ).json()
    if "username" in str(create):
        with open("saved_account.txt","a")as acct:
            acct.write(f'{create}\n')
            acct.close()

    print(create)
else:
    print(sendsms.text)

"""
You can use this API in any language (py, php, js, Go, java) to create your own account registration automation.

For bulk account creation or any queries, join @gxbytes for updates and upcoming features. 
If you have any queries about this API, you can contact me on Telegram. My username is '@god_x_gamer'.
"""
