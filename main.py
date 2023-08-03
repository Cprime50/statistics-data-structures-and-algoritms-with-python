# PLEASE PIP INSTALL PSYCOPG2-BINARY BECUASE OF OUR POSTGRES DB UNLESS THIS WILL NOT RUN

#parsing the data of colour of clothes worn on each weekday from our html file to a dictionary
data = {
    'Monday': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'Tuesday': 'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE',
    'Wednesday': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE',
    'Thursday': 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'Friday': 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE',
}

#Question (1).
''' What colour is the mean colour? This is quite tricky because 
mean = sum of colours/length of colours, since our colours are strings and we cannot sum strings, there can't be a mean colour,
although we can store the colours in a list and use the indexes of each colour to get a sum and then divide that sum by the length of the list'''

def find_mean_colour(colours_str):
    colours_list = colours_str.split(', ')          #parse the colors into a list, sepearting each by a comma
    colour_length = len(colours_list)               #finding length of list with len func

    total_sum = sum(index for index, _ in enumerate(colours_list)) #Here i use enumearte a python function to generate the indexes of a list, I then iterate through the indexes and store each iteration as an index value which gets summed with the next index value until the final iteration
    mean = total_sum/ colour_length
    return mean
mean_colour = find_mean_colour(', '.join(data.values()))
print("The Mean of the colours is:", mean_colour)


#Question (2).
'''   Which color is mostly worn throughout the week?
 The answer this question I will need to find the mode of the colours'''

#Creating an algoritm for calculating the mode colour of shirts based on the frequency at which the colour is worn
def find_mode_colour(colours_str):
    colours_list = colours_str.split(', ')        #parse the colors into a list, sepearting each by a comma
    colour_counts = {}                              #creating a dictionary to hold counts of each colour
    for colour in colours_list:                     #creating a for loop to iterate through the colours in the colours_list
        colour_counts[colour] = colour_counts.get(colour, 0) + 1            # checking each colour in our colour_counts dictionary. If the color is not present in the dictionary, it returns 0 as the default value of that colour, then if that colour is counted again it increments its value by 1    

    most_common_colour = max(colour_counts, key=colour_counts.get)          #using the python max function to get the clour with maximum value from the colour_counts dictionary and storing it in the  most_common_color variable
    mode_colour = most_common_colour                              

    return mode_colour

mode_colour = find_mode_colour(', '.join(data.values()))
print("Colour mostly worn throughout the week is:", mode_colour)


#Question (3).
'''   Which color is the median?
the median is the middle index in our list, here i will write a function to sort the list in ascending order,
 removing all dupicates then checking for the length of the list, if the list lenght is even the our median should be addition of both middle 
 indexes/2 but we cant add and divide strings so I will just output both even indexes if odd It will output only the middle index
 '''

#creating a function to calculate the median of the list of colours
def find_median_colour(colours_str):
    #gathering data from the dictionary and storing in a list
    colours_list = colours_str.split(', ')

    #sorting the colours and removing duplicate using the python sorted function
    sorted_colors = sorted(set(colours_list))

    median_index = len(sorted_colors) // 2              #getting length of sorted colours using len function then getting the integer division of the number by 2 to find the middle number
    if len(sorted_colors) % 2 == 0:                     #checking if the length of sorted colors is even cus even numbers will have 2 middle numbers
        median_colour = sorted_colors[median_index], sorted_colors[median_index + 1]                # if even then our median colour will be both middle numbers normally we add them both and divide by 2 but in this situation they are strings
    else:
        median_colour = sorted_colors[median_index]                                     #if odd then outputs the middle number
    
    return median_colour

median = find_median_colour(', '.join(data.values()))
print('The median of the colour is:', median)

#Question (4).
'''  Get the variance of the colors?
 to get the variance I need to get the deviations  which is the  difference between each color's occurent rate and the mean of all colours, then square each deviations and calculate their average.'''

def find_variance_colour(colours_str):
    colours_list = colours_str.split(', ')
    colour_length = len(colours_list)

    # This is the Mean of the colours I calculated earlier
    mean = find_mean_colour(colours_str)

    # square the deviations
    colour_counts = {}
    for color in colours_list:
        colour_counts[color] = colour_counts.get(color, 0) + 1

    deviations = [(colour_counts[color] - mean) ** 2 for color in colours_list]

    # find average of deviations to get the Variance
    variance_colour = sum(deviations) / colour_length
    return variance_colour
variance = find_variance_colour(', '.join(data.values()))
print('The variance is:', variance)


#Question (5).
''' if a colour is chosen at random, what is the probability that the color is red??
 counting number of reds and dividing by length of all colors_list'''

def find_probability_red(colours_str):
    colours_list = colours_str.split(', ')
    colour_length = len(colours_list)
    colour_counts = {}
    for color in colours_list:
        colour_counts[color] = colour_counts.get(color, 0) + 1

    probability_red = colour_counts['RED'] / colour_length

    return probability_red

probability_being_red = find_probability_red(', '.join(data.values()))
print('The probability for a random colour picked to be red is:', probability_being_red)






