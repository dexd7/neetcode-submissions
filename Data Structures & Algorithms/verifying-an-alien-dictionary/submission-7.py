class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        order_lookup_o1 = {c: i for i, c in enumerate(order)}
        for word_idx in range(1, len(words)):
            small_word = words[word_idx-1]
            big_word = words[word_idx]
            for j in range(len(small_word)):
                if j>=len(big_word):
                    return False
                if small_word[j] != big_word[j]:
                    if order_lookup_o1[small_word[j]]>order_lookup_o1[big_word[j]]:
                        return False
                    break
        return True