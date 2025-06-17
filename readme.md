# DYNAMIC COLLAGE MAKER
#### Video Demo:  https://youtu.be/5-9P0ZREPeI
#### Description:

#**Dynamic Collage Maker**
### The dynamic collage maker uses [Google Image Search API](https://pypi.org/project/Google-Images-Search/) to conduct a search of a user inputted term to save a user defined amount of images (evenly divisible) into a collage automatically.
Using the math library, the image count is then used in a number of calculations to determine canvas size, and image placement  the canvas itself this why it had to be evenly divisible divides it into rows and columns depending on how many images there are and then it assigns each image to the center of that and then offsets it by a random amount within 100 pixels of the center using the random Library.

#to use the Dynamic Collage Maker, first run pip install requirements.txt in the root folder
## then, run python project.py SEARCHQUERY NUMBER
### SEARCHQUERY should be your search term for the images, the program will find random ones from the google image search API that match your search term
### NUMBER should be a digit 4, 16, etc, which is evenly divisible. The program will send you back to the input stage if it isn't

##After that, all that's left to do is sit back and relax while it generates your image, which will be in the root folder as output.png
images used in the collage are stored in the images folder for easy cleanup, but will be overwritten by subsequent image generations
BE SURE TO DOWNLOAD your collage when done!


#Some interesting challenges I ran into:
### File names: The length of the filenames on some images are too long to save, so I implemented a function that renames them when it resizes them to 500x500px, so they're instead img1-imgX, with X meaning the total number of images
### Debugging with a global variable. To make things easier initially, the user input for the total number of images is a global variable defined as an int of sys.argv[2], but when debugging I had to call a mock variable to fill in for it, which proved more difficult than I thought, in the future I wouldn't use a global variable in this manner
### amusing results: In the test video putting in the one word search of pyramids results in some random conspiracy related images, which I found quite amusing.

## Overall I'd say my program fulfills my original specifications, which were as follows:
###My final project will be a dynamic image collage maker that creates a dynamic collage based on user input. The main function would prompt the user for input and manage the flow of the program. Additional functions will be retreiving images from an external API, overlaying them in a collage layout, and then saving the collage to a file.