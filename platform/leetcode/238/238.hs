productExceptSelf nums = zipWith (*) leftProducts rightProducts where
  leftProducts = init (scanl (*) 1 nums)
  rightProducts = tail (scanr (*) 1 nums)

main :: IO()
main = print(productExceptSelf [1,2,3,4])
