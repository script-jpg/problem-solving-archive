subsets :: [a] -> [[a]]
subsets [] = [[]]
subsets (x:xs) = let ps = subsets xs in ps ++ map (x:) ps 

main :: IO()
main = print (subsets [1,2])
