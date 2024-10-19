from header_creator import create_header

result = create_header(
    prompt="""
A vibrant and modern banner image for a GitHub repository called "Header Creator". The image should be in a 16:9 aspect ratio, perfect for a repository header. The main focus is a large, bold text that says "Header Creator" in the center, using a sleek, modern font with a gradient color scheme from deep blue to vibrant purple.

Behind the text, create a dynamic background that represents the concept of image creation and manipulation. Include abstract representations of:
1. A paintbrush leaving a trail of colorful pixels
2. Floating image frames with different aspect ratios
3. Swirling lines of code in a subtle, semi-transparent style

On one side of the image, show a simplified 3D representation of a computer or smartphone screen with a partially completed header image being created.

Use a color palette that combines deep blues, purples, and touches of cyan to create a tech-savvy and creative atmosphere. The overall style should be clean, professional, and slightly futuristic, appealing to developers and designers.

Ensure that the "Header Creator" text is the largest and most prominent element in the image, instantly catching the viewer's attention when they visit the repository.
    """,
    input_image_path="data/input2.png",
    mask_image_path="data/mask.png",
    output_image_path="data/output2.png",
    model="V_2_TURBO",
    magic_prompt="ON",
    aspect_ratio="ASPECT_16_9",
    style_type="RENDER_3D"
)

if result:
    print(f"ヘッダー画像が生成されました: {result}")
else:
    print("ヘッダー画像の生成に失敗しました")
