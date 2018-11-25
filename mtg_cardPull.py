#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv


def findFirstHalfFullSetAPI():
    #API call to get the JSON file
    abcAPI = "https://api.scryfall.com/sets/abc"
    response = requests.get(abcAPI)
    abcJSON = response.json()
    abcDetails = abcJSON['search_uri']
    fullResponse = requests.get(abcDetails)
    abcFullJSON = fullResponse.json()
    total_cards = abcFullJSON['total_cards']
    #Creates the CSV file
    with open('abc.csv', 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #Counts the amount of cards in the set
        setCountStage = abcFullJSON['data']
        setCount = len(setCountStage)
        writer.writerow(["Number", "Name", "Colour", "Rarity"])
        for Counter in range(setCount):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = abcFullJSON['data'][Counter]['name']
            rarity = abcFullJSON['data'][Counter]['rarity']
            colour = abcFullJSON['data'][Counter]['color_identity']
            CollectorNumber = abcFullJSON['data'][Counter]['collector_number'] 
            writer.writerow([CollectorNumber, CardName, colour, rarity])
    #If there are more than 175 cards, code to get the second half. The JSONs only contain info for the first 175 cards
    if setCount == 175:
        findSecondHalfFullSet()


def findSecondHalfFullSet():
    #API call to get the JSON file
    abcAPI = "https://api.scryfall.com/sets/abc"
    response = requests.get(abcAPI)
    abcJSON = response.json()
    abcDetails = abcJSON['search_uri']
    fullResponse = requests.get(abcDetails)
    abcFullJSON = fullResponse.json()
    total_cards = abcFullJSON['total_cards']
    abcContinued = abcFullJSON['next_page']
    fullResponseCont = requests.get(abcContinued)
    abcContJSON = fullResponseCont.json()
    #Opens the CSV file and appends to it
    with open('abc.csv', 'a',  newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #Counts the amount of cards in the second half of the set
        for Counter in range(total_cards - 175):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = abcContJSON['data'][Counter]['name']
            rarity = abcContJSON['data'][Counter]['rarity']
            colour = abcContJSON['data'][Counter]['color_identity']
            CollectorNumber = abcContJSON['data'][Counter]['collector_number']
            writer.writerow([CollectorNumber, CardName, colour, rarity])


def tokens():
    #API call to get the JSON file
    abcAPI = "https://api.scryfall.com/sets/tabc"
    response = requests.get(abcAPI)
    abcJSON = response.json()
    abcDetails = abcJSON['search_uri']
    fullResponse = requests.get(abcDetails)
    abcFullJSON = fullResponse.json()
    total_cards = abcFullJSON['total_cards']
    #Opens the CSV file and appends to it
    with open('abc.csv', 'a',  newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #Counts the amount of tokens
        tokenCountStage = abcFullJSON['data']
        tokenCount = len(tokenCountStage)
        for Counter in range(tokenCount):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = abcFullJSON['data'][Counter]['name']
            rarity = abcFullJSON['data'][Counter]['rarity']
            colour = abcFullJSON['data'][Counter]['color_identity']
            CollectorNumber = abcFullJSON['data'][Counter]['collector_number'] 
            writer.writerow([CollectorNumber, CardName, colour, rarity])


def promo():
    #API call to get the JSON file
    abcAPI = "https://api.scryfall.com/sets/pabc"
    response = requests.get(abcAPI)
    abcJSON = response.json()
    abcDetails = abcJSON['search_uri']
    fullResponse = requests.get(abcDetails)
    abcFullJSON = fullResponse.json()
    total_cards = abcFullJSON['total_cards']
    #Opens the CSV file and appends to it
    with open('abc.csv', 'a',  newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #Counts the amount of tokens
        promoCountStage = abcFullJSON['data']
        promoCount = len(promoCountStage)
        for Counter in range(promoCount):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = abcFullJSON['data'][Counter]['name']
            rarity = abcFullJSON['data'][Counter]['rarity']
            colour = abcFullJSON['data'][Counter]['color_identity']
            CollectorNumber = abcFullJSON['data'][Counter]['collector_number'] 
            writer.writerow([CollectorNumber, CardName, colour, rarity])



def main():
    findFirstHalfFullSetAPI()
    tokens()
    promo()

#This starts my program!
if __name__ == "__main__":
    main()
