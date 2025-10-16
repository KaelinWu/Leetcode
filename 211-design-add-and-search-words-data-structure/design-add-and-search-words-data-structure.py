class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.is_word = True


        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i== len(word):
                return node.is_word
            
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]],i+1)
            return False
        return dfs(self.root,0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)