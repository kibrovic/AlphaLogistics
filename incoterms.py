#!/usr/bin/env python3

from pick import pick

incoterms = {
    'Svi vidovi saobraćaja': {
        'Prodavač ugovara glavni prijevoz [NE]': {
            'Kupac plaća utovar robe [DA]': {
                'incoterm': 'EXW'
            },
            'Kupac plaća utovar robe [NE]': {
                'incoterm': 'FCA'
                }
        },
        'Prodavač ugovara glavni prijevoz [DA]': {
            'Prodavač snosi rizik prijevoza [NE]': {
                'Prodavač osigurava u ime kupca [NE]': {
                    'incoterm': 'CPT'
                },
                'Prodavač osigurava u ime kupca [DA]': {
                    'incoterm': 'CIP'
                }
            },
            'Prodavač snosi rizik prijevoza [DA]': {
                'Isporučeno na terminal [DA]': {
                    'incoterm': 'DAT'
                },
                'Isporučeno na terminal [NE]': {
                    'Kupac snosi troškove uvoza [DA]': {
                        'incoterm': 'DAP'
                    },
                    'Kupac snosi troškove uvoza [NE]': {
                        'incoterm': 'DDP'
                    }
                }
            }
        }
    },
    'Transport vodenim saobraćajem': {
        'Prodavač ugovara glavni prijevoz [NE]': {
            'Prodavač isporučuje uz bok broda [DA]': {
                'incoterm': 'FAS'
            },
            'Prodavač isporučuje uz bok broda [NE]': {
                'incoterm': 'FOB'
            }
        },
        'Prodavač ugovara glavni prijevoz [DA]': {
            'Prodavač osigurava u ime kupca [NE]': {
                'incoterm': 'CFR'
            },
            'Prodavač osigurava u ime kupca [DA]': {
                'incoterm': 'CIF'
            }
        }
    }
}

incoterms_opis = {
    'EXW': """Prodavač dostavlja na odredište\nKupac plaća troškove uvoza i izvoza""",
    'FCA': """Prodavač dostavlja na odredište\nProdavač isporučuje robu u naznačenom mjestu\nProdavač plaća troškove izvoza a kupac uvoza""",
    'CPT': """Prodavač dostavlja na odredište\nProdavač plaća troškove izvoza a kupac uvoza""",
    'CIP': """Prodavač dostavlja na odredište\nProdavač plaća troškove izvoza a kupac uvoza""",
    'DAT': """Prodavač dostavlja na odredište\nProdavač plaća troškove izvoza a kupac uvoza""",
    'DAP': """Prodavač dostavlja na odredište\nKupac plaća istovar robe\nProdavač plaća troškove izvoza a kupac uvoza""",
    'DDP': """Prodavač dostavlja na odredište\nKupac plaća istovar robe\nProdavač plaća troškove uvoza i izvoza""",
    'FAS': """Transport vodenim saobraćajem\nKupac ugovara glavni prijevoz\nProdavač plaća troškove izvoza a kupac uvoza""",
    'FOB': """Transport vodenim saobraćajem\nKupac ugovara glavni prijevoz\nProdavač isporučuje na palubu broda\nProdavač plaća troškove izvoza a kupac uvoza""",
    'CFR': """Transport vodenim saobraćajem\nKupac snosi rizik transporta\nProdavač isporučuje na palubi broda\nProdavač plaća troškove izvoza a kupac uvoza""",
    'CIF': """Transport vodenim saobraćajem\nKupac snosi rizik transporta\nProdavač plaća troškove izvoza a kupac uvoza"""
}

def get_incoterm():
    incoterm = ''
    level = incoterms
    stop = 'no'
    while stop != 'yes':
        lista = [key for key in level]
        option = pick(lista)
        if option[0] == 'incoterm':
            incoterm = level['incoterm']
            break
        level = level[option[0]]
        #stop = input('Stop? [yes/no]')

    print('\033[1m' + incoterm + '\033[0m')
    print(incoterms_opis[incoterm])
    return incoterm, incoterms_opis[incoterm]
