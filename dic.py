dict1 = {"name": "MINHAJ", "age": "mai nhi batunga","ghar": "bhut durr hai"}
print(type(dict1))

print(dict1)
print(dict1["name"])
marks = {"amorkit" : 56, "minhaj" : 89, "bhaku" : 78, "kalu": 85}
print(marks)
print(marks["kalu"])
marks["prichunda"] = 25  # this is a way of add data of any one in ur existing dict
print(marks)

print(marks.get("chumpa"))
# (.get) help krta hai error se bchane m .. agr wo item nhi h dict mai to none execute dega ...dekh bhai tere dict mai hai hi nhi chumpa to nhi ayega ..
print(marks.keys())
print(marks.items())
print(marks.values())
