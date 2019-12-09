from random import randrange

BASIC_NEWS_REPORT = """\
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

RESISTANCE_DESTABILISATION="""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} tout est optimal.

```diff
+ Les oiseaux chantent,
+ Les enfants jouent,
- Certains mentent,
- Gare à vous,

+ Louée soit notre présidente,
+ Elle est là pour nous,
- À tous les troubles-fête,
- Nos chars foncent sur vous!
```

À demain peuple adoré.
"""

RESISTANCE_DESTABILISATION2="""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} notre pays est resplendissant !

```diff
+ Doux peuple adoré,
+ Ne te laisse pas détourner,
+ Du droit chemin injustement décrié,
+ Par l'opposition dissidante,
+ Contre la douce saveur enivrante,
+ De notre adorée Présidente.
```

À demain peuple aimé.
"""

THANKS_FROM_PRESIDENT="""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} notre adorée Présidente nous accorde quelques paroles !

"Bonjour mes chers frères et soeurs, vous faites du bon boulot ! Votre travail paie !"

Merci adorée Présidente pour ces mots motivants !

À demain peuple adoré.
"""

PARTIELS_S7="""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} s'achève un long week-end pour nos jolies têtes blondes à la FAC !

Contemplez notre jeunesse se hisser au rang de futurs citoyens durant leur partiels !
Que la chance soit avec vous ! Nul doute que vous réussirez à rendre notre adorée Présidente fière !
N'oubliez pas, un état puissant est un état avec une jeunesse dynamique et motivée !

À demain peuple adoré.
Reposez-vous, prochains diplômés.
"""

FIN_PARTIELS_S7="""\
```fix
Vox Populi - La parole du peuple
```
Aujourd'hui {date} s'achève une dure semaine pour nos jolies têtes blondes à la FAC !

La nation espère que vos partiels ont étés des plus fructueux !
Reposez-vous maintenant, prochains diplômés.

À demain peuple adoré.
"""

ALL_NEWS_REPORT = [BASIC_NEWS_REPORT, RESISTANCE_DESTABILISATION, THANKS_FROM_PRESIDENT, RESISTANCE_DESTABILISATION2]

def get_random_news_report():
    return ALL_NEWS_REPORT[randrange(len(ALL_NEWS_REPORT))]
