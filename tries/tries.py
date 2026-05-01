"""
tries.py

A collection of common Trie patterns used in interviews and LeetCode,
implemented as small, focused classes and functions.
"""

# ---------------------------------------------------------
# Pattern A: Trie Construction
# ---------------------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Standard Prefix Tree.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time: O(L), Space: O(L)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        Time: O(L), Space: O(1)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word that starts with the prefix.
        Time: O(L), Space: O(1)
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))      # True
    print(trie.search("app"))        # False
    print(trie.starts_with("app"))   # True
    trie.insert("app")
    print(trie.search("app"))        # True
