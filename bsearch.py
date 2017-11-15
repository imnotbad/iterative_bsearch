dictionary_words = []

with open("english_words.txt", "r") as words:
    for word in words:
        dictionary_words.append(word.lower().strip())

def bsearch(search_value, array):
    mid_point = 0
    start = 0
    end = len(array)-1

    while start <= end:
        mid_point = (start + end)//2
        if array[mid_point] == search_value:
            break
        elif array[mid_point] < search_value:
            start = mid_point+1
        elif array[mid_point] > search_value:
            end = mid_point-1
    
    return mid_point

print(bsearch("dog", dictionary_words))
