# AlbumArtCollageMaker
Python app to generate color-sorted collages from square images such as album art
# Usage:
Run app from GUI.py

Have a folder ready filled with the images you wish to use for your collage (currently .png and .jpg only!)
(If image is not square, it will be resized to a square)
Select that folder from the first browse
Select an output folder from the second for the final image
Give your collage a file name (NOTE: THERE IS CURRENTLY NO OVERWRITE WARNING SO MAKE SURE YOU USE A UNIQUE NAME!)
Choose a desired ratio for your output image

Options:
Perfect Ratio checkbox will perform one of to methods to return an image with exactly the desired ratio.
If this is not selected, the program will find the closest ratio that can be generated with the number of images you have.
Stretch method is currently not working.
Fill method will randomly insert black squares into the collage to add enough tiles to perfect the ratio
Color sort method will change how the program sorts your images in the collage (Just play around and see what you like!)
Subimage size determines how big each individual image will be in the collage. By extension this determines the overall output size. Be careful with many images not to make this too large or the app may run out of memory and crash!

Select "Run" to output the image

Example outputs can be found in repo

# TODO
- Fix stretch functionality
- Add color interpolation for fill method
- Add user warnings to GUI and implement error handling
