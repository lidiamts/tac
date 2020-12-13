"""Filter out stopwords for word cloud"""

import sys
import nltk
try:
    from nltk.corpus import stopwords
except LookupError:
    nltk.download('stopwords')
    from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "conseil", "aucun", "doivent",
       "nouvelle", "mois", "sieur", "très", "déja", "quatre", "cause", "agit", "grand", "également", "avant", "part", "donné",
       "car", "quant", "parce", "alors", "moyen", "faite", "Leurs", "seulement", "dernier", "laquelle", "aucune", "aujourd'hui",
       "ans", "nombre", "première", "plusieurs", "suite", "celles", "elles", "quand", "jour", "établi", "établi", "peu",
       "ancien", "proposé", "peuvent", "seule", "toute", "beaucoup"]
sw = set(sw)


def filtering(year):
    path = f"{year}.txt"
    output = open(f"{year}_keywords.txt", "w")

    with open(path) as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)


if __name__ == '__main__':
    data_path = sys.argv[1]
    filtering(year)
