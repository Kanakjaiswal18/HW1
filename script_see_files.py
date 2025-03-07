from data_loader import *
from explore_data import *

# Replace 'your_directory_path' with the path of the directory you want to walk
training_json = walk_files('./data/training')
evaluation_json = walk_files('./data/evaluation')
count = 0
# get the data in a usable format
for example in training_json:
    print(f"example_{count}")
    examples = get_example_train_elements(example)
    visualize_explore(examples, f"example_train_{count}")
    count += 1

    # TODO get this to work
    examples = get_example_test_elements(example)
    visualize_explore(examples, f"example_test_{count}")
    count += 1