import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="header-creator",
    version="0.2.1",
    author="Sunwood-ai-labs",
    author_email="your.email@example.com",
    description="A package to create header images using Ideogram API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sunwood-ai-labs/header_creator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "python-dotenv",
        "loguru",
        "click",
        "pic-to-header",  # この依存関係が PyPI に存在することを確認してください
    ],
    entry_points={
        "console_scripts": [
            "header-creator=header_creator.cli:cli",
        ],
    },
)
