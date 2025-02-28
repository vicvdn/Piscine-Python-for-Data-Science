ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# modify a list (changeable, duplicates)
ft_list[1] = "World!"

# modify a tuple (unchangeable, duplicates)
ft_tuple = ("Hello", "France!")

# modify a set (no access through indexes, no duplicates, but mutable)
ft_set.remove("tutu!")
ft_set.add("Paris!")

# modify a dictionnary (keys immutable and unique)
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)