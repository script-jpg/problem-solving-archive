import Data.Char (isAlpha, toLower)
import Utils.TestUtils (test)

isPalindrome s =
  let parsed = filter isAlpha s in
  let word = map toLower parsed in
  word == reverse word

main = do
  test "1" (isPalindrome "A man, a plan, a canal: Panama") True
  test "2" (isPalindrome "race a car") False
  test "3" (isPalindrome " ") True
