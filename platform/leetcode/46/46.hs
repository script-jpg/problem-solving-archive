import Data.List (inits, tails)

splits :: [a] -> [([a], [a])]
splits xs = zip (inits xs) (tails xs)

permute :: [a] -> [[a]]
permute [] = [[]]
permute (x:xs) = [pre ++ [x] ++ post | rest <- permute xs, (pre, post) <- splits rest]

main :: IO()
main = print (permute [1,2,3])
