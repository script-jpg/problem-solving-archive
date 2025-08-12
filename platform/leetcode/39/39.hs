combinationSum :: [Int] -> Int -> [[Int]]
combinationSum _ 0 = [[]]
combinationSum [] _ = []
combinationSum (c:cs) target
  | target < 0 = []
  | otherwise = map (c:) (combinationSum (c:cs) (target-c)) ++ combinationSum cs target

main = print (combinationSum [2,3,6,7] 7)
