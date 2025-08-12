tf :: Int -> String
tf x
  | mod x 15 == 0 = "FizzBuzz"
  | mod x 3 == 0 = "Fizz"
  | mod x 5 == 0 = "Buzz"
  | otherwise = show x

fizzbuzz :: Int -> [String]
fizzbuzz n = map tf [1..n]

main :: IO()
main = print (fizzbuzz 15)
