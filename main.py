from RVE_Generator import *
import matplotlib.pyplot as plt
import json


cwd = os.getcwd()
# All the data from deck.yaml is now in the following deck variable

deck = Deck( cwd + "/decks/RandomRVE.yaml" )

domain_RVE = RVE_definition(deck.doc["RVE"])

domain_fibres = Fibre_definition(deck.doc["Fibres"])

final_RVE = Place_Fibre(domain_RVE, domain_fibres)

plot = Plot(domain_RVE.origin, final_RVE.fibres )


with open(cwd+'\\'+deck.doc['Output']['folder']+'\\'+'fibres.json', 'w') as f:
    json.dump(final_RVE.fibres, f)
    
with open(cwd+'\\'+deck.doc['Output']['folder']+'\\'+'RVE.json', 'w') as f:
    json.dump(domain_RVE.origin, f)