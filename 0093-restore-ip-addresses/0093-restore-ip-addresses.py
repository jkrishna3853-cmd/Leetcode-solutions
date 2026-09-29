class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)

        if n < 4 or n > 12:
            return []
        
        result = []
        
        def backtrack(start_idx: int, path: list[str]):

            if len(path) == 4:

                if start_idx == n:
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if start_idx + length > n:
                    break
                
                segment = s[start_idx : start_idx + length]

                if len(segment) > 1 and segment[0] == '0':
                    break

                if int(segment) > 255:
                    break

                backtrack(start_idx + length, path + [segment])

        backtrack(0, [])
        return result