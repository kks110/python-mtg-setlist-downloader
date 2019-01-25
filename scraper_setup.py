

def scraper_setup():
    #Sets up the loop
    while True:
        #Asks for the set code
        set_input = input("What is the set code for the set? - ")
        #Opens the base file and creates a new file using the set name
        f1 = open('mtg_card_pull.py', 'r')
        f2 = open(set_input + '_card_pull.py', 'w')
        for line in f1:
            f2.write(line.replace('xyz', set_input))
        f1.close()
        f2.close()
        created_file = set_input + '_card_pull'
        #Runs the created file
        data_scraper = __import__(created_file)
        data_scraper.main()
        #Asks is there is another set that needs to be scraped
        another_set = input("Do you have another set you need to download? (y/N) ")
        if another_set.lower() =="y":
            continue
        else:
            break


def main():
    scraper_setup()

#This starts my program!
if __name__ == "__main__":
    main()