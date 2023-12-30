from typing import List


class Solution:
    @staticmethod
    def findwordscontaining(words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]


Input_words = ["leet", "code"]
input_x = "e"
solution_instance = Solution()
print(solution_instance.findwordscontaining(words=Input_words, x=input_x))
