module Utils.TestUtils (test) where

-- A simple reusable test function
test :: (Eq a, Show a) => String -> a -> a -> IO ()
test label got expected =
    if got == expected
        then putStrLn (label ++ ": PASS")
        else putStrLn (label ++ ": FAIL (got " ++ show got ++ ", expected " ++ show expected ++ ")")
