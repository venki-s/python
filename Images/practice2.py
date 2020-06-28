from PIL import Image
import os

word = Image.open(os.getcwd()+'/word_matrix.png')
mask = Image.open('mask.png')

mask = mask.resize(word.size)

mask.putalpha(200)

word.paste(mask,(0,0), mask)

word.show()