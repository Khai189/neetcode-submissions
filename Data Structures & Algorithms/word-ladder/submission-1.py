from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        if beginWord == endWord:
            return 1

        available_words = set(wordList)

        begin_frontier = {beginWord}
        end_frontier = {endWord}

        length = 1

        while begin_frontier and end_frontier:
            if len(begin_frontier) > len(end_frontier):
                begin_frontier, end_frontier = (
                    end_frontier,
                    begin_frontier
                )

            next_frontier = set()

            for word in begin_frontier:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        if char == word[i]:
                            continue

                        new_word = (
                            word[:i] + char + word[i + 1:]
                        )

                        # The two searches have met.
                        if new_word in end_frontier:
                            return length + 1

                        if new_word not in available_words:
                            continue

                        next_frontier.add(new_word)
                        available_words.remove(new_word)

            begin_frontier = next_frontier
            length += 1

        return 0

