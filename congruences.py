import sys
sys.set_int_max_str_digits(8000)

def congruences():
    print("-------------------------------")
    print("CONGRUENCES - PUISSANCE")
    print("-------------------------------")
    dividende = input("DIVIDENDE: ")
    nbr = int(dividende.split("**")[0])
    p = int(dividende.split("**")[1])
    modulo = int(input("MODULO: "))

    # Recherche de la congruence de NBR
    print(f"On recherche le reste de {nbr} | {modulo}")
    congr = nbr%modulo
    div = nbr//modulo
    print(f"On a {nbr} = {modulo} x {div} + {congr}")
    if congr == 0:
        print(f"=> {nbr} ≡ {congr} [{modulo}]")
        print(f"=> {nbr}**{p} ≡ {congr}**{p} [{modulo}]")
        print(f"=> {nbr}**{p} ≡ {congr} [{modulo}]")
        return

    # Recherche de la puissance pour laquelle : congr**n ≡ 1 [modulo]
    n = 1
    while congr**n%modulo != 1:
        n += 1
    print("On a n ∈ ℕ")
    print(f"On cherche la puissance pour laquelle {congr}**n ≡ 1 [{modulo}]")
    print(f"On a donc n = {n}")
    
    # Recherche du reste de la congruence de la puissance p
    pdiv = p//n
    prest = p%n
    print(f"On décompose la puissance, soit {p}")
    print(f"On a donc {p} = {n} x {pdiv} + {prest}")

    # On relie les deux
    print("On rassemble alors :")
    print(f"{dividende} ≡ {congr}**({n}x{pdiv}+{prest})")
    print(f"≡ ({congr}**{n})**{pdiv} x {congr}**{prest}")
    print(f"≡ {congr}**{prest} ≡ {congr**prest} ≡ {(congr**prest)%modulo} [{modulo}]")