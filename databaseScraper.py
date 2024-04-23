import requests # type: ignore
from bs4 import BeautifulSoup, NavigableString
import csv # type: ignore

#url for pokemon database
pokeURL = "https://pokemondb.net/pokedex/all"

pokeData = requests.get(pokeURL)

pokeSoup = BeautifulSoup(pokeData.content, "html.parser")

#id pokedex
#elements tbody > tr each tr is a different pokemon 
#tr > td each td is a datapoint
#tr is comprised of newlines ('\n') and tds, you gotta skip the newlines
#idk
#print(soup.find("tbody"))

pokeTable = pokeSoup.find("tbody")

#print(pokeTable.contents[23])
#looks like the order is as follows:
pokeStats = ["Number", "Name", "Type", "Total", "HP", 
             "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]

test = []
typeCheck = type(NavigableString("test"))

#pseudo code
#for each element in the table
#check if it is a navigable string
#if yes pass, else iterate through the element as an iterable element
#check if the iterable contains navigable strings
#if yes, pass, else take the value of the element and append it to a new row
#check if the name already exists in the new list (TBD pokedex)
#if the name exists, the next occurence is an alt form, append the alt name
#add the new row to the new list 

#print(type(pokeTable.contents[0]))



with open("pokedex.csv", "w", newline='', encoding="utf-8") as csvfile:
    pokeWriter = csv.writer(csvfile)

    for row in pokeTable:
        newRow = []
        if type(row) == typeCheck:
            pass
        else:
            for stat in row:
                if type(stat) == typeCheck:
                    pass
                else:
                    newData = stat.string
                    if stat.string == None:
                        if stat.a:
                            newData = stat.a.string
                            if stat.small:
                                if newData in stat.small.string:
                                    newData = stat.small.string
                                else:
                                    newData += " "+stat.small.string
                        if stat.span:
                            newData = stat.span.string
                            if stat.small:
                                if newData in stat.small.string:
                                    newData = stat.small.string
                                else:
                                    newData += " "+stat.small.string
                    newRow.append(newData)
        pokeWriter.writerow(newRow)
