# MTGDeckBuilder

This is a basic deck builder for Magic: The Gathering using the Magic: The Gathering API. It has the following utilities:
  -Search for cards based on name, colors, converted mana cost, type, subtype, rarity, set, keywords, power, and toughness.
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
