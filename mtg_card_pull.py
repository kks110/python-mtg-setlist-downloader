# Used to get the URL
import requests
# Used to export the data to a CSV
import csv


# This writes the file.
def write_file(mtg_set, set_json, set_count, inc_prerelease, set_type="c"):
    with open(mtg_set + '.csv', 'a', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if set_type == "":
            writer.writerow(["Number", "Card Name", "Colour", "Rarity"])
        elif set_type == "t":
            writer.writerow(["Tokens"])
        elif set_type == "p":
            writer.writerow(["Promos"])
        for x in range(set_count):
            # Appends data to the CSV file
            card_name = set_json['data'][x]['name']
            rarity = set_json['data'][x]['rarity']
            colour = set_json['data'][x]['color_identity']
            collector_number = set_json['data'][x]['collector_number']
            if inc_prerelease:
                writer.writerow([collector_number, card_name, colour, rarity])
            else:
                if "s" not in collector_number:
                    writer.writerow([collector_number, card_name, colour, rarity])


def api_call(mtg_set, set_type, inc_prerelease):
    card_counter = 0
    # API call to get the JSON file
    set_api = "https://api.scryfall.com/sets/" + set_type + mtg_set
    set_json = requests.get(set_api).json()
    if set_json['object'] != "error":
        set_details = set_json['search_uri']
        set_full_json = requests.get(set_details).json()
        total_cards = set_full_json['total_cards']
        # Counts the amount of cards in the set
        set_count = len(set_full_json['data'])
        # Creates the CSV file
        write_file(mtg_set, set_full_json, set_count, inc_prerelease, set_type)
        card_counter += set_count
        # If there are more than 175 cards, code to get the second half.
        # The JSONs only contain info for the first 175 cards
        while card_counter < total_cards:
            continued = set_full_json['next_page']
            set_full_json = requests.get(continued).json()
            set_count = (len(set_full_json['data']))
            write_file(mtg_set, set_full_json, set_count, inc_prerelease)
            card_counter += set_count
    else:
        print("An error has occured. Maybe the set code was wrong?")


def setup(mtg_set, inc_prerelease):
    set_main = ""
    set_token = "t"
    set_promo = "p"
    api_call(mtg_set, set_main, inc_prerelease)
    api_call(mtg_set, set_token, inc_prerelease)
    api_call(mtg_set, set_promo, inc_prerelease)


