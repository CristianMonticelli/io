#la parola decifrata e lunica comprensibile
parola_nascosta = "FKH EHOOR VLVWHPL H UHWL"
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
spostamento = 1
chiave = 0
for i in range(26):
    parola = ""
    for l in parola_nascosta:
        for a in alfabeto:
            if l == a:
                if alfabeto.index(a)+spostamento < len(alfabeto):
                    chiave = spostamento
                    parola += alfabeto[alfabeto.index(a)+chiave]
                    
                else:
                    chiave = spostamento-26
                    parola += alfabeto[alfabeto.index(a)+chiave]
                    
        if l == " ":
            parola+=" "
    spostamento+=1
    print(f"la parola: {parola} | chiave: {chiave*-1}")



