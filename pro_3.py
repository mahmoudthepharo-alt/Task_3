def input_set(set_number):
    s = set()
    
    print(f"Enter elements for set {set_number} (type -1 to finish):")
    
    while True:
        value = input("> ")
        
        if value == "-1":
            break
        
        if value.strip():
            s.add(value.strip())
    
    return s


def common_elements(set1, set2):
    return set1 & set2


set1 = input_set(1)
set2 = input_set(2)

result = common_elements(set1, set2)

print("Common elements:", result)