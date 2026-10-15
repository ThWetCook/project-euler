totaal = 0
with open("numbers.txt", "r", encoding="utf-8") as f:
    for lijn in f:
        woord = lijn.strip()
        totaal += len(woord.replace(" ", "").replace("-", ""))
        print(totaal)