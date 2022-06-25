import periodicTable
def main():
    print("""•• Hello there, welcome to the PT Google.
    Using this software, you will be able to:
    --> Find the details of an element using the element name -- Enter 'element name'
    --> Find the details of an element using its atomic number -- Enter 'atomic number'
    --> Find the details of an element using its symbol -- Enter 'symbol'
    --> To exit -- Enter 'exit'.checking
    Enjoy!! ••""")
    while True:
        wt = input("-->  ")
        if wt.lower() == "element name":
            name = input("What's the name of the element? ")
            ElementName(name.capitalize())
        elif wt.lower() == "atomic number":
            atomicNo = input("What is the atomic number of the element? ")
            AtomicNumber(atomicNo)
        elif wt.lower() == "symbol":
            symbolgiven = input("What's the symbol of the element you know? ")
            symbol(symbolgiven.capitalize())
        elif wt.lower() == "exit":
            break
def AtomicNumber(number):
        number = str(number)
        for element in periodicTable.elements:
            if element['Atomic Number']==number:
                print(element["Element Name"],"or","'"+element["Symbol"]+"'"
                ,"of atomic number", element["Atomic Number"], 
                "has atomic mass", element["Atomic Mass"], end=" .\n")
def symbol(sy):
    for element in periodicTable.elements:
        if element["Symbol"]==sy:
            print(element["Element Name"],"or","'"+element["Symbol"]+"'",
            "has atomic number",element["Atomic Number"], "and atomic mass"
            ,element["Atomic Mass"])
def ElementName(nm):
    for element in periodicTable.elements:
        if element["Element Name"]==nm:
            print(element["Element Name"],"or","'"+element["Symbol"]+"'",
            "has atomic number",element["Atomic Number"], "and atomic mass"
            ,element["Atomic Mass"])

main()