string = 'prashant'

# sequence assignment
a,b,c,d,e,f,g,h = string

print(a,h)

# tuple assignment
p,q = 2,4
print(q)

# positional
[n,m] = ['mc' , 'bc']
print(m)

print(string[:5])
print(string[5:8])

# Augmented
spams = 50
spams =+ 42
print(spams)

# Extended unpacking
seq = [1, 2, 3, 4]
k, *l = seq
print(k)
print(l)