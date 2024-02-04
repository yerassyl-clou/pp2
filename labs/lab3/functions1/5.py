def permutations(elements):
    if len(elements) <= 1:
        return [elements]
    
    result = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        
        for x in permutations(remaining_elements):
            result.append([current_element] + x)
    
    return result



lst = [1, 2, 3, 4]
print(permutations(lst))
