import requests
#accesskey is the pyhton script used to save the api keys. Please dont hardcode your api keys, especially if your code is opensource.
import accesskey 
import json

def num_verify():
    phone_number = input("Please enter your phone number: ")
    




    print(f"Your phone number is {phone_number}")

    url = 'http://apilayer.net/api/validate?access_key=' + accesskey.access_key_num + '&number=' + phone_number
    response = requests.get(url)
    print (response.content)

    resp = json.loads(response.content)
    if resp['valid']:
        print("the number is valid")
  

        
