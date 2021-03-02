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
puissance, *nombres = 2, 1, 2, 3
print("puissance = ",puissance)
print("nombres = ", nombres)
print("*nombres = ", *nombres)

#/!\ VERSION D'ESSAI /!\#

def puiss_etoile(puissance, *nombres):
  print("----")
  print(f" puissance : {puissance}")
  print(f" nombres : {nombres}")
  print("----")
  return [i**puissance for i in nombres]

print(f" puissance etoile : {puiss_etoile(2,1,2,3)}")

assert puiss_etoile(2,4,5) == [16, 25]

#/!\ VRAI VERSION /!\#

def puiss_etoileV2(*nombres):
  print("----")
  print(f" valeurs: {nombres}")
  pui, *derniers = nombres
  print(f" pui : {pui}")
  print(f" nombres : {derniers}")
  print("----")
  return [i**pui for i in derniers]

print(f" puissance etoile V2 : {puiss_etoileV2(2,1,2,3)}")

assert puiss_etoileV2(2,4,5) == [16, 25]

# -- 3) -- #
b = 1,2
a = 1, 2, 3
print(a)
*a,c = 0, *b
print(*a,c)
# z = 0, *b, 8, (*"azerty",58)

#print(f" somme3 : {somme3(*a)}") # ne marche pas car on a que deux éléments 
#print(" somme2 : ", somme2(*a)) # marche car on a 2 éléments dans a