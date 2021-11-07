import urllib.parse
import requests
import colorama
from colorama import Fore
from colorama import Style

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Rigu6LhDU2Utq3Y1UBoZMzPUhcE1yzTG"

while True: 
    user_name = input(Fore.RESET + "Name of the user: ") 
    if user_name == "quit" or user_name == "q": 
        break
    orig = input(Fore.RESET + "Starting Location: ") 
    if orig == "quit" or orig == "q": 
        break
    dest = input(Fore.RESET + "Destination: ") 
    if dest == "quit" or dest == "q": 
        break
        
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print(Fore.GREEN + "Hello " + user_name + "! Here are your directions: ")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(Fore.GREEN + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print('Extra Information: ')
            if json_data["route"]["legs"][0]['hasTollRoad'] == True:
                print("This direction has a toll fee.")
            else:
                print("This direction does not have a toll fee.")

            if json_data["route"]["legs"][0]['hasUnpaved'] == True:
                print("This direction has unpaved road.")
            else:
                print("This direction has a paved road.")
            
            print("=============================================\n") 
        print("Fuel Used The Entire Trip: " + str(json_data["route"]["fuelUsed"]))
    elif json_status == 402: 
        print("**********************************************") 
        print(Fore.RED + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.") 
        print("**********************************************\n") 
    elif json_status == 611: 
        print("**********************************************") 
        print(Fore.RED + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.") 
        print("**********************************************\n")
    else:
        print("************************************************************************") 
        print(Fore.RED + "For Staus Code: " + str(json_status) + "; Refer to:") 
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") 
        print("************************************************************************\n")