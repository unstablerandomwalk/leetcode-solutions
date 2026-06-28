from collections import defaultdict
from functools import lru_cache
class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        mp = defaultdict(list)
        for a in allowed:
            mp[(a[0], a[1])].append(a[2])
        @lru_cache(None)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs("".join(path))
                if (row[i], row[i+1]) not in mp:
                    return False              
                for c in mp[(row[i], row[i+1])]:
                    path.append(c)
                    if build_next(i + 1, path):
                        return True
                    path.pop()
                return False
            return build_next(0, [])
        return dfs(bottom)
        