import click
from .core import create_header

@click.command()
@click.option('--prompt', required=True, help='画像生成のためのプロンプト')
@click.option('--input', 'input_image_path', required=True, help='入力画像のパス')
@click.option('--mask', 'mask_image_path', required=True, help='マスク画像のパス')
@click.option('--output', 'output_image_path', required=True, help='出力画像のパス')
def cli(prompt, input_image_path, mask_image_path, output_image_path):
    """ヘッダー画像を生成するCLIツール"""
    result = create_header(prompt, input_image_path, mask_image_path, output_image_path)
    if result:
        click.echo(f"ヘッダー画像が正常に生成されました: {result}")
    else:
        click.echo("ヘッダー画像の生成に失敗しました")

if __name__ == '__main__':
    cli()
