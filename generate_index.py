import os
import json
import re

def numero_chapitre(nom):
    match = re.search(r"chap(\d+)", nom)
    if match:
        return int(match.group(1))
    return 9999


for racine, dossiers, fichiers in os.walk("."):

    dossiers[:] = [
        d for d in dossiers
        if d not in {".git", ".github"}
    ]

    pdfs = [
        f for f in fichiers
        if f.endswith(".pdf")
    ]

    if pdfs:
        pdfs.sort(key=numero_chapitre)

        with open(
            os.path.join(racine, "index.json"),
            "w",
            encoding="utf8"
        ) as fichier:
            json.dump(
                pdfs,
                fichier,
                indent=2,
                ensure_ascii=False
            )