import click
from .core import create_header
from .config import DEFAULT_MODEL, DEFAULT_MAGIC_PROMPT, DEFAULT_ASPECT_RATIO, DEFAULT_STYLE_TYPE

@click.command()
@click.option('--prompt', required=True, help='画像生成のためのプロンプト')
@click.option('--input', 'input_image_path', required=True, help='入力画像のパス')
@click.option('--mask', 'mask_image_path', required=True, help='マスク画像のパス')
@click.option('--output', 'output_image_path', required=True, help='出力画像のパス')
@click.option('--model', default=DEFAULT_MODEL, help='使用するIdeogramモデル')
@click.option('--magic-prompt', default=DEFAULT_MAGIC_PROMPT, help='マジックプロンプトオプション')
@click.option('--aspect-ratio', default=DEFAULT_ASPECT_RATIO, help='生成する画像のアスペクト比')
@click.option('--style-type', default=DEFAULT_STYLE_TYPE, help='生成する画像のスタイルタイプ')
def cli(prompt, input_image_path, mask_image_path, output_image_path, model, magic_prompt, aspect_ratio, style_type):
    """ヘッダー画像を生成するCLIツール"""
    result = create_header(prompt, input_image_path, mask_image_path, output_image_path,
                           model=model, magic_prompt=magic_prompt, aspect_ratio=aspect_ratio, style_type=style_type)
    if result:
        click.echo(f"ヘッダー画像が正常に生成されました: {result}")
    else:
        click.echo("ヘッダー画像の生成に失敗しました")

if __name__ == '__main__':
    cli()
