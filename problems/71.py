class Solution:
    def simplifyPath(self, path: str) -> str:
        order = []

        for item in path.split('/'):
            if not item:
                continue
            elif item == '..':
                if order:
                    order.pop()
            elif item == ".":
                continue
            else:
                order.append(item)
        
        return '/' + '/'.join(order)