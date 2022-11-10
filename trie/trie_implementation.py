from typing import Dict


class Trie:
    root: "Trie.TrieNode"

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for letter in word:
            if letter not in current_node.childs:
                current_node.childs[letter] = self.TrieNode()
            current_node = current_node.childs[letter]

        current_node.isEnd = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for letter in word:
            if letter not in current_node.childs:
                return False
            current_node = current_node.childs[letter]

        return current_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for letter in prefix:
            if letter not in current_node.childs:
                return False
            current_node = current_node.childs[letter]

        return True

    class TrieNode:
        childs: Dict[str, "Trie.TrieNode"]
        isEnd: bool

        def __init__(self):
            self.childs = {}
            self.isEnd = False
