from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup (
    name="fileclip",
    version="0.0.1",
    description="Copies the contents of a specified file to your clipboard.",
    url="https://github.com/reppocs/fileclip",
    author="Corey Reppond",
    author_email="reppocs@gmail.com",
    license="MIT",
    install_requires=["pyperclip", "binaryornot"] 
)
