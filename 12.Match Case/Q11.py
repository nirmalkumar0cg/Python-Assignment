# Q11. File Type Detector
# Take a file extension as input:

# pdf
# jpg
# png
# mp3
# mp4
# Display the type of file.

user_input = input('Enter The File Extension: ')

match user_input:
    case 'pdf':
        print('Document')
    case 'jpg':
        print('Image')
    case 'png':
        print('Image')
    case 'mp3':
        print('Audio')
    case 'mp4':
        print('Video')
    case _:
        print('Unknown File Type')