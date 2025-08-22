class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def g(lpr, rpr, acc):
            match (lpr, rpr):
                case (0,0):
                    return [acc]
                case (0, _):
                    return g(0, rpr-1, acc+")")
                case _:
                    return g(lpr-1, rpr, acc+"(") + ([] if lpr >= rpr else g(lpr, rpr-1, acc+")"))
        return g(n,n,"")
