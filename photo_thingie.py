import random
import json


# read object from json
def read_json(filename):
    with open(filename, "r") as f:  # open the file
        contents = f.read()  # read the contents
        objects = json.loads(contents)  # load the json
        return objects


# print selected random object
def assemble_message():
    lists = read_json("/Users/hollylemos/Projects/photo_them_sample.json")
    perspective = random.choice(lists['perspective'])
    object = random.choice(lists['object'])
    condition = random.choice(lists['condition'])
    # print(condition, object, perspective)
    print("Take a {0} photo of a {1} from a {2} perspective".format(condition, object, perspective))

assemble_message()
