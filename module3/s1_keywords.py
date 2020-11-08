"""Testing keyword extraction with YAKE"""

import os
import yake

ignored = set(["conseil communal", "conseil général"])

kw_extractor = yake.KeywordExtractor(lan="fr", top=20)
data_path = "D:/DOCUMENTS/data/txt/"
files = os.listdir(data_path)
for f in sorted(files):
    if f.startswith("Bxl_1848_"):
        text = open(data_path + f, encoding='utf-8', errors='ignore').read()
        keywords = kw_extractor.extract_keywords(text)
        kept = []
        for score, kw in keywords:
            words = kw.split()
            if len(words) > 1 and kw not in ignored: # only bigrams and more
                kept.append(kw)
        print(f"{f} mentions these keywords: {', '.join(kept)}...")
