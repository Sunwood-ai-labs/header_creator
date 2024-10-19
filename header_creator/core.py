import os
import json
import requests
from loguru import logger
from .image_generator import generate_image
from .header_processor import process_header_image

def create_header(prompt, input_image_path, mask_image_path, output_image_path):
    logger.info("ヘッダー画像生成プロセスを開始します")

    # Ideogram APIを使用して画像を生成
    result = generate_image(prompt)

    if result:
        logger.info("生成された画像の情報:")
        logger.info(json.dumps(result, indent=2, ensure_ascii=False))
        
        # 生成された画像のURLを取得
        generated_image_url = result.get("image_url", "")
        
        if generated_image_url:
            # 生成された画像をダウンロード
            response = requests.get(generated_image_url)
            if response.status_code == 200:
                with open(input_image_path, 'wb') as f:
                    f.write(response.content)
                logger.info(f"生成された画像を保存しました: {input_image_path}")
                
                # ヘッダー画像を処理
                process_result = process_header_image(input_image_path, mask_image_path, output_image_path)
                logger.info(f"ヘッダー画像が生成されました: {process_result}")
                return process_result
            else:
                logger.error(f"画像のダウンロードに失敗しました: {response.status_code}")
        else:
            logger.error("生成された画像のURLが見つかりません")
    else:
        logger.warning("画像が生成されませんでした")

    logger.info("ヘッダー画像生成プロセスが完了しました")
    return None
