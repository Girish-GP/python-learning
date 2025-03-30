# write a function to remove a given word from the list and also strip it from other words

list = ["Grapes","apes","tapes","es"]

word = "es"
def remove_from_list(l,w):
    updated = []
    for item in l:
        if item != w:
            updated.append(item.strip(w))
        else:
            l.remove(w)
    return updated

filtered = remove_from_list(list,word)
print(filtered)