def fatorial(x):
    if x <= 1:
        return 1
    if x > 1:
        return fatorial(x - 1) * x


#  print(fatorial(6))