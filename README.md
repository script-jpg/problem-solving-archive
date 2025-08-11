# Problem Solving Archive

A personal archive of programming problem solutions, organized by platform and problem number, with support for multiple languages and detailed notes.

## 📂 Structure

```
platform/
    leetcode/
        <problem-number>/
            <problem-number>.py     # Python solution
            <problem-number>.hs     # Haskell solution
            <problem-number>.md     # Markdown notes (for Obsidian)
    kattis/
        <problem-name>.py           # Python solution for Kattis problem
```

### 🔹 LeetCode Organization
Each LeetCode problem is placed in a folder named after its problem number.
This allows storing multiple solutions in different languages for the same problem.

Example:
```
platform/leetcode/1/
    1.py   # Python solution
    1.hs   # Haskell solution
    1.md   # Notes and tags (used with Obsidian)
```

### 🔹 Kattis Organization
Kattis problems are organized by their problem name (or identifier) as filenames.

Example:
```
platform/kattis/lvable.py
```

---

## 📝 Notes & Tags with Obsidian
The `.md` files are written for use with [Obsidian](https://obsidian.md/), allowing:
- Tags for categorizing problems (`#dp`, `#graph`, `#greedy`, etc.)
- Links to related problems
- Explanations of solution approaches
- Space for alternative ideas or optimizations

Example `1.md`:
```markdown
# Two Sum
#array #hashmap

Find two numbers that add up to a target value.

**Approach**: Use a hashmap for O(n) lookup.
```

---

## 🚀 Future Expansion
This structure supports adding:
- More platforms (e.g., Codeforces, AtCoder)
- Multiple solutions per problem in different languages
- Rich markdown notes with references
