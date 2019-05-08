import json
import csv
import textstat

def main():
	with open('visit_utah_updated_01_19.json', mode = 'r', encoding = 'utf-8') as f: #Open the data that is in a json file and load it into data
		data = json.loads(f.read(), encoding = 'utf-8')
	#Goals
	#1. Add in the engagement data
	#2. Add data and follower data?? Joins
	#3. Figure out "most popular" model
	#4. Emoji data??
	imagetags = set()
	hashtags = set()
	imageobjects = set()
	imagecolors = set()
	keywords = set()
	for photo in data: #Get the column names
		md = photo['metadata'] #The photo's metadata
		tags = md['imageTags'] #The photo's image tags by the API
		ht = md['hashtags'] #The photo's hash tags by the user
		objects = md['imageObjects'] #Objects in the photo found by the API
		colors = md['imageColors'] #The 3 main colors in the photo found by the API
		words = md['keywords'] #Main words in the photo's user caption found by the API
		fieldnames = ['PageName', 'PostID', 'Readability', 'PostTime', 'Height', 'Width', 'PHash']
		for tag in tags:
			imagetags.add(tag['value'])
		for tag in ht:
			hashtags.add(tag)
		for object in objects:
			imageobjects.add(object['name'])
		for color in colors:
			imagecolors.add(color['value'])
		for word in words:
			keywords.add(word)
	with open('Data.csv', 'w', newline = '') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		length = 10+len(imagetags)+len(hashtags)+len(imageobjects)+len(imagecolors)+len(keywords)
		for tag in imagetags:
			fieldnames.append(tag)
		for tag in hashtags:
			fieldnames.append(tag)
		for objects in imageobjects:
			fieldnames.append(objects)
		for color in imagecolors:
			fieldnames.append(color)
		for word in keywords:
			fieldnames.append(word)
		fieldnames.append('Followers')
		fieldnames.append('Comments')
		fieldnames.append('Likes')
		writer.writerow(fieldnames)
		for photo in data: #Get the data out with the associated column name
			photodata = list(['0']*length)
			md = photo['metadata'] #The photo's metadata
			tags = md['imageTags'] #The photo's image tags by the API
			ht = md['hashtags'] #The photo's hash tags by the user
			objects = md['imageObjects'] #Objects in the photo found by the API
			colors = md['imageColors'] #The 3 main colors in the photo found by the API
			words = md['keywords'] #Main words in the photo's user caption found by the API
			photodata[0] = photo['pageName']
			photodata[1] = photo['extPostId']
			photodata[2] = textstat.text_standard(photo['rawText'], float_output=False)
			photodata[3] = photo['extCreatedAt']
			photodata[4] = md['imgHeight']
			photodata[5] = md['imgWidth']
			photodata[6] = md['imagePHash']
			i = 7
			for tag1 in imagetags:
				for tag2 in tags:
					if tag1 == tag2:
						photodata[i] = tag['confidence']
						break
				i = i+1
			for tag1 in hashtags:
				for tag2 in ht:
					if tag1 == tag2:
						photodata[i] = 1
						break
				i = i+1
			for object1 in imageobjects:
				for object2 in objects:
					if object1 == object2:
						photodata[i] = objects['conf']
						break
				i = i+1
			for color1 in imagecolors:
				for color2 in colors:
					if color1 == color2:
						photodata[i] = colors['confidence']
						break
				i = i+1
			for word1 in keywords:
				for word2 in words:
					if word1 == word2:
						photodata[i] = 1
						break
				i = i+1
			photodata[length-3] = photo['nFollowers']
			photodata[length-2] = photo['nComments']
			photodata[length-1] = photo['nLikes']
			writer.writerow(photodata)
	print('Done')

if __name__ == '__main__':
	main()
	
	#The number of likes? engagement? Derived Variables?
	'''Preliminary searchs
	249 images in the data set
	each image has 3 main categories
		extPostId - An ID number (External post ID - used by instagram)
		postLink - A link to the instagram post in question
		metadata - The actual data
	Metadata consists of 9 attributes
		imgWidth - int, width of the image in pixels
		language - unicode, they all say en which I bet means English, kinda obvious (most stuff will be in English)
		(can repeat??)imageTags - list of dictionaries, variable length, all the tags the API found in the image, number and value of tags can vary among different pictures, around 10 or all of them
			confidence - float, 0-1, a guess at how accurate the value is, percentage
			value - unicode, a tag the API has detected in the image
		hashtags - list, the list of tags placed on the image by the user
		imageObjects - list of dictionaries, variable length, objects found in the image by the API
			??vertexes - list of dictionaries, the corners that make a box around the object
				x - int, pixel location
				y - int, pixel location
			name - unicode, an object
			conf - float, 0-1, a guess at how accurate that object is in that location????
		imageColors - list of dictionaries, the main three colors found (can be changed for more colors) in each photo (mapped into 200 color dimension space, web colors?)
			color - unicode, the english name of the color
			confidence - float, percentage of the color found in the image
			value - unicode, the hexcode for the color
		imagePHash - int, duplicate detection, can handle resizing and color changes, looks at structure of the image
		keywords - list of unicode, variable length, a subsection of the words used in the caption.  The API seems to remove certain words like and and to (conjections, prepositions).
			The words should be cleaned?
		imgHeight - int, height of the image in pixels'''
	#The layer - the vector taken right before ML classification.  This vector manages to capture both tag and pixel data.  Need to read more on this (Similar to reverse image search)
		
