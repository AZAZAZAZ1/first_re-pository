students={
    "Alice":["ID0001",26,"A"],
    "Bob":["ID0002",27,"B"],
    "Claire":["ID0003",17,"C"],
    "Dan":["ID0004",21,"D"],
    "Emma":["ID0005",22,"E"],
    }
# to get Claire data:

print(students["Claire"])

#To get Claire (ID):
print(students["Claire"][0])

#----------------------------------------------------------------

students={
    "Alice":{"ID":"ID0001","Age":26,"Grade":"A"},
    "Bob":{"ID":"ID0002","Age":27,"Grade":"B"},
    "Claire":{"ID":"ID0003","Age":17,"Grade":"C"},
    "Dan":{"ID":"ID0004","Age":21,"Grade":"D"},
    "Emma":{"ID":"ID0005","Age":22,"Grade":"E"},
    }
# to get Dan grade:
print(students["Dan"]["Age"])
print(students["Emma"]["ID"], students["Emma"]["Grade"])

# note the below commands will not work because the above values in between {} are not a list [], so you cannot index them
print(students["Dan"][2])
print(students["Emma"][0], students["Emma"][4])
