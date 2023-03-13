'''
Created on 13 Mar 2023

@author: julianporter
'''
import re

def getCards(prefix='hw'):
    cards=[]
    with open('/proc/asound/cards','r',encoding='utf-8') as f:
        for line in f:
            #print(f'###{line}###')
            m=re.match(r'\s*(\d+)\s+\[(\S+)\s*\]',line)
            if m is not None:
                dev, card = m.groups()
                cards.append(f'{prefix}:CARD={card},DEV={dev}')
    return cards

cards=getCards()   
for card in cards : print(card)
