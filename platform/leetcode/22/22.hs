-- https://leetcode.com/problems/generate-parentheses/description/

dfs :: Int -> Int -> [String]
dfs 0 0 = [[]]
dfs 0 rpr = map (')':) (dfs 0 (rpr-1))
dfs lpr 0 = map ('(':) (dfs (lpr-1) 0)
dfs lpr rpr = map ('(':) (dfs (lpr-1) rpr) ++
  if lpr < rpr then map (')':) (dfs lpr (rpr-1)) else []

generateParenthesis :: Int -> [String]
generateParenthesis n = dfs n n

main :: IO()
main = print (generateParenthesis 3)
