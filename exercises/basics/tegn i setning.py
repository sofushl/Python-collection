t = list(input("Skriv en liten tekst eller setning: "))
s = str(input("Gi et tegn som skal optelles: "))
counter = 0

if s in t:
    for i in t:
        if i == s:
            counter += 1


print(f"Det er {counter} {s}'er i teksten din")
