from typing import List
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> List[List[str]]:

        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)
        distance = {beginWord: 0}

        queue = deque([beginWord])
        found_distance = float('inf')

        while queue:
            word = queue.popleft()
            current_distance = distance[word]

            if current_distance >= found_distance:
                continue

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word not in words:
                        continue

                    if new_word not in distance:
                        distance[new_word] = current_distance + 1
                        parents[new_word].append(word)
                        queue.append(new_word)

                        if new_word == endWord:
                            found_distance = current_distance + 1

                    elif distance[new_word] == current_distance + 1:
                        parents[new_word].append(word)

        if endWord not in distance:
            return []

        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)

        return result