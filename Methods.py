def paliPrime(n):
    fmt = '%-5d'
    if n >= 1:
        print (fmt % 2)
    count = 2
    i = 3
    while count <= n:
        paliPrime = True
        if str(i) == str(i)[::-1]:
            for a in range(2, i):
                if i % a == 0:
                    paliPrime = False
                    break
            if paliPrime:
                print (fmt % i)
                if count % 10 == 0:
                    print('i')
                count += 1
        i += 2
    
    if count % 10 != 1:
        print("j")
