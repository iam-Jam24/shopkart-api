# Contributing to ShopKart API

1. Open an issue first. For bugs, include the input, the actual result and the expected result.
2. Create a branch named `fix/issue-<number>` or `feature/<short-name>`.
3. Every bug fix must add a test that fails before the fix and passes after it.
4. Never delete or weaken existing tests.
5. Run the full test suite before opening a pull request:

   ```
   pip install -r requirements-dev.txt
   python -m pytest -v
   ```

6. Reference the issue in the pull request description with `Fixes #<number>`.
7. A maintainer reviews and merges every pull request.
