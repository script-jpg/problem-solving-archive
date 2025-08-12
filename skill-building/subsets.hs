import Data.List (tails, inits)
-- lists all perfect squares <= 50
squaresUnder50 :: [Int]
squaresUnder50 = [x*x | x <- [1..10], x*x <= 50]
squaresUnder50' = takeWhile (<=50) [x*x | x <- [1..]]

withParity :: [ (Int, String)]
withParity = [ (x, parity) | x <- [1..8], let parity = if even x then "even" else "odd"]

safeTail :: [a] -> [a]
safeTail [] = []
safeTail (x:xs) = xs

myMap :: (a->b) -> [a] -> [b]
myMap _ [] = []
myMap f (x:xs) = f x : myMap f xs

insertEverywhere :: a -> [a] -> [[a]]
insertEverywhere v [] = [[v]]
insertEverywhere v (y:ys) = (v:y:ys): map (y:) (insertEverywhere v ys) 

insertEverywhere' :: a -> [a] -> [[a]]
insertEverywhere' v ys = [pre ++ [v] ++ post | (pre,post) <- splits ys] where
  splits xs = zip (inits xs) (tails xs)

window3 :: [a] -> [[a]]
window3 xs = takeWhile (\x -> length x == 3) (map (take 3) (tails xs))

windowN :: [a] -> Int -> [[a]]
windowN xs n = takeWhile (\x -> length x == n) (map (take n) (tails xs))

permute :: [a] -> [[a]]
permute [] = [[]]
permute (x:xs) = [pre ++ [x] ++ post | rest <- permute xs, (pre, post) <- splits rest]
  where splits a = zip (inits a) (tails a)

main :: IO()
main = print (insertEverywhere 'v' "hello")
