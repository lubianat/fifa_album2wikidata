import pandas as pd
import os
from pathlib import Path

HERE = Path(__file__).parent.resolve()

spreadsheet_url = (
    "https://docs.google.com/spreadsheets/d/e/"
    "2PACX-1vQ0qXOmOq93-jvcxk-Xx4MwfZOVdJ0Ye1ZqZHLI0f"
    "-yoOM08NCcSXBaOUfQ2x7eKObZTuBSIlCSEEyF"
    "/pub?output=xlsx"
)
os.system(f"wget -O data/stickers.xlsx {spreadsheet_url} ")


groups = "A B C D E F G H".split()

statements = ""
for group in groups:
    stickers = pd.read_excel("data/stickers.xlsx", sheet_name=group)

    for i, row in stickers.iterrows():
        s = "Q113646122"  # FIFA Sticker Album 2022
        p = "|P180|"
        o = row["id"]
        qp1 = "|P1545|"
        qo1 = '"' + row["code"] + '"'
        rp1 = "|S854|"
        ro1 = s

        # Add depicts to the album
        statements += s + p + o + qp1 + qo1 + rp1 + ro1 + "\n"

        s2 = row["id"]
        p2 = "|P1532|"
        o2 = row["country for sports"]
        # Add country for sports to the players
        statements += o + p2 + o2 + rp1 + ro1 + "\n"

HERE.parent.joinpath("data/depicts_for_players.qs").write_text(
    statements, encoding="UTF-8"
)
