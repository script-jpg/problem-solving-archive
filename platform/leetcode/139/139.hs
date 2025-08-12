-- https://leetcode.com/problems/word-break/description/

splits :: [a] -> [[[a]]]
splits []     = [[]]
splits (x:xs) = [ (x:ys):yss | (ys:yss) <- splits xs ]
             ++ [ [x]:rest  | rest     <- splits xs ]

allTrue :: [Bool] -> Bool
allTrue = all (==True)

inDict :: [String] -> String -> Bool
inDict dict x = x `elem` dict

isEveryListElementsinDict :: [String] -> [String] -> Bool
isEveryListElementsinDict dict = allTrue . map (inDict dict)

wordBreak s wordDict = let boolList = map (isEveryListElementsinDict wordDict) (splits s)
  in any (==True) boolList

main :: IO()
main = do
  print (wordBreak "leetcode" ["leet", "code"])
  print (wordBreak "catsandog" ["cats", "dog", "sand", "and", "cat"])
