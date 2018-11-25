#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv


def writeFile(abcJSON, setCount):
    with open('abc.csv', 'a', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        reader = csv.reader(csv_file, delimiter=',')
        for Counter in range(setCount):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = abcJSON['data'][Counter]['name']
            rarity = abcJSON['data'][Counter]['rarity']
            colour = abcJSON['data'][Counter]['color_identity']
            CollectorNumber = abcJSON['data'][Counter]['collector_number'] 
            writer.writerow([CollectorNumber, CardName, colour, rarity])

def findFirstHalfFullSetAPI(set_type):
    #API call to get the JSON file
    abcAPI = "https://api.scryfall.com/sets/" + set_type + "abc"
    response = requests.get(abcAPI)
    abcJSON = response.json()
    abcDetails = abcJSON['search_uri']
    fullResponse = requests.get(abcDetails)
    abcFullJSON = fullResponse.json()
    total_cards = abcFullJSON['total_cards']
    #Counts the amount of cards in the set
    setCountStage = abcFullJSON['data']
    setCount = len(setCountStage)
    #Creates the CSV file
    writeFile(abcFullJSON, setCount)
    #If there are more than 175 cards, code to get the second half. The JSONs only contain info for the first 175 cards
    if setCount == 175:
        abcContinued = abcFullJSON['next_page']
        fullResponseCont = requests.get(abcContinued)
        abcContJSON = fullResponseCont.json()
        writeFile(abcContJSON, total_cards - 175)


def setup():
    setMain = ""
    setToken = "t"
    setPromo = "p"
    findFirstHalfFullSetAPI(setMain)
    findFirstHalfFullSetAPI(setToken)
    findFirstHalfFullSetAPI(setPromo)

def main():
    setup()

#This starts my program!
if __name__ == "__main__":
    main()

