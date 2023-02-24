"""
Project Name : Track Phonenumber Location.
Author : Shaily Kesharwani
Date : 20/02/2023
Language : Python 3.10.6
Details : This is the tracker of phonenumber location.
Version : 1.0.1
"""


import phonenumbers
#phonenumbers is a module 
import time
from phonenumbers import geocoder
from phonenumbers import timezone

#Geocoder - Its the process of transforming a description of a location 
number = input("Enter the number with country code: ")
time.sleep(2)

print("\nTracking...\n")
time.sleep(2)

phoneNumber = phonenumbers.parse(number)
print("Its tracked...the number is from")
timeZone = timezone.time_zones_for_number(phoneNumber)
# print(phoneNumber)
print(timeZone)


ch_nmber = phonenumbers.parse(number, "CH")
#CH - country history
print(geocoder.description_for_number(ch_nmber , "en"))


from phonenumbers import carrier
#carrier - is a function it helps you get the name of the service provider of the phone number you're tracking
service_nmber = phonenumbers.parse(number, "RO")

print("\nAnd SIM is..")
print(carrier.name_for_number(service_nmber , "en"))

