from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        chars = [c for c in sorted(freq.keys(), reverse=True) if freq[c] >= k]
        max_len = len(s) // k

        def is_k_subsequence(sub):
            target = sub * k
            it = iter(s)
            return all(c in it for c in target)
        queue = deque([''])
        result = ''
        while queue:
            curr = queue.popleft()
            for c in chars:
                nxt = curr + c
                if sum(nxt.count(ch) * k for ch in set(nxt)) > sum(freq[ch] for ch in set(nxt)):
                    continue
                if is_k_subsequence(nxt):
                    if len(nxt) > len(result) or (len(nxt) == len(result) and nxt > result):
                        result = nxt
                    if len(nxt) < max_len: 
                        queue.append(nxt)
        return result
