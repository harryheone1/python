# read all character which should be searched
f1 = open('data/one_piece_charactor_list.txt', 'r')
character_list = f1.read().split('|')
character_num = {character: 0 for character in character_list}
f1.close()


f2 = open('data/one_piece_file.txt', encoding='utf-8')
# put all text into 1 line
all_text = f2.read().replace('\n', '')
print(all_text)
for word in all_text.split():
    if word in character_list:
        character_num[word] += 1

print(character_num)
f2.close()

def read_file(path):
    result = open(path, 'r').read()
    return result

print(read_file('data/one_piece_charactor_list.txt').split('|'))

