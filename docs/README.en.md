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
  <a href="https://github.com/Sunwood-ai-labs/header-creator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sunwood-ai-labs/header-creator.svg" alt="License"></a>
  <a href="https://github.com/Sunwood-ai-labs/header-creator"><img src="https://img.shields.io/github/stars/Sunwood-ai-labs/header-creator.svg?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/Sunwood-ai-labs/header-creator/issues"><img src="https://img.shields.io/github/issues/Sunwood-ai-labs/header-creator.svg" alt="GitHub issues"></a>
</p>

<p align="center">
  <b>Header Creator is a Python package for generating and processing header images using the Ideogram API. Version 0.2.1 has been released.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white" alt="Click">
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white" alt="Loguru">
  <img src="https://img.shields.io/badge/Ideogram-FF6B6B?style=for-the-badge&logo=image&logoColor=white" alt="Ideogram">
  <img src="https://img.shields.io/badge/pic--to--header-4B0082?style=for-the-badge&logo=image&logoColor=white" alt="pic-to-header">
</p>

</div>

## 🚀 Project Overview

Header Creator is a Python package that generates header images using the Ideogram API. It's usable from both a command-line interface (CLI) and a Streamlit app.  Version 0.2.1 adds a Streamlit app user interface and changes the repository name from "HarmonAI III" to "Header Creator".


## ✨ Key Features

- Header image generation using the Ideogram API
- Usable from both a command-line interface (CLI) and a Streamlit app
- Customization via a configuration file (`config.py`)
- API key management, prompt input, mask image upload, and parameter settings via the Streamlit app


## 🔧 Usage

The Streamlit app provides an easy-to-use GUI for generating header images. Run `app.py` to start the Streamlit app.


### Using from a Python script:

```python
from header_creator import create_header

result = create_header(
    prompt="A stunning tropical paradise header image",
    input_image_path="path/to/input.png",
    mask_image_path="path/to/mask.png",
    output_image_path="path/to/output.png",
    api_key="YOUR_API_KEY" # or environment variable IDEOGRAM_API_KEY
)

if result:
    print(f"Header image generated: {result}")
else:
    print("Header image generation failed")
```

### Using from the command line:

```bash
header-creator --prompt "A stunning tropical paradise header image" --input path/to/input.png --mask path/to/mask.png --output path/to/output.png --api-key YOUR_API_KEY # or environment variable IDEOGRAM_API_KEY
```


## 📦 Installation

1. Install from PyPI:

```bash
pip install header-creator
```

2. Create a `.env` file and set your Ideogram API key to `IDEOGRAM_API_KEY` (see `.env.example`).


## ⚙️ Configuration

The following default settings can be changed in the `config.py` file:

- `DEFAULT_MODEL`: The Ideogram model to use (default: `V_2_TURBO`)
- `DEFAULT_MAGIC_PROMPT`: Magic prompt option (default: `ON`)
- `DEFAULT_ASPECT_RATIO`: Aspect ratio of the generated image (default: `ASPECT_16_9`)
- `DEFAULT_STYLE_TYPE`: Style type of the generated image (default: `RENDER_3D`)


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Bug reports, feature requests, and pull requests are welcome. Please open an issue to discuss changes before making large modifications.

## 🙏 Acknowledgements

This project uses the [Ideogram API](https://ideogram.ai/). Thanks to iris-s-coon and Maki.