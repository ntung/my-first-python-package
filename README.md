# Simple Python Package

This is a simple example package. Getting through the documentation below, we create a simple Python package and publish it on PyPi.

You can use [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

# How to build and upload
1. Update the version in the `pyproject.toml` file to avoid the errors when uploading the package to TestPyPi or PyPi.
2. Build: `python -m build`.
3. Upload: `python -m twine upload --repository testpypi dist/*`.

# Tests
Run `pip install pytest` to install the pytest package. See the `tests/utils_test.py` for the tips/tricks to load package path. Then, run `pytest`.

# References
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
