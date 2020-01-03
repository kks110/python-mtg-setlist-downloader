import requests
import mtg_card_pull


def valid_set(mtg_set):
    set_api = "https://api.scryfall.com/sets/" + mtg_set
    set_json = requests.get(set_api).json()
    if set_json['object'] == "error":
        print(mtg_set + " is an invalid set name")
        return False
    else:
        return True


def scraper_setup():
    # Sets up the loop
    while True:
        # Asks for the set code
        set_input = input("What is the set code for the set? - ")
        if valid_set(set_input):
            inc_prerelease = input("Would you like to include pre-release promos? (y/n) ")
            if inc_prerelease.lower() == "y":
                inc_prerelease = True
                print("Card that are pre-release promos will appear in the promo section, with an S next to their number")
            else:
                inc_prerelease = False
            mtg_card_pull.setup(set_input, inc_prerelease)
        # Asks is there is another set that needs to be scraped
        another_set = input("Do you have another set you need to download? (y/n) ")
        if another_set.lower() =="y":
            continue
        else:
            break


def main():
    scraper_setup()


# This starts my program!
if __name__ == "__main__":
    main()
