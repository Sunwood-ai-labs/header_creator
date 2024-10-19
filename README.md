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
  <b>Header Creator は、Ideogram API を使用してヘッダー画像を生成し、処理するための Python パッケージです。</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Click-000000?style=for-the-badge&logo=python&logoColor=white" alt="Click">
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white" alt="Loguru">
  <img src="https://img.shields.io/badge/Ideogram-FF6B6B?style=for-the-badge&logo=image&logoColor=white" alt="Ideogram">
</p>

</div>

## 🚀 機能

- Ideogram API を使用した画像生成
- 生成された画像の処理と保存
- コマンドラインインターフェース (CLI) のサポート

## 📦 インストール

1. PyPI からインストールします：

```bash
pip install header-creator
```

2. `.env` ファイルを作成し、Ideogram API キーを設定します：

```
IDEOGRAM_API_KEY=your_ideogram_api_key_here
```

## 🛠 使用方法

### Python スクリプトから使用する場合

```python
from header_creator import create_header

result = create_header(
    prompt="A stunning tropical paradise header image",
    input_image_path="path/to/input.png",
    mask_image_path="path/to/mask.png",
    output_image_path="path/to/output.png"
)

if result:
    print(f"ヘッダー画像が生成されました: {result}")
else:
    print("ヘッダー画像の生成に失敗しました")
```

### コマンドラインから使用する場合

```bash
header-creator --prompt "A stunning tropical paradise header image" --input path/to/input.png --mask path/to/mask.png --output path/to/output.png
```

## ⚙️ 設定

`config.py` ファイルで以下のデフォルト設定を変更できます：

- `DEFAULT_MODEL`: 使用する Ideogram モデル
- `DEFAULT_MAGIC_PROMPT`: マジックプロンプトオプション
- `DEFAULT_ASPECT_RATIO`: 生成する画像のアスペクト比
- `DEFAULT_STYLE_TYPE`: 生成する画像のスタイルタイプ

## 👨‍💻 開発

1. このリポジトリをクローンします：

```bash
git clone https://github.com/yourusername/header-creator.git
cd header-creator
```

2. 仮想環境を作成し、アクティベートします：

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

3. 開発用の依存関係をインストールします：

```bash
pip install -r requirements.txt
```

4. テストを実行します：

```bash
pytest
```

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🤝 貢献

バグ報告、機能リクエスト、プルリクエストを歓迎します。大きな変更を加える前に、まずイシューを開いて変更内容について議論してください。

## 🙏 謝辞

このプロジェクトは [Ideogram API](https://ideogram.ai/) を使用しています。
