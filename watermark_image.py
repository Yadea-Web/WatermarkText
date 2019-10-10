# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

def add_image_to_image(backimage, watermark, position):
	#创建底图
	target = Image.new('RGBA', (backimage.size[0], backimage.size[1]), (0, 0, 0, 0))

	# 如果水印比图片大，就设置成相同大小的
	if (backimage.size[0] < watermark.size[0] or backimage.size[1] < watermark.size[1]):
		watermark = watermark.resize((backimage.size[0], backimage.size[1]))

	# 分离透明通道
	r,g,b,a = watermark.split()
	# 将头像贴到底图
	backimage.convert("RGBA")
	target.paste(backimage, (0,0))

	#将装饰贴到底图
	watermark.convert("RGBA")
	if int(position) == 1:
		target.paste(watermark,(0,0))
	elif int(position) == 2:
		target.paste(watermark,(0,int(backimage.size[1]-watermark.size[1])), mask=a)
	elif int(position) == 3:
		target.paste(watermark,(int(backimage.size[0]-watermark.size[0]),0), mask=a)
	elif int(position) == 4:
		target.paste(watermark,(int(backimage.size[0]-watermark.size[0]),int(backimage.size[1]-watermark.size[1])), mask=a)
	elif int(position) == 5:
		target.paste(watermark,(int((backimage.size[0]-watermark.size[0])/2),int((backimage.size[1]-watermark.size[1])/2)), mask=a)
	else:
		target.paste(watermark,(0,0), mask=a)

	# 保存图片
	target.save("markResult.png")
	print('Image Watermark Finished!!! See the markResult.png')

if __name__ == '__main__':
	image = input("please enter the image url: ")
	markImage = input("please enter the watermark image url: ")
	img = Image.open(image)
	watermark = Image.open(markImage)
	if format(watermark.mode) == 'RGBA':
		print("watermark的色彩模式为{}".format(watermark.mode))
		position = input("please enter the watermark position, 1.top left 2.top right 3.bottom left 4.bottom right 5.center: ")
		add_image_to_image(img, watermark, position)
	else:
		print("水印图片色彩模式不正确，必须为RGBA")
