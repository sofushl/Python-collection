dna="GCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGC"

dnarnaconv = {
    "A":"U",
    "T":"A",
    "C":"G",
    "G":"C"
}

kodontable = { 
 "UUU": "Fenylalanin", "CUU": "Leucin", 
 "AUU": "Isoleucin", "GUU": "Valin", 
 "UUC": "Fenylalanin", "CUC": "Leucin", 
 "AUC": "Isoleucin", "GUC": "Valin", 
 "UUA": "Leucin", "CUA": "Leucin", 
 "AUA": "Metionin", "GUA": "Valin", 
 "UUG": "Leucin", "CUG": "Leucin", 
 "AUG": "Metionin", "GUG": "Valin", 
 "UCU": "Serin", "CCU": "Prolin", 
 "ACU": "Treonin", "GCU": "Alanin", 
 "UCC": "Serin", "CCC": "Prolin", 
 "ACC": "Treonin", "GCC": "Alanin", 
 "UCA": "Serin", "CCA": "Prolin", 
 "ACA": "Treonin", "GCA": "Alanin", 
 "UCG": "Serin", "CCG": "Prolin", 
 "ACG": "Treonin", "GCG": "Alanin", 
 "UAU": "Tyrosin", "CAU": "Histidin", 
 "AAU": "Asparagin", "GAU": "Asparaginsyre", 
 "UAC": "Tyrosin", "CAC": "Histidin", 
 "AAC": "Asparagin", "GAC": "Asparaginsyre", 
 "UAA": "Stopp", "CAA": "Glutamin", 
 "AAA": "Lysin", "GAA": "Glutaminsyre", 
 "UAG": "Stopp", "CAG": "Glutamin", 
 "AAG": "Lysin", "GAG": "Glutaminsyre", 
 "UGU": "Cystein", "CGU": "Arginin", 
 "AGU": "Serin", "GGU": "Glycin", 
 "UGC": "Cystein", "CGC": "Arginin", 
 "AGC": "Serin", "GGC": "Glycin", 
 "UGA": "Stopp", "CGA": "Arginin", 
 "AGA": "Arginin", "GGA": "Glycin", 
 "UGG": "Tryptofan", "CGG": "Arginin", 
 "AGG": "Arginin", "GGG": "Glycin" 
}

rna = ""

for i in dna:
    i = i.capitalize()
    
    if i in dnarnaconv.keys():
        rna = rna + dnarnaconv[i]   
    else:
        print("Ugyldig input")

print(rna)

combo = ""
protein = ""
for i in rna:
    if not len(combo) == 3:
        combo = combo + i.capitalize()
    else:
        if combo in kodontable.keys():
            if len(protein) > 0:
                protein = protein+ ", " + kodontable[combo]
            else:
                protein = kodontable[combo]
        else:
            print("Ugyldig input")
        combo = ""

print(protein)