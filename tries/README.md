# 📌 Tries (Prefix Trees)

## 1. Basic Information

**Definition**: A tree-like data structure used to efficiently store and retrieve keys in a dataset of strings.

**Physical Representation**: A tree where each node represents a character. A path from the root to a node represents a prefix or a complete string.

**Key Analogy**: The contact list on your phone where you type "A", then "L", then "I", and it filters to "Alice".

**In Python:**  
- Typically implemented using nested dictionaries or custom `TrieNode` objects containing a dictionary of children and a boolean flag `is_end_of_word`.

**When to Use Tries:**  
- Autocomplete features
- Spell checkers
- Longest prefix matching
- Word search games (like Boggle)

---

## 2. Basic Operations

- **Insert**: Adding a word to the trie character by character.
- **Search**: Checking if a complete word exists in the trie.
- **Starts With**: Checking if there is any word in the trie that starts with a given prefix.

---

## 3. Complexity Stats
| Operation    | Time        | Space       |
| --------     | -------     | -------     |
| Insert       | $O(L)$      | $O(L)$      |
| Search       | $O(L)$      | $O(1)$      |
| Starts With  | $O(L)$      | $O(1)$      |

*Where $L$ is the length of the word.*

---
## 4. Common Problems

#### Pattern A: Trie Construction
- Example Problem: Implement Trie (Prefix Tree)
- Strategy: Use a nested dictionary or nodes with `is_end` flag.

#### Pattern B: Word Search II
- Example Problem: Find all words from a dictionary present in a 2D grid.
- Strategy: Build a Trie of the dictionary words, then do a DFS on the grid checking the Trie.
