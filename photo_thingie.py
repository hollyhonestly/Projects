from argparse import ArgumentParser
import random
import json


def read_json(filename):
    with open(filename, "r") as f:  # open the file
        contents = f.read()  # read the contents
        objects = json.loads(contents)  # load the json
        return objects


def assemble_message(lists):
    perspective = random.choice(lists['perspective'])
    object = random.choice(lists['object'])
    condition = random.choice(lists['condition'])
    return "Take a {0} photo of a {1} from a {2} perspective".format(condition, object, perspective)


def parse_args():
    parser = ArgumentParser(description='Provides inspiration for photography')
    parser.add_argument('inspiration_file', type=str, help='path to json file')
    return parser.parse_args()


def main():
    # ORIGINAL FILE = '/Users/hollylemos/Projects/photo_them_sample.json'
    args = parse_args()
    file_name = args.inspiration_file
    loaded_json = read_json(file_name)
    print(assemble_message(loaded_json))

if __name__ == '__main__':
    main()
