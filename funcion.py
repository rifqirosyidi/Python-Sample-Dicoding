# Funcion Basic
def changeme(list_val):
    list_val.append([1, 2, 3, 4])
    print("Nilai dalam fungsi: ", list_val)
    return


mylist = [10, 20, 30]
changeme(mylist)

print("Nilai luar fungsi: ", mylist)


def changeme():
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4];  # This would assign new reference in mylist
    print("Nilai di dalam fungsi: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme()
print("Nilai di luar fungsi: ", mylist)


# Another Function
def printinfo(name, umur):
    print("Name: ", name)
    print("Age :", umur)
    return


printinfo("Rifqi", 25)


# Function with default arguments
def printinfo(name, umur=20):
    print("Name: ", name)
    print("Age :", umur)
    return


printinfo(name="Rifqi")


# Implementasi Variable Length *(star) parameter *var_args_tuple
def printinfo(arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(10)
printinfo(10, 60, 79)
