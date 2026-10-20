class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str, node: TrieNode = None) -> bool:
        if node is not None:
            cur = node
        else:
            cur = self.root
        if len(word) == 0:
            return cur.endOfWord
        # print(f"\n*** Searching {word}, in node: {cur.children.keys()}")

        for i, c in enumerate(word):
            # if it's wildcard, search everychild for the trimmed word and check if I found it  
            if c == '.':
                for child in cur.children.values():
                    if self.search(word[i+1:], child):
                        return True
                # return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        
