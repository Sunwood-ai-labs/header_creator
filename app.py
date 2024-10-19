import streamlit as st
import os
from header_creator import create_header

# ページ設定
st.set_page_config(
    page_title="header-creator",
    page_icon="🖼️",
    layout="wide"
)

def main():
    st.markdown("""

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
  <b>Header Creator は、Ideogram API を使用してヘッダー画像を生成し、処理するための Python パッケージです。バージョン 0.1.1 がリリースされました。</b>
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

                """, unsafe_allow_html=True)

    # API Key input (password field for masking)
    api_key = st.text_input("API Key", type="password")

    # Input parameters
    prompt = st.text_area("Prompt", value="""
A vibrant and modern banner image for a GitHub repository called "Header Creator". The image should be in a 16:9 aspect ratio, perfect for a repository header. The main focus is a large, bold text that says "Header Creator" in the center, using a sleek, modern font with a gradient color scheme from deep blue to vibrant purple.

Behind the text, create a dynamic background that represents the concept of image creation and manipulation. Include abstract representations of:
1. A paintbrush leaving a trail of colorful pixels
2. Floating image frames with different aspect ratios
3. Swirling lines of code in a subtle, semi-transparent style

On one side of the image, show a simplified 3D representation of a computer or smartphone screen with a partially completed header image being created.

Use a color palette that combines deep blues, purples, and touches of cyan to create a tech-savvy and creative atmosphere. The overall style should be clean, professional, and slightly futuristic, appealing to developers and designers.

Ensure that the "Header Creator" text is the largest and most prominent element in the image, instantly catching the viewer's attention when they visit the repository.
    """, height=300)

    mask_image = st.file_uploader("Mask Image", type=["png", "jpg", "jpeg"])

    model = st.selectbox("Model", ["V_1", "V_2", "V_2_TURBO"])
    magic_prompt = st.radio("Magic Prompt", ["ON", "OFF"])
    aspect_ratio = st.selectbox("Aspect Ratio", ["ASPECT_16_9", "ASPECT_4_3", "ASPECT_1_1"])
    style_type = st.selectbox("Style Type", ["RENDER_3D", "FLAT", "REALISTIC"])

    if st.button("Generate Header"):
        if api_key and mask_image:
            # Save uploaded mask image temporarily
            mask_image_path = "temp_mask.png"
            with open(mask_image_path, "wb") as f:
                f.write(mask_image.getvalue())

            # Set paths for input and output images
            input_image_path = "temp_input.png"
            output_image_path = "output.png"

            # Call create_header function
            result = create_header(
                prompt=prompt,
                input_image_path=input_image_path,
                mask_image_path=mask_image_path,
                output_image_path=output_image_path,
                api_key=api_key,
                model=model,
                magic_prompt=magic_prompt,
                aspect_ratio=aspect_ratio,
                style_type=style_type
            )

            if result:
                st.success(f"Header image generated: {result}")
                st.image(output_image_path)
            else:
                st.error("Failed to generate header image")

            # Clean up temporary files
            os.remove(mask_image_path)
            if os.path.exists(input_image_path):
                os.remove(input_image_path)
        else:
            if not api_key:
                st.warning("Please enter your API Key")
            if not mask_image:
                st.warning("Please upload a mask image")

if __name__ == "__main__":
    main()
