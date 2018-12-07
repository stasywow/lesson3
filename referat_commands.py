with open('referat.txt', 'r') as text:
    cont = text.read()
        print(cont)
len(cont)
cont.count(' ') + cont.count('\n') - 1
cont_wow = cont.replace('.','!')
with open('referat2.txt', 'w') as ref:
    ref.write(cont_wow)
