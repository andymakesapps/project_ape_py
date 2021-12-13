import matplotlib.pyplot as plt
import numpy as np
import itertools
import random
import json
import sys
import os


class APEBuilder():
    def __init__(self, length, coloring_type):
        self.length = length
        self.coloring_type = coloring_type
        self.coloring_types = ["Full", "BlackAndWhite", "Grayscale", "Grayscale - Red", "Grayscale - Green", "Grayscale - Blue"]
        self.palette_json_generic_filename = "palette_generic.json"

        if self.coloring_type not in self.coloring_types:
            sys.exit(f"Invalid Coloring type, try one of the following:\n{self.coloring_types}")
        
        print(f"APE Builder has been initalized. Length set to {self.length} and coloring type to {self.coloring_type}")
    
    def generate_colors_array(self, coloring_type):
        '''
        Function used to create all RGB colors.
        Returns an array with all possible color combinations.
        '''
        print(f"Creating Colors Array of type {self.coloring_type}")
        if coloring_type == "Full":
            colors = list(itertools.product([i for i in range(0, 256)], repeat=3))
        elif coloring_type == "BlackAndWhite":
            colors = [(i, i, i) for i in [0, 255]]
        elif coloring_type == "Grayscale":
            colors = [(i, i, i) for i in range(0, 256)]
        elif coloring_type == "Grayscale - Red":
            colors = [(i, 0, 0) for i in range(0, 256)]
        elif coloring_type == "Grayscale - Green":
            colors = [(0, i, 0) for i in range(0, 256)]
        elif coloring_type == "Grayscale - Blue":
            colors = [(0, 0, i) for i in range(0, 256)]
        print("Array has been created with lenght: {}".format(len(colors)))
        return colors

    def create_colors_array_file(self):
        '''
        Function used to generate a json file with all RGP colors.
        The json will contain values for all coloring types. Returns file creation.
        '''
        print("Creating color palette file...")
        palette_json = {}
        for coloring_type in self.coloring_types:
            print(f"Creating values for: {coloring_type} Coloring Type")
            colors = self.generate_colors_array(coloring_type)
            print("Adding values to dictionary.")
            palette_json[coloring_type] = colors

        print("Creating color palette json file...")
        with open(f'palette/{self.palette_json_generic_filename}', 'w') as json_file:
            json.dump(palette_json, json_file)
        print("File has been created")
    
    def update_colors_array_file(self):
        '''
        Function which checks for updates in the color array file.
        '''
        print("Checking for updates to the colors array file...")
        with open(f'palette/{self.palette_json_generic_filename}', 'r') as json_file:
            data = json.load(json_file)
        existing_coloring_types = list(data.keys())
        print(f"Current color types in file: \n\t{existing_coloring_types}")
        new_coloring_types = list(set(self.coloring_types) - set(existing_coloring_types))
        if not new_coloring_types:
            print("No new color types to update.")
        else:
            print(f"Will add the following coloring types: \n\t{new_coloring_types}")
            for coloring_type in new_coloring_types:
                new_colors = self.generate_colors_array(coloring_type)
                data[coloring_type] = new_colors
            with open(f'palette/{self.palette_json_generic_filename}', 'w') as json_file:
                json.dump(data, json_file) 
    
    def check_colors_array_file(self):
        '''
        Function used to check if the palette file exists.
        If it does not it will be created, otherwise nothing will be returned.
        '''
        print("Checking if color palette json file exists...")
        if not os.path.exists(f'palette/{self.palette_json_generic_filename}'):
            print("Color palette file does not exist.")
            self.create_colors_array_file()
        else:
            print("Color palette file exists.")
            self.update_colors_array_file()
    
    def get_colors_array(self):
        '''
        Function that returns the color array based on the coloring type provided.
        If the palette file does not exit, it will be created, otherwise it is updated.
        '''
        print("Getting colors array...")
        if not os.path.exists(f'./palette/{self.palette_json_generic_filename}'):
            print("Could not find palette file.")
            self.create_colors_array_file()
        else:
            print("Palette file exists.")
            self.update_colors_array_file()
        with open(f'palette/{self.palette_json_generic_filename}', 'r') as json_file:
            data = json.load(json_file)
        print("Returning the color array.")
        return data[self.coloring_type]

    def generate_random_image(self, continous=False):
        '''
        Function creates a random image based on inputs.
        If continous is set to True it will keep on generating random images.
        '''
        print("Generating random image...")
        colors_list = []
        colors_array = self.get_colors_array()
        while True:
            for _ in range(0, self.length**2):
                random_number = random.randint(0, len(colors_array)-1)
                colors_list.append(colors_array[random_number])
            print("Array created.")
            self.create_image(colors_list)
            if not continous:
                break
    
    def generate_all_images(self):
        '''
        Function used to generate all images in order for a specific color array.
        '''
        colors_array = self.get_colors_array()
        print(colors_array)
        [self.create_image(colors_subset) for colors_subset in itertools.product(colors_array, repeat = self.length**2)]
    
    def create_image(self, long_color_array):
        '''
        Function which generates the image based on color array inputs.
        First an array is created at random and from that a numpy 2D array. Then an image is generated using numpy and pyplot.
        '''
        colors_array_2d = [long_color_array[i:i + self.length] for i in range(0, len(long_color_array), self.length)]
        nparr = np.array(colors_array_2d)
        print("Numpy array created.")
        plt.imshow(nparr)
        plt.axis('off')
        plt.show()
    
 
def main():
    length = 2
    coloring_type = "BlackAndWhite"
    ape_builder = APEBuilder(length=length, coloring_type=coloring_type)

    ape_builder.generate_random_image()

if __name__ == '__main__':
    main()