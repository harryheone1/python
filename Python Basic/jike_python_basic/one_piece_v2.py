import re

# worse performance but to show power of function
def find_item(hero) :
    with open('data/one_piece_file.txt', encoding='utf-8') as f:
        text = f.read().replace('\n', '')
        return len(re.findall(hero, text))


# read charactor name
name_dict = {}
with open('data/one_piece_charactor_list.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)

print(name_sorted)