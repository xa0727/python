def merge_grades(dict_a, dict_b):
    merged={}
    for name,score in dict_a.items():
        merged[name]=score
    for name,score in dict_b.items():
        if name in merged:
            if score>merged[name]:
                merged[name]=score
        else:
            merged[name]=score
    sorted_merged=sorted(merged.items())
    # print(merged.items())
    # print(sorted_merged)
    return str(dict(sorted_merged))


if __name__ == "__main__":
    dict_a_str = input().strip()
    dict_b_str = input().strip()
    dict_a = eval(dict_a_str)
    dict_b = eval(dict_b_str)
    result = merge_grades(dict_a, dict_b)
    print(result)