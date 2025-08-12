cartesianAll :: [[a]] -> [[a]]
cartesianAll []     = [[]]
cartesianAll (xs:xss) = [ x:ys | x  <- xs, ys <- cartesianAll xss]

getNumbers '2' = "abc"
getNumbers '3' = "def"
getNumbers '4' = "ghi"
getNumbers '5' = "jkl"
getNumbers '6' = "mno"
getNumbers '7' = "pqrs"
getNumbers '8' = "tuv"
getNumbers '9' = "wxyz"
getNumbers _ = "_"

letterCombinations :: String -> [String]
letterCombinations digits = let letters = map getNumbers digits in cartesianAll letters
