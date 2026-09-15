from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj={st:[] for st in wordList}

        def are_neighbors(word1,word2):
            if word1==word2:
                return False
            if len(word1)!=len(word2):
                return False
            count=0    
            for c1,c2 in zip(word1,word2):
                if c1!=c2:
                    count+=1
            if count!=1:
                return False
            
            return True            


        for word1 in wordList:
            for word2 in wordList:
                if are_neighbors(word1,word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)

        distance={word:-1 for word in wordList}
        
        def bfs(start):
            queue=deque()
            queue.append(start)
            distance[start]=0
            while queue:
                curr=queue.popleft()
                for word in wordList:
                    if are_neighbors(curr,word):
                        if distance[word]==-1:
                            distance[word]=distance[curr]+1
                            queue.append(word)

        bfs(beginWord)
        print(distance)

        return distance[endWord]+1




