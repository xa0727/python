def count_words(text):
    word_counts={}
    words=text.split()
    # print(words)
    for word in words:
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1
    sorted_words=sorted(word_counts.items(),key=lambda x:(-x[1],x[0]))#负号代表降序排序
    # 如果第一个参数相等，按照第二个参数排
    return sorted_words



if __name__=='__main__':
    text=input().strip()
    result=count_words(text)
    for word,freq in result:
        print(f"{word}:{freq}")