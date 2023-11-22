import os

# specify the directory you want to change
directory = 'c:\\Users\\jmkin\\PycharmProjects\\CrippleMrOnion2023\\Sprites'

for filename in os.listdir(directory):
    if '_2' in filename:
        new_filename = filename.replace('_2', '')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
