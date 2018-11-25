

def scraperSetUp():
    #Sets up the loop
    while True:
        #Asks for the set code
        setInput = input("What is the set code for the set? - ")
        #Opens the base file and creates a new file using the set name
        f1 = open('mtg_cardPull.py', 'r')
        f2 = open(setInput + '_cardPull.py', 'w')
        for line in f1:
            f2.write(line.replace('abc', setInput))
        f1.close()
        f2.close()
        createdFile = setInput + '_cardPull'
        #Runs the created file
        DataScraper = __import__(createdFile)
        DataScraper.main()
        #Asks is there is another set that needs to be scraped
        another_set = input("Do you have another set you need to download? (Y/N) ")
        if another_set =="y":
            continue
        else:
            break


def main():
    scraperSetUp()

#This starts my program!
if __name__ == "__main__":
    main()
