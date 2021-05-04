import requests
from flask import Flask, render_template, url_for, request, redirect
from mtgsdk import Card, Set, Type, Supertype, Subtype, Changelog
from classCard import deckCard, result


#initialize
app = Flask(__name__)

decklist = []
results = []
defaultResult = result("", "")

#adds a card to the decklist
def add(selectedCard):
    changed = False

    #if card is in decklist, increment quantity by 1
    for card in decklist:
        if card.getName() == selectedCard:
            card.quantity += 1
            changed = True

    #if card is not in decklist, create deckCard object and add to decklist
    if changed == False:
        selectedCard = deckCard(selectedCard, 1)
        decklist.append(selectedCard)

#removes a card from the decklist
def remove(selectedCard):

    #if card is in decklist, remove 1 from quantity
    for card in decklist:
        if card.getName() == selectedCard:
            card.quantity -= 1

    #if card is at 0 quantity, delete the deckCard object and remove from decklist
    for card in decklist:
        if int(card.getQuantity()) == 0:
            decklist.remove(card)
            del card

#exports the decklist into a .txt file
def exportDecklist(file):
    f = open(file, 'w')
    for card in decklist:
        f.write(card.getQuantity() + " " + card.getName())
        f.write("\n")
    f.close()

#creates a card and adds it to the decklist
def createCard(name, quantity):
    try:
        card = deckCard(name, quantity)
        decklist.append(card)
    except:
        pass

#imports a .txt file and adds entries to decklist
def importDecklist(file):
    try:
        entry = []
        f = open(file, 'r')
        decklist.clear()
        for line in f:
            entry = line.strip("\n").split(" ")
            counter = 0
            for x in entry:
                if counter >= 2:
                    entry[1] = entry[1] + " " + entry[int(counter)] 
                counter += 1
            createCard(entry[1], int(entry[0]))
    except:
        pass
    f.close()
    return decklist

#searches the api with given constraints        
def search(cardname, cardcolor, cardcmc, cardtype, cardsubtype, cardrarity, cardset, cardtext, cardpower, cardtoughness):
    link = 'https://api.magicthegathering.io/v1/cards?pageSize=100'
    constraints = ""

    #add name to search if applicable
    if len(cardname) >= 1:
        constraints = constraints + "&name=" + cardname

    #add color choice to search if applicable
    if cardcolor != "":
        constraints = constraints + "&colors=" + cardcolor

    #add converted mana cost to search if applicable
    if cardcmc != "":
        constraints = constraints + "&cmc=" + cardcmc

    #add type to search if applicable
    if len(cardtype) >=1:
        constraints = constraints + "&types=" + cardtype

    #add subtype to search if applicable
    if len(cardsubtype) >=1:
        constraints = constraints + "&subtypes=" + cardsubtype

    #add rarity to search if applicable
    if cardrarity != "":
        constraints = constraints + "&rarity=" + cardrarity

    #add set to search if applicable
    if len(cardset) >= 1:
        constraints = constraints + "&set=" + cardset

    #add card text to search if applicable
    if len(cardtext) >= 1:
        constraints = constraints + "&text=" + cardtext

    #add power to search if applicable
    if cardpower != "":
        constraints = constraints + "&power=" + cardpower

    #add toughness to search if applicable
    if cardtoughness != "":
        constraints = constraints + "&toughness=" + cardtoughness

    #searches cards using the constraints, then adds them to the results list to be displayed
    response = requests.get(link + constraints)
    cards = response.json()
    int = 0
    results.clear()
    for entry in cards["cards"]:
        resultAdd = True
        cardname = (cards["cards"][int]['name'])
        try:
            cardimage = cards["cards"][int]['imageUrl'] 
            searchresult = result(cardname, cardimage)
            for x in results:
                if x.getName() == searchresult.getName():
                    resultAdd = False
            if resultAdd == True:
                results.append(searchresult)
        except:
            resultAdd = False
        int += 1

    if not results:
        failedResult = result("No cards match your search. Please try again.", "")
        results.append(failedResult)

    return results

#MTG Deckbuilder server
@app.route("/", methods=["POST", "GET"])
def deckBuilder():
    if request.method == "POST":
        if request.form["button"] == "Search":
            pagenum = 1
            cardname = request.form["cardname"]
            cardcolor = ""
            for x in range(1,6):
                varColor = "color" + str(x)
                try:
                    cardcolor = cardcolor + request.form[varColor] + ","
                except:
                    pass
            cardcmc = request.form["cmc"]
            cardtype = request.form["type"]
            cardsubtype = request.form["subtype"]
            cardrarity = request.form["rarity"]
            cardset = request.form["set"]
            cardtext = request.form["text"]
            cardpower = request.form["power"]
            cardtoughness = request.form["toughness"]
            search(cardname, cardcolor, cardcmc, cardtype, cardsubtype, cardrarity, cardset, cardtext, cardpower, cardtoughness)
            return redirect(url_for("deckBuilder", decklist=decklist, results=results))
        elif request.form["button"] == "Import Decklist":
            deckfile = request.form["deckfile"] + ".txt"
            try:
                importDecklist(deckfile)
                return redirect(url_for("deckBuilder", decklist=decklist, results=results))
            except:
                return redirect(url_for("deckBuilder", decklist=decklist, results=results))
        elif request.form["button"] == "Export Decklist":
            deckfile = request.form["deckfile"] + ".txt"
            if deckfile != ".txt":
                exportDecklist(deckfile)
                return redirect(url_for("deckBuilder", decklist=decklist, results=results))
            else:
                return redirect(url_for("deckBuilder", decklist=decklist, results=results))
    else:
        return render_template('deckbuilder.html', decklist=decklist, results=results)

#page for specific cards
@app.route("/<card>", methods=["POST","GET"])
def cardpage(card):
    pagecard=defaultResult
    for entry in results:
        if entry.getName() == card:
            pagecard=entry
    if request.method == "POST":
        if request.form["adder"] == "Add":
            deckcard = pagecard.getName()
            add(deckcard)
        elif request.form["adder"] == "Remove":
            deckcard = pagecard.getName()
            remove(deckcard)
    return render_template('card.html', decklist=decklist, results=results, card=card, pagecard=pagecard)

if __name__ == '__main__':
    app.run(debug=True)


