# Num_Verify
## A phone number authenticity verification using REST APIs
This is a light weight code snippet which uses the API-layer's ipstack API to gather validity, location and other data for a given phone number.
Create an account with [NumVerify] (https://numverify.com/product) to begin with. 

Dependencies include: (USE PIP)
: Requests 
: IPstack - Geolookup
: JSON

The given phone number's information includes (in JSON format)
: Number validity
: Local format of the phone number 
: Int'l format of the phone number 
: Country code and country name 
: Location
: Carrier 
: Line type 

Use a JSON handler to extract data and test it against set conditions.
From the top of the head, this code snippet can be used for:
: Restricting app usage to users originating from a location
: Ensuring validity of the number
: can restrict app access depending upon Phone number type

**Note: Make sure that your api key isnt't hardcoded to the application and it is stored in a secure db. Sqlite will work just fine.**



#### Coded and managed by:
Team Sonic_Boom
: Guru Prasad R
: Akshaya N
: Thrisha
: Nitheshkumar 
: Dikshith 

**Feel free to use the code and suggest changes or contribute to the code or the documentation by raising an issue or creating a branch and starting a pull request.**

**Viva Open Source**

