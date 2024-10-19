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
  <img src="https://via.placeholder.com/600x200.png?text=Header+Creator" alt="Header Creator Logo">

# Header Creator

<p align="center">
  <a href="https://pypi.org/project/header-creator/"><img src="https://img.shields.io/pypi/v/header-creator.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/header-creator/"><img src="https://img.shields.io/pypi/pyversions/header-creator.svg" alt="Python versions"></a>
  <a href="https://github.com/yourusername/header-creator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/yourusername/header-creator.svg" alt="License"></a>
</p>

<p align="center">
  <b>Header Creator is a Python package for generating and processing header images using the Ideogram API.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white" alt="Click">
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white" alt="Loguru">
  <img src="https://img.shields.io/badge/Ideogram-FF6B6B?style=for-the-badge&logo=image&logoColor=white" alt="Ideogram">
</p>

</div>

## 🚀 Features

- Image generation using the Ideogram API
- Processing and saving of generated images
- Command-line interface (CLI) support

## 📦 Installation

1. Install from PyPI:

```bash
pip install header-creator
```

2. Create a `.env` file and set your Ideogram API key:

```
IDEOGRAM_API_KEY=your_ideogram_api_key_here
```

## 🛠 Usage

### Using from a Python script

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

### Using from the command line

```bash
header-creator --prompt "A stunning tropical paradise header image" --input path/to/input.png --mask path/to/mask.png --output path/to/output.png
```

## ⚙️ Configuration

You can change the following default settings in the `config.py` file:

- `DEFAULT_MODEL`: The Ideogram model to use
- `DEFAULT_MAGIC_PROMPT`: Magic prompt options
- `DEFAULT_ASPECT_RATIO`: Aspect ratio of the generated image
- `DEFAULT_STYLE_TYPE`: Style type of the generated image

## 👨‍💻 Development

1. Clone this repository:

```bash
git clone https://github.com/yourusername/header-creator.git
cd header-creator
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3. Install development dependencies:

```bash
pip install -r requirements.txt
```

4. Run tests:

```bash
pytest
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Bug reports, feature requests, and pull requests are welcome.  Please open an issue to discuss changes before making large modifications.

## 🙏 Acknowledgements

This project utilizes the [Ideogram API](https://ideogram.ai/).