import logging
import os
import shutil

import nico_font_tool
from examples import fonts_dir, outputs_dir

logging.basicConfig(level=logging.DEBUG)


def convert_font(
        font_file_name: str,
        outputs_name: str,
        font_size: int = None,
        glyph_offset_x: int = 0,
        glyph_offset_y: int = 0,
        glyph_adjust_width: int = 0,
        glyph_adjust_height: int = 0,
):
    font_file_path = os.path.join(fonts_dir, font_file_name)
    sheet_data, alphabet = nico_font_tool.create_sheet(
        font_file_path,
        font_size,
        glyph_offset_x,
        glyph_offset_y,
        glyph_adjust_width,
        glyph_adjust_height,
    )

    palette_outputs_dir = os.path.join(outputs_dir, 'palette')
    if not os.path.exists(palette_outputs_dir):
        os.makedirs(palette_outputs_dir)
    nico_font_tool.save_palette_png(sheet_data, palette_outputs_dir, outputs_name)
    nico_font_tool.save_dat_file(alphabet, palette_outputs_dir, outputs_name)
    
    rgba_outputs_dir = os.path.join(outputs_dir, 'rgba')
    if not os.path.exists(rgba_outputs_dir):
        os.makedirs(rgba_outputs_dir)
    nico_font_tool.save_rgba_png(sheet_data, rgba_outputs_dir, outputs_name)
    nico_font_tool.save_dat_file(alphabet, rgba_outputs_dir, outputs_name)


def main():
    if os.path.exists(outputs_dir):
        shutil.rmtree(outputs_dir)
    os.makedirs(outputs_dir)

    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-8px-monospaced.woff2',
        outputs_name='fusion-pixel-8px-monospaced',
        font_size=8,
    )
    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-8px-proportional.woff2',
        outputs_name='fusion-pixel-8px-proportional',
        font_size=8,
    )
    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-10px-monospaced.woff2',
        outputs_name='fusion-pixel-10px-monospaced',
        font_size=10,
    )
    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-10px-proportional.woff2',
        outputs_name='fusion-pixel-10px-proportional',
        font_size=10,
    )
    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-12px-monospaced.woff2',
        outputs_name='fusion-pixel-12px-monospaced',
        font_size=12,
    )
    convert_font(
        font_file_name='fusion-pixel/fusion-pixel-12px-proportional.woff2',
        outputs_name='fusion-pixel-12px-proportional',
        font_size=12,
    )
    convert_font(
        font_file_name='unifont/unifont-15.0.01.ttf',
        outputs_name='unifont',
        font_size=16,
    )
    convert_font(
        font_file_name='unifont/unifont-15.0.01.bdf',
        outputs_name='unifont-bdf',
    )
    convert_font(
        font_file_name='roboto/Roboto-Regular.ttf',
        outputs_name='roboto',
        font_size=24,
    )


if __name__ == '__main__':
    main()
