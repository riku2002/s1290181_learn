import pandas as pd
import re

class frequenciesOfItems:
    def __init__(self, inputFile, sep='\t'):
        self.inputFile = inputFile
        self.sep = sep

    def getFrequencies(self):
        # Initialize an empty dictionary to store item frequencies
        item_frequencies = {}

        # Read the data from the input file into a DataFrame using pandas
        df = pd.read_csv(self.inputFile, sep=self.sep)

        # Extract the coordinates pattern from the column names using regex
        # For example, "Point(12.34 56.78)" is a pattern we want to find
        coordinate_pattern = re.compile(r'Point\(\s*-?\d+\.\d+\s*-?\d+\.\d+\s*\)')

        # Iterate through each row in the DataFrame
        for row_idx in range(len(df)):
            # Find all coordinate patterns in the current row and store them in a list
            coordinate_list = coordinate_pattern.findall(str(df.iloc[row_idx]))

            # Iterate through each coordinate in the list
            for coordinate in coordinate_list:
                # Check if the coordinate exists in the item_frequencies dictionary
                if coordinate in item_frequencies:
                    # If it exists, increment its frequency by 1
                    item_frequencies[coordinate] += 1
                else:
                    # If it doesn't exist, add it to the dictionary with frequency 1
                    item_frequencies[coordinate] = 1

        # Return the dictionary containing item frequencies
        return item_frequencies
