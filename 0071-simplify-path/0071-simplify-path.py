class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        
        for portion in components:
            if portion == "" or portion == ".":

                continue
            elif portion == "..":

                if stack:
                    stack.pop()
            else:

                stack.append(portion)

        return "/" + "/".join(stack)