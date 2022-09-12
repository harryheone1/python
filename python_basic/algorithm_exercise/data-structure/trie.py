class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie_node = self.trie_root
        for idx, c in enumerate(word):
            if not trie_node.children[ord(c) - ord('a')]:
                trie_node.children[ord(c) - ord('a')] = TrieNode()
            trie_node = trie_node.children[ord(c) - ord('a')]
             # change is_word
            if idx == len(word) - 1:
                trie_node.is_word = True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie_node = self.trie_root
        for c in prefix:
            if not trie_node.children[ord(c) - ord('a')]:
                return False
            trie_node = trie_node.children[ord(c) - ord('a')]
        return True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie_node = self.trie_root
        for c in word:
            if not trie_node.children[ord(c) - ord('a')]:
                return False
            trie_node = trie_node.children[ord(c) - ord('a')]

        return trie_node.is_word


class TrieNode:

    def __init__(self, is_word, children):
        self.is_word = [None] * 26
        self.children = children

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
print(obj.startsWith('a'))