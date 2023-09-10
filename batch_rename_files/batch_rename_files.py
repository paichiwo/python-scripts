import os

directory = "images/"   # Replace with the path to the directory containing the files
substring = "Wisielec"          # Replace with the substring to remove from the file names

for filename in os.listdir(directory):
    if substring in filename:
        new_filename = filename.replace(substring, "Hangman")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
