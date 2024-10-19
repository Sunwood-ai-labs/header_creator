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
  <b>Header Creator は、Ideogram API を使用してヘッダー画像を生成し、処理するための Python パッケージです。バージョン 0.2.2 がリリースされました。</b>
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

## 🚀 プロジェクト概要

Header Creatorは、Ideogram APIを用いてヘッダー画像を生成するPythonパッケージです。コマンドラインインターフェース(CLI)とStreamlitアプリの両方から利用可能です。  バージョン 0.2.2では、Streamlitアプリのテーマ設定を追加し、UI/UXを向上させました。


## ✨ 主な機能

- Ideogram API を使用したヘッダー画像生成
- コマンドラインインターフェース (CLI) とStreamlitアプリからの利用
- 設定ファイル(`config.py`)によるカスタマイズ
- StreamlitアプリによるAPIキー管理、プロンプト入力、マスク画像アップロード、パラメータ設定
- ヘッダー画像のダウンロード機能 (v0.2.2から)
- 生成処理中のスピナー表示 (v0.2.2から)


## 🔧 使用方法

Streamlitアプリを使用することで、GUIから簡単にヘッダー画像を生成できます。`app.py` を実行してStreamlitアプリを起動してください。


### Python スクリプトから使用する場合

```python
from header_creator import create_header

result = create_header(
    prompt="A stunning tropical paradise header image",
    input_image_path="path/to/input.png",
    mask_image_path="path/to/mask.png",
    output_image_path="path/to/output.png",
    api_key="YOUR_API_KEY" # または環境変数 IDEOGRAM_API_KEY
)

if result:
    print(f"ヘッダー画像が生成されました: {result}")
else:
    print("ヘッダー画像の生成に失敗しました")
```

### コマンドラインから使用する場合

```bash
header-creator --prompt "A stunning tropical paradise header image" --input path/to/input.png --mask path/to/mask.png --output path/to/output.png --api-key YOUR_API_KEY # または環境変数 IDEOGRAM_API_KEY
```


## 📦 インストール手順

1. PyPI からインストールします：

```bash
pip install header-creator
```

2.  `.env` ファイルを作成し、`IDEOGRAM_API_KEY` にIdeogram APIキーを設定します (`.env.example`を参照)。


## ⚙️ 設定

`config.py` ファイルで以下のデフォルト設定を変更できます：

- `DEFAULT_MODEL`: 使用する Ideogram モデル (デフォルト: `V_2_TURBO`)
- `DEFAULT_MAGIC_PROMPT`: マジックプロンプトオプション (デフォルト: `ON`)
- `DEFAULT_ASPECT_RATIO`: 生成する画像のアスペクト比 (デフォルト: `ASPECT_16_9`)
- `DEFAULT_STYLE_TYPE`: 生成する画像のスタイルタイプ (デフォルト: `RENDER_3D`)

## 🆕 最新情報

- **v0.2.2:** Streamlitアプリのテーマ設定を追加、UI/UX向上、ヘッダー画像のダウンロード機能追加、生成処理中のスピナー表示追加。


## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🤝 貢献

バグ報告、機能リクエスト、プルリクエストを歓迎します。大きな変更を加える前に、まずイシューを開いて変更内容について議論してください。

## 🙏 謝辞

このプロジェクトは [Ideogram API](https://ideogram.ai/) を使用しています。  iris-s-coon さんと Maki さんに感謝します。