def merge_dicts(dict1, dict2):
    merged={}
    for key,value in dict1.items():
        merged[key]=value
    for key,value in dict2.items():
        if key in merged:
            merged[key]+=value
        else:
            merged[key]=value
    sorted_merged=dict(sorted(merged.items()))
    return str(sorted_merged)


if __name__ == "__main__":
    dict1_str = input().strip()
    dict2_str = input().strip()
    dict1 = eval(dict1_str)
    dict2 = eval(dict2_str)
    result = merge_dicts(dict1, dict2)
    print(result)