from collections import deque
from typing import List

# BFS ALGORITHM 

def word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> List[str]:

    word_set = set(wordList)
    
    if endWord not in word_set:
        return []
    
    queue = deque([(beginWord, [beginWord])])
    visited = {beginWord}
    
    while queue:
        current_word, path = queue.popleft()
        
        if current_word == endWord:
            return path
        
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + char + current_word[i+1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, path + [new_word]))
    
    return [] 