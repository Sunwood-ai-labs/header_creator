import requests
import json
from loguru import logger
from .config import IDEOGRAM_API_KEY, DEFAULT_MODEL, DEFAULT_MAGIC_PROMPT, DEFAULT_ASPECT_RATIO, DEFAULT_STYLE_TYPE

def generate_image(prompt, model=DEFAULT_MODEL, magic_prompt_option=DEFAULT_MAGIC_PROMPT, 
                   aspect_ratio=DEFAULT_ASPECT_RATIO, style_type=DEFAULT_STYLE_TYPE):
    url = "https://api.ideogram.ai/generate"
    
    payload = {
        "image_request": {
            "model": model,
            "prompt": prompt,
            "magic_prompt_option": magic_prompt_option,
            "aspect_ratio": aspect_ratio,
            "style_type": style_type
        }
    }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Api-Key": IDEOGRAM_API_KEY
    }
    
    logger.info(f"Ideogram APIにリクエストを送信します。プロンプト: {prompt}")
    logger.info(f"パラメータ: モデル={model}, マジックプロンプト={magic_prompt_option}, アスペクト比={aspect_ratio}, スタイル={style_type}")
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        logger.success("Ideogram APIからの応答を正常に受信しました")
        return json.loads(response.text)
    else:
        logger.error(f"エラー: {response.status_code}")
        logger.error(response.text)
        return None
