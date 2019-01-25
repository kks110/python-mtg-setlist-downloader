# python-mtg-set-list-downloader
Enter a set name and download a list of cards for the set.

Requests is required for this to run. Install with pip:
```
py -m pip install requests
```

Ensure that both files are saved in the same location.

First run scraperSetUp.py, it will ask for the set code.

This will then create a new file using mtg_cardPull.py, which will then download a csv with all the cards, tokens and promo cards.
