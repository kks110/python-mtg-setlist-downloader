

def scraperSetUp():
    #Sets up the loop.
    while True:
        #Asks for the set code.
        set_input = input("What is the set code for the set? - ")
        #Opens the base file and creates a new file using the set name.
        f1 = open('mtg_cardPull.py', 'r')
        f2 = open(set_input + '_cardPull.py', 'w')
        for line in f1:
            f2.write(line.replace('abc', set_input))
        f1.close()
        f2.close()
        created_file = set_input + '_cardPull'
        #Runs the created file.
        data_scraper = __import__(created_file)
        data_scraper.main()
        #Asks is there is another set that needs to be scraped.
        another_set = input("Do you have another set you need to download? (y/n) ")
        if another_set.lower() =="y":
            continue
        else:
            break


def main():
    scraperSetUp()

#This starts my program!
if __name__ == "__main__":
    main()
