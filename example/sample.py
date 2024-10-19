from header_creator import create_header

result = create_header(
    prompt="A cat paradise header image",
    input_image_path="data/input.png",
    mask_image_path="data/mask.png",
    output_image_path="data/output.png"
)

if result:
    print(f"ヘッダー画像が生成されました: {result}")
else:
    print("ヘッダー画像の生成に失敗しました")
