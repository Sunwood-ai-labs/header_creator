---
title: Header Creator
emoji: 🦀
colorFrom: purple
colorTo: yellow
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: mit
---

<div align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/header_creator/refs/heads/main/docs/header-creator.png" alt="Header Creator Logo">

# Header Creator

<p align="center">
  <a href="https://pypi.org/project/header-creator/"><img src="https://img.shields.io/pypi/v/header-creator.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/header-creator/"><img src="https://img.shields.io/pypi/pyversions/header-creator.svg" alt="Python versions"></a>
  <a href="https://github.com/Sunwood-ai-labs/header_creator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sunwood-ai-labs/header-creator.svg" alt="License"></a>
</p>

<p align="center">
  <b>Header Creator is a Python package for generating and processing header images using the Ideogram API. Version 0.1.1 has been released.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white" alt="Click">
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white" alt="Loguru">
  <img src="https://img.shields.io/badge/Ideogram-FF6B6B?style=for-the-badge&logo=image&logoColor=white" alt="Ideogram">
</p>

</div>

## 🚀 Project Overview

Header Creator is a Python package that generates header images using the Ideogram API. It can be used both from a command-line interface (CLI) and from Python scripts.  Version 0.1.1 updates the README file with absolute paths for the logo image and updates the English and Japanese versions of the README. This improves display from GitHub Pages and similar services.


## ✨ Key Features

- Header image generation using the Ideogram API
- Usable from both a command-line interface (CLI) and Python scripts
- Customization via a configuration file (`config.py`)


## 🔧 Usage

### Using from a Python Script

```python
from header_creator import create_header

result = create_header(
    prompt="A stunning tropical paradise header image",
    input_image_path="path/to/input.png",
    mask_image_path="path/to/mask.png",
    output_image_path="path/to/output.png"
)

if result:
    print(f"Header image generated: {result}")
else:
    print("Header image generation failed")
```

### Using from the Command Line

```bash
header-creator --prompt "A stunning tropical paradise header image" --input path/to/input.png --mask path/to/mask.png --output path/to/output.png
```

## 📦 Installation

1. Install from PyPI:

```bash
pip install header-creator
```

2. Create a `.env` file and set your Ideogram API key to `IDEOGRAM_API_KEY` (see `.env.example`).


## ⚙️ Configuration

The following default settings can be changed in the `config.py` file:

- `DEFAULT_MODEL`: The Ideogram model to use
- `DEFAULT_MAGIC_PROMPT`: Magic prompt options
- `DEFAULT_ASPECT_RATIO`: The aspect ratio of the generated image
- `DEFAULT_STYLE_TYPE`: The style type of the generated image

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Bug reports, feature requests, and pull requests are welcome. Please open an issue to discuss changes before making large modifications.

## 🙏 Acknowledgements

This project uses the [Ideogram API](https://ideogram.ai/). Thanks to iris-s-coon and Maki.