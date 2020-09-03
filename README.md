# Num_Verify
## A phone number authenticity verification using REST APIs
This is a light weight code snippet which uses the API-layer's ipstack API to gather validity, location and other data for a given phone number.

### Dependencies include: (USE PIP)
1. Requests 
2. IPstack - Geolookup
3 json 

### The given phone number's information includes (in JSON format)
1. Number validity
2. Local format of the phone number 
3. Int'l format of the phone number 
4. Country code and country name 
5. Location
6. Carrier 
7. Line type 
'''    
{
   "valid": true,   
   "local_format": "4158586273",
   "intl_format": "+14158586273",
   "country_code": "US",
   "country_name": "United States of America",
   "location": "Novato",
   "carrier": "AT&T Mobility LLC",
   "line_type": "mobile"
}
'''

#### Use a JSON handler to extract data and test it against set conditions.
#### From the top of the head, this code snippet can be used for  

#### Note: Make sure that your api key isnt't hardcoded to the application and it is stored to the application. 

#### Feel free to use the code and suggest changes or improve the code or the documentation by raising an issue or creating a pull request and sharing a gist of the change. 

#### Coded and managed by:
### Team Sonic_Boom:
1. Guru Prasad R
2. Akshaya N
3. Thrisha
4. Nitheshkumar 
5. Dikshith 

