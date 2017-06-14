import itertools
import sys
print(sys.version)

# Taken from pyethrecover
combinations=[
    ('hello', 'bonjour', 'hola'),
    ('', 'mister', 'president'),
    #('brother', ),
    ('smith', 'jefferson')
]

pwds=[]
def generate_all(el, tr):
    if el:
        for j in range(len(el[0])):
            for w in generate_all(el[1:], tr + el[0][j]):
                yield w
    else:
        yield tr

pwds = itertools.chain(pwds, generate_all(combinations,''))
pwds_l = list(pwds)
n_pws = len(pwds_l)

print('Number of passwords to test {0} '.format(n_pws))

i=1
found = 0
for l in pwds_l:    
    print "%s" % l

