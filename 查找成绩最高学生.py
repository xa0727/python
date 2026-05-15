def find_top_students(n, records):
    max_score=max(score for name,score in records)
    top_students=[name for name,score in records if score==max_score]
    return top_students




if __name__ == "__main__":
    n = int(input().strip())
    records = []
    for _ in range(n):
        name, score = input().strip().split()
        records.append((name, int(score)))
    result = find_top_students(n, records)
    print(result)