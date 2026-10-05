list_a = ["HTML", "CSS", "JS"]

for each in list_a:
    if each.startswith("H"):
        list_a.remove(each)

print(list_a)