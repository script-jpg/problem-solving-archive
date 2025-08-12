import Data.List (inits, tails)

permute :: [a] -> [[a]]
permute [] = [[]]
permute (x:xs) = [pre ++ [x] ++ post | rest <- permute xs, (pre, post) <- splits rest]
  where splits a = zip (inits a) (tails a)

main :: IO()
main = print (permute [1,2,3])
