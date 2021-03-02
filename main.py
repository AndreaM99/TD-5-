# ---- #
premier, *derniers = 1, 2, 3

print(derniers)  # [2, 3]
print(*derniers) # 2 3

# ---- #
def somme2(z, y):
   return z + y

def somme3(x,y,z):
  return x + y + z

def sommeliste(maliste):
  return sum(maliste)

sommeliste([1,2,3]) # 6
print(sommeliste([1,2,3]))

def somme_etoile(*meschiffres):
  return sum(meschiffres)

somme_etoile(1,2,3) # 6
print(somme_etoile(1,2,3))

# -- 1) -- #
def puiss(x,liste):
  z = [i**x for i in liste]
  return z

puiss(2,[1,2,3])
print(puiss(2,[1,2,3]))

assert puiss(2, [4,5]) == [16, 25] # assert stop la fonction si c'est vérifier 

# -- 2) -- #
