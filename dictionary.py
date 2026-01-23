# dictionary

dic={"a":1,"b":2,"c":3}

print(dic.keys())  # prints all keys in the dictionary
print(dic.values())  # prints all values in the dictionary
print(dic.items())  # prints all key-value pairs in the dictionary
dic["d"]=4  # adding a new key-value pair
print(dic)
del dic["b"]  # deleting a key-value pair
print(dic)

print(dic.get("a"))  # getting the value for key "a"
print(dic.get("z", "Not Found"))  # getting the value for key "z" with default value

print(dic.update({"e":5, "f":6}))  # updating the dictionary with new key-value pairs
print(dic)

# iterating through a dictionary
for key in dic:
    print(f"Key: {key}, Value: {dic[key]}")
for key, value in dic.items():
    print(f"Key: {key}, Value: {value}")

# dictionary functions
"""
get - returns the value for a key if it exists, else returns a default value dic.get(key, default)
pop - removes a key and returns its value dic.pop(key)
popitem - removes and returns an arbitrary key-value pair dic.popitem()
clear - removes all key-value pairs dic.clear()
update - updates the dictionary with key-value pairs from another dictionary dic.update(other_dic)
setdefault - returns the value for a key if it exists, else sets it to a default value and returns that dic.setdefault(key, default)
"""

