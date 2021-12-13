#PROJECT A.P.E.

##ALL PHOTOS EVER

_WORK IN PROGRESS_

**Introduction**

Project A.P.E., or All Photos Ever, aims to provide the basis of an image generator which can then be used together with other applications and services. In a nutshell the code creates all possible images based on user defined parameters. To best explain how it works it is easier to simplify the problem. Imagine a 2 X 2 grid, composed of 4 squares which can either be white or black, if we were to randomlly assign a color to each square we would have a total of 2<sup>4</sup> or 16 total images. Now let's expand that grid to a 100 X 100, or even a 1000 X 1000, the number of possible images increases exponentially. Finally, let's change the possible colors, instead of just black and white let's look at all RGB combinations. As we know an RGB color is composed of three inputs, the luminosity for each color: red, green, and blue, ranging from 0 to 255, so 256 possible values for one color, meaning 256<sup>3</sup> or 16,777,216 total colors. Now what the script does is it looks at that grid and for each pixel or 'square' in the grid, it picks a color out of the total possible combination in the RGB range.

**Utilizing the script**

The class uses the following initalizers:

**length** - _The length of the image, or number of colored squares on one side of the square._

**coloring_type** - _Which colors will the image use, can be one of the following: Full (all RGB Colors), BlackAndWhite (only Black and White), Grayscale (gray RGB colors), Grayscale - Red|Green|Blue (gray RGB colors Red|Green|Blue shaded)_


The functions it uses are:

**generate_random_image** - _Creates a random image based on the length and coloring_type provided in the initializers._

**generate_all_images** - _Creates all images possible based on the input initializers._


**Future Work**

Future plans will involve the option to generate an image from a starting point, e.g. half of the pixels in the image are already colored and it will only generate all possible combinations for the remaining ones. Even further work will be to include some machine learning algorithm that can skim through all the images creates and provide images which actually resemble something.