def all_thing_is_obj(object: any) -> int:
	obj_type = type(object)
	types_list = {
		list : "List",
		tuple : "Tuple",
		set : "Set",
		dict : "Dict",
		str : "String",
	}

	type_name = types_list.get(obj_type, "Type not found")
	if (type_name == "Type not found"):
		print(f"{type_name}")
		return 42
	
	if (obj_type == str) :
		print(f"{object} is in the kitchen : {obj_type}")
	else :
		print(f"{types_list[obj_type]} : {obj_type}")
	return 42