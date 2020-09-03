# Num_Verify
## A phone number authenticity verification using REST APIs
This is a light weight code snippet which uses the API-layer's ipstack API to gather validity, location and other data for a given phone number.
Create an account with [NumVerify] (https://numverify.com/product) to begin with. 

Dependencies include: (USE PIP)
1. Requests 
2. IPstack - Geolookup
3. JSON

The given phone number's information includes (in JSON format)
1. Number validity
2. Local format of the phone number 
3. Int'l format of the phone number 
4. Country code and country name 
5. Location
6. Carrier 
7. Line type 

Use a JSON handler to extract data and test it against set conditions.
From the top of the head, this code snippet can be used for:
1. Restricting app usage to users originating from a location
2. Ensuring validity of the number
3. can restrict app access depending upon Phone number type

**Note: Make sure that your api key isnt't hardcoded to the application and it is stored in a secure db. Sqlite will work just fine.**



#### Coded and managed by:
Team Sonic_Boom:
1. Guru Prasad R
2. Akshaya N
3. Thrisha
4. Nitheshkumar 
5. Dikshith 

**Feel free to use the code and suggest changes or contribute to the code or the documentation by raising an issue or creating a branch and starting a pull request.**

**Viva Open Source**

