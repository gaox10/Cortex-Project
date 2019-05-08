import json

def main():
	with open('test.json') as f:
		data = json.load(f) #Here is the line that is throwing the 
							#error, something to do with unicode. Try
							#messing around in the JSON and with 
							#encodings/decodings to get it to read in
	print('Done')
		
if __name__ == '__main__':
	main()
	
'''Outline of the Data
pageName - Insta page name
extPostId - ID number
rawText - Actual string text of the post
extCreatedAt - datetime timestamp of posting
postLink - web address
metadata
	language
	keywords
	hashtags
	imgWidth
	imgHeight
	imageColors
	imageTags
	imageObjects - multiple identical objects
	imagePHash
nFollowers - number of followers
nComments - number of comments
nLikes - number of likes'''
	
