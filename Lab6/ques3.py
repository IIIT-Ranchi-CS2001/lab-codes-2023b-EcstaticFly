def my_max(*args):
    if not args:
        raise ValueError("empty sequence")
    max_value = args[0]
    for value in args[1:]:
        if value > max_value:
            max_value = value
    return max_value
container_type = input("Enter the container type (list/set/tuple): ").strip().lower()
values = input("Enter the elements separated by space: ").split()

if container_type == "list":
    container = [int(x) for x in values]
elif container_type == "set":
    container = {int(x) for x in values}
elif container_type == "tuple":
    container = tuple(int(x) for x in values)
else:
    raise ValueError("Invalid container type. Choose from 'list', 'set', or 'tuple'.")

print(f"Maximum value in the {container_type} is: {my_max(*container)}")