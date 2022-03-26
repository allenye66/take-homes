#README:

#you can run the file directly and it will output the answer
#at the bottom you can specify the grid letters and the valid words


#thank you for reading, please let me know if you have any questions
#you can reach me at allenye66@gmail.com


#creates a prefix tree or trie data structure
class PTree:
        #constructor creates a dict and boolean
        def __init__(self):
            self.children = {}
            self.isWord = False
         
        #takes in a word to add to the prefix tree
        #inserts a word into the prefix tree by building the nodes from the characters
        #and sets the boolean value to true
        def insert(self, word):
            curr = self
            for c in word:
                if c not in curr.children:
                    curr.children[c] = PTree()
                curr = curr.children[c]
            curr.isWord = True

#contains method findWords that builds a prefix tree then uses dfs to find the words that exist
class Solve:
    
        #takes in a board of letters and valid words
        #returns valid words found by using the boggle strategy
        def findWords(self, board, words):
            
            #builds a prefix tree and fills it with the valid words
            pt = PTree()
            for word in words:
                pt.insert(word)
            
            R, C = len(board), len(board[0])
            
            #what we will be returning
            res = set()
    
            #dfs to find which valid words can be reached with the boggle strategy
            def dfs(grid, r, c, node, word):
                
                #base cases
                if(r == R or c == C or r < 0 or c < 0):
                    return
                
                curr = grid[r][c]
                
                #more base cases
                if(curr == "#" or curr not in node.children):
                    return
                
                #backtracking algorithm   
                grid[r][c] = "#"
                
                node = node.children[curr]
                word += curr
                
                if node.isWord:
                    res.add(word)
                    
                #searches all adjacent positions
                dfs(grid, r - 1, c, node, word)
                dfs(grid, r + 1, c, node, word)
                dfs(grid, r, c + 1, node, word)
                dfs(grid, r, c - 1, node, word)
                dfs(grid, r - 1, c - 1, node, word)
                dfs(grid, r + 1, c + 1, node, word)
                dfs(grid, r - 1, c + 1, node, word)
                dfs(grid, r + 1, c - 1, node, word)
                
                grid[r][c] = curr
                    
            #runs dfs on each letter
            for i in range(R):
                for j in range(C):
                    dfs(board, i, j, pt, "")
            return list(res)
            

class Boggle:
    #takes in valid words
    def __init__(self, validWords):
        self.dictionary = validWords
        
    #takes in width, height, and letters
    #only letters are needed
    def SolveBoard(self, width, height, boardLetters):
        #creates a solver from the Solve class
        solver = Solve()
        return solver.findWords(boardLetters, self.dictionary)
 
        
def main(letters, validWords):
    b = Boggle(validWords)
    print(b.SolveBoard(3, 3, letters))
    #print('abroad' in b.SolveBoard(3, 3, letters) or 'robbed' in b.SolveBoard(3, 3, letters))

if __name__ == '__main__':
    letters = [['y', 'o', 'x'], ['r', 'b', 'a'], ['v', 'e', 'd']]
    validWords = ['abroad', 'robbed', 'abed', 'aero', 'aery', 'bad', 'bade', 'bead', 'bed', 'boa', 'bore', 'bored', 'box', 'boy', 'bread', 'bred', 'bro', 'broad', 'byre', 'dab', 'derby', 'orb', 'orbed', 'ore', 'read', 'red', 'road', 'rob', 'robe', 'robed', 'verb', 'very', 'yore', 'robbed', 'abroad', 'be', 'boar', 'dove']
    main(letters, validWords)