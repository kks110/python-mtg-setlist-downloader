#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv

#This writes the file.
def write_file(abc_json, set_count, inc_prerelease, set_type="0"):
    with open('abc.csv', 'a', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if set_type == "":
            writer.writerow(["Number", "Card Name", "Colour", "Rarity"])
        elif set_type == "t":
            writer.writerow(["Tokens"])
        elif set_type == "p":
            writer.writerow(["Promos"])
        for Counter in range(set_count):
            #Prints the data out on screen and also puts it in to the CSV file
            card_name = abc_json['data'][Counter]['name']
            rarity = abc_json['data'][Counter]['rarity']
            colour = abc_json['data'][Counter]['color_identity']
            collector_number = abc_json['data'][Counter]['collector_number']
            if inc_prerelease:
                writer.writerow([collector_number, card_name, colour, rarity])
            else:
                if "s" not in collector_number:
                    writer.writerow([collector_number, card_name, colour, rarity])

def api_call(set_type, inc_prerelease):
    #API call to get the JSON file
    abc_api = "https://api.scryfall.com/sets/" + set_type + "abc"
    response = requests.get(abc_api)
    abc_json = response.json()
    abc_details = abc_json['search_uri']
    full_response = requests.get(abc_details)
    abc_full_json = full_response.json()
    total_cards = abc_full_json['total_cards']
    #Counts the amount of cards in the set
    set_count_stage = abc_full_json['data']
    set_count = len(set_count_stage)
    #Creates the CSV file
    write_file(abc_full_json, set_count, inc_prerelease, set_type)
    #If there are more than 175 cards, code to get the second half. The JSONs only contain info for the first 175 cards
    if set_count == 175:
        abc_continued = abc_full_json['next_page']
        full_response_cont = requests.get(abc_continued)
        abc_cont_json = full_response_cont.json()
        write_file(abc_cont_json, total_cards - 175, inc_prerelease)


def setup():
    inc_prerelease = input("Would you like to include pre-release promos? (y/n) ")
    if inc_prerelease.lower() == "y":
        inc_prerelease = True
        print("Card that are pre-release promos will appear in the promo section, with an S next to their number")
    else:
        inc_prerelease = False
    set_main = ""
    set_token = "t"
    set_promo = "p"
    api_call(set_main, inc_prerelease)
    api_call(set_token, inc_prerelease)
    api_call(set_promo, inc_prerelease)

def main():
    setup()

#This starts my program!
if __name__ == "__main__":
    main()
