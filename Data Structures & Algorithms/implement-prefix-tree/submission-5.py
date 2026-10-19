
class TreeNode:
    def __init__(self, word: str = ""):
        next = ""
        if len(word) > 0:
            self.val = word[0]
            next = word[1:]
        else:
            self.val = ""

        self.nexts = {}
        if len(next) > 0:
            newNode = TreeNode(next)
            self.nexts[next[0]] = newNode
            self.isWord = False
        else:
            self.isWord = True


class PrefixTree:
    root: TreeNode 

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:

        parentNode = self.root
        remainingWord = word

        while len(remainingWord) > 0 and remainingWord[0] in parentNode.nexts.keys():
            parentNode = parentNode.nexts[remainingWord[0]]
            remainingWord = remainingWord[1:]
        
        # node doesnt exist
        if len(remainingWord) > 0:
            # create start node 
            node = TreeNode(remainingWord)
            parentNode.nexts[remainingWord[0]] = node
        else:
            parentNode.isWord = True
        

    def search(self, word: str) -> bool:
        #print(f"Searching for: {word}, in the {self.root.nexts.keys()}")

        found = False
        i = 0
        node = self.root
        while not found and i < len(word):
            if word[i] in node.nexts.keys():
                node = node.nexts[word[i]]
                i += 1
                if i == len(word) and node.isWord:
                    found = True
            else:
                return False

        return found  

        
    def startsWith(self, prefix: str) -> bool:
        found = False
        i = 0
        node = self.root
        while not found and i < len(prefix):
            if prefix[i] in node.nexts.keys():
                node = node.nexts[prefix[i]]
                i += 1
                if i == len(prefix):
                    found = True
            else:
                return False

        return found  
