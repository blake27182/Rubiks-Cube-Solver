from PIL import Image
import math

try:
	original = Image.open("IMG_5180.jpg")
except:
	print("unable to open file")

faceUSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]
faceDSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]
faceLSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]
faceRSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]
faceFSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]
faceBSquares = [(1050,1050,1250,1250),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950),(500,750,700,950)]

faceUColors = [[0,0,0],[0,0,0],[0,0,0]]
faceDColors = [[1,1,1],[1,1,1],[1,1,1]]
faceLColors = [[2,2,2],[2,2,2],[2,2,2]]
faceRColors = [[3,3,3],[3,3,3],[3,3,3]]
faceFColors = [[4,4,4],[4,4,4],[4,4,4]]
faceBColors = [[5,5,5],[5,5,5],[5,5,5]]

def SayColor(rgb):
	# absWhite=rgb[0]>150 and rgb[1]>150 and rgb[2]>150
	# relWhite=abs(rgb[0]-rgb[1])+abs(rgb[1]-rgb[2])<10
	# absYellow=rgb[0] and rgb[1] and rbg[2]
	# relYellow=
	# absBlue=rgb[0] and rgb[1] and rbg[2]
	# relBlue=
	# absOrange=rgb[0] and rgb[1] and rbg[2]
	# relOrange=
	# absGreen=rgb[0] and rgb[1] and rbg[2]
	# relGreen=
	# absRed=rgb[0] and rgb[1] and rbg[2]
	# relRed=

	# if absWhite and relWhite:
	# 	return 0
	# elif absYellow and relYellow:
	# 	return 1
	# elif absRed and relRed:
	# 	return 2
	# elif absOrange and relOrange:
	# 	return 3
	# elif absBlue and relBlue:
	# 	return 4
	# elif absGreen and relGreen:
	# 	return 5
	# else:
	# 	return none
	return 0
	

def ColorPicker(box):
	original.show()
	cropped = original.crop(box)
	w,h = cropped.size
	pixels = cropped.getcolors(w*h)
	mostFrequent = pixels[0]
	cropped.show()
	for count, color in pixels:
		if count > mostFrequent[0]:
			mostFrequent = count,color
	pallet = Image.new("RGB",(200,200),mostFrequent[1])
	pallet.show()
	# return SayColor(mostFrequent[1])

ColorPicker(faceUSquares[1])

# print(ColorPicker(faceUSquares[1]))



