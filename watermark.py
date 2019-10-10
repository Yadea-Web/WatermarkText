from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text):
    font = ImageFont.truetype('./JDJSZHONG.TTF', 20)

    # 添加透明背景
    new_img = Image.new('RGBA', (image.size[0], image.size[1]), (0, 0, 0, 0))
    new_img.paste(image, (0, 0))

    # 添加水印文字
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(10, rgba_image.size[0], font_len*20):
        for j in range(10, rgba_image.size[1], 100):
        	image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)
    image_with_text.save(u'%s.png'%(text))
    print('Image Watermark Finished!!! See the %s.png'%(text))
    return image_with_text


if __name__ == '__main__':
	image = input("please enter the image url: ")
	text = input("please enter the watermark text: ")
	img = Image.open(image)
	im_after = add_text_to_image(img, text)