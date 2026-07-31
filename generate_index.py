import os
import json

for racine, dossiers, fichiers in os.walk("."):
    pdfs = [
        f for f in fichiers
        if f.endswith(".pdf")
    ]

    if pdfs:
        with open(
            os.path.join(racine, "index.json"),
            "w",
            encoding="utf8"
        ) as fichier:
            json.dump(pdfs, fichier, indent=2, ensure_ascii=False)