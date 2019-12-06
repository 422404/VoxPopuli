from datetime import datetime

def random_propaganda():
    date = datetime.now().strftime("%d/%m/%Y")
    return f"""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} tout va bien.

- Le peuple est **heureux**
- Le taux de chomâge est au plus **bas**
- La bourse est **fructueuse**
- La météo est **bonne**
- Le commerce ce porte **admirablement bien**
- Notre nation est **forte**
- Notre adorée Présidente est **fière**

Merci à notre adorée Présidente de nous accorder tant de bonheur en ces temps troubles.
Merci au gouvernement d'être juste et équitable.
Merci au peuple d'exister.

```diff
- À tous les fauteurs de trouble: attention.
```

Bonne journée peuple cher.
À demain.
"""