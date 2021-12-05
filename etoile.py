def escalier(n=6,s="*"):
    etoiles = 0
    x = s
    while etoiles<n:
        print (x)
        x = x + s
        etoiles = etoiles + 1
