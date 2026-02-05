# Quick Git Commit Guide (Beginner)

Use these simple steps to save and share your work manually.

1. See what changed:
   git status

2. Stage files you want to save (example: the calculator file):
   git add "Python Program Choices (User Verify).py"
   # or stage all changes to tracked files:
   git add -u

3. Commit with a short message:
   git commit -m "Add simple calculator"

4. Push to the remote (GitHub):
   git push origin main

Notes & tips:
- To only stage certain files, list them with `git add file1 file2`.
- To undo a staged file: `git reset HEAD file`.
- To amend the last commit (before pushing): `git commit --amend -m "New message"`.
- If you need to create a branch: `git checkout -b my-feature` then push with `git push -u origin my-feature`.
- Check `git log --oneline` to see recent commits.

If you want, I can add a simple alias or script to make this even shorter. 👍