class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_string(self, word: str) -> None:
        nxt = self.root
        for i in word:
            nxt = nxt.add_char(i)
            nxt.freq += 1
        nxt.end_of_key = True

    def search_string(self, string: str) -> bool:
        nxt2 = self.root
        for i in string:
            if i not in nxt2.nodes:
                return False
            nxt2 = nxt2.nodes[i]
        return nxt2.end_of_key

    def count_prefix(self, prefix: str) -> int:
        nxt = self.root
        for i in prefix:
            if i not in nxt.nodes:
                return 0
            nxt = nxt.nodes[i]
        return nxt.freq


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.end_of_key = False
        self.freq = 0

    def add_char(self, c: chr):
        if c not in self.nodes:
            self.nodes[c] = TrieNode()
        return self.nodes[c]
    