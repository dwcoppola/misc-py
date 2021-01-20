def myfunc(n):
  return lambda v : v + n

appendlastname = myfunc(" Coppola")
appendmiddlename = myfunc(" William")

print(appendlastname(appendmiddlename("David")))
print(appendlastname("Stacey"))
print(appendlastname("Chuck"))
print(appendlastname("Nora"))
print(appendlastname("Talia"))