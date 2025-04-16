import numpy as np

def calculate(list):
    #katsotaan että käyttäjä on syöttänyt 9 numeroa
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #Muutetaan 3x3 matriisiksi
    matrix = np.array(list).reshape(3, 3)

    calculations = {
        #Keskiarvon määrittäminena
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        #Varianssin määrittäminen
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        #keskihajonnan määrittäminen
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        #Maksimin määrittäminen
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        #Minimind määrittäminen
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        #Summan määrittäminen
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }



    #Palauttaa arvot
    return calculations
