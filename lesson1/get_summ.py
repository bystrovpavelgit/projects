def get_summ(one, two, delimiter="&"):
    """ function get summ of one and two"""
    return str(one) + delimiter + str(two)


lp = get_summ("Learn", "python")
print(lp)
print(lp.upper())

