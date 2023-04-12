import sys
sys.set_int_max_str_digits(8000)

def reste_pow():
    print("-------------------------------")
    print("TROUVER LE RESTE - PUISSANCE")
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

def reste_pow_n():
    print("-------------------------------")
    print("TROUVER RESTE AVEC N - PUISSANCE")
    print("-------------------------------")
    dividende = input("DIVIDENDE: ")
    modulo = int(input("MODULO: "))
    nbr = int(dividende.split("**")[0])
    p = dividende.split("**")[1]

    print(f"On recherche le plus petit n ∈ ℕ tel que {nbr}**n ≡ 1 [{modulo}]")
    n = 2
    while (nbr**n)%modulo != 1:
        n += 1
    print(f"On a donc n = {n}")
    print(f"On fait alors un tableau des reste de n=0 à n={n-1}")
    # On fait le tableau de 0 à n-1
    tab = []
    for i in range(n):
        nb = str((nbr**i)%modulo)
        if not nb in tab:
            tab.append(nb)
    print("On a alors les reste suivants: ")
    print(f"{p}  {' ' * len(p)}:", " ".join(list(map(lambda i: "{:<3}".format(i), [i for i in range(n)]))))
    print(f"{nbr}**{p}:", " ".join(list(map(lambda r: "{:<3}".format(r), tab))))
