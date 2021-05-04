# MTGDeckBuilder

This is a basic deck builder for Magic: The Gathering using the Magic: The Gathering API. It has the following utilities:

  -Search for cards based on name, colors, converted mana cost, type, subtype, rarity, set, card text, power, and toughness.
  
  -Add and remove searched cards from the decklist.
  
  -Import an existing decklist.
  
  -Export the current decklist to a .txt file. 
  
  -Additionally, decklists created using this app are formated to be directly copy/paste into https://www.tcgplayer.com/massentry, allowing the user to quickly buy all the cards from the decklist.
  
# How To Launch

1. Download the "MTG DeckBuilder" folder from this repository.
2. Open the command prompt and change into the folder "MTG DeckBuilder"
3. Ensure that the following python libraries are installed: requests, flask, mtgsdk. If they are not installed, use the command prompt to pip install them. ("py -m pip install requests", etc)
4. Launch the python program ("py mtgdeckbuilder.py")
5. Open up a broweser (Google Chrome preferred) and go to the following address: "localhost:5000"

# Importing Decklists

Decklists can be imported into the app by first ensuring that the .txt file containing the decklist is saved in the "MTG Deckbuilder" folder. Type the name of the .txt file without the extenstion (ex. "sampledecklist", not "sampledecklist.txt"). Lastly, click the Import Decklist button. The decklist from the text file will override the current active decklist, so be sure to export the active decklist if you want to save it first!

Please note that decklists have a specific format. Each line contains the quantity of the card in the deck, followeed by the card name (ex. "1 Counterspell"). Any additional text in the .txt file may prevent the full decklist from being loaded correctly.

#Exporting Decklists

Decklists can be exported to a .txt file, allowing the user to save progress on building the deck. To export the current decklist, simply type the filename of the .txt file you want to create or override and click "Export Decklist." The decklist will be saved in the "MTG DeckBuilder" folder. 

#Search Filters

The main feature of this app is to be able to search for cards to add to your deck. The following search filters can be used to help narrow the results to find the best cards for your deck, although none of them are manditory.

Name - The name of the card. This can be an exact name, or can be a word that appears in the name.

Colors - Thses are the colors that will be on the card. Other colors may appear, but the checked colors are guaranteed to appear.

Converted Mana Cost (CMC) - This is the total mana cost of the card. This is found by adding the colored mana and the non-colored mana listed in the top right of the card. Note that the "X" mana cost on cards does not count towards this number.

Type - The type of card. Examples: Creature, Artifact, Instant

Subtype - Subtypes/Archtypes of the card. Examples: Goblin, Angel, Vampire

Rarity - The rarity of the card

Set - The set code that the card(s) come from. Note that this is not the same as the set name. Examole: "SOI", not "Shadows over Innistrad."

Text - Any words/keywords that appear in the effect text of the card. Examoles: flying, deathtouch

Power - The power listed on creatures

Toughness - The toughness listed on creatures.

#Adding and Removing Cards from the Decklist

To add or remove a card from the decklist:

1. Search for the card using the search filters.
2. Click on the card.
3. Click "Add" to add to the decklist, or "remove" to remove it from the decklist.
4. Click "Return to Deckbuilder" to return to the search screen.

#Functionality with TCGPlayer

The decklist is formatted specifically to be used with TCGPlayer.com in order to purchase physical copies of the cards for your deck. Simply go to tcgplayer.com/massentry and copy/paste the decklist, then click "Add to Cart." 

DISCLAIMER: Some cards may be out of print/out of stock. 

#Credits

MTG DeckBuilder was created by Justin Sanner as his final undergraduate project at Columbus State University under the supervision of Jose Canedo. 
