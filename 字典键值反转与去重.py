def reverse_dict(original):
    reversed_dict={}
    for key,value in original.items():
        if value not in reversed_dict:
            reversed_dict[value]=[]
        reversed_dict[value].append(key)
    for k,v in reversed_dict.items():
        if len(v)==1:
            reversed_dict[k]=v[0]
    return str(reversed_dict)


if __name__ == "__main__":
    original_str = input().strip()
    original = eval(original_str)
    result = reverse_dict(original)
    print(result)