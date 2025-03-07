# README: HW1

## Project Overview
This project loads, processes, and visualizes data from the **Abstraction and Reasoning Corpus (ARC)** dataset. The workflow involves:
1. **Loading JSON data** from the dataset.
2. **Processing the data** into numpy arrays.
3. **Visualizing input-output examples** using matplotlib.
4. **Saving visualized plots** for further analysis.

## File Descriptions
### 1. `data_loader.py`
This script is responsible for loading and processing data.
- **`walk_files(directory)`**: Recursively loads JSON files from the given directory.
- **`get_example_train_elements(json_example)`**: Converts training data to numpy arrays.
- **`get_example_test_elements(json_example)`**: Converts test data to numpy arrays.
### 2. `explore_data.py`
This script visualizes the dataset.
- **`visualize_explore(examples, title="")`**:
  - Generates a **side-by-side** plot of input and output matrices.
  - Saves plots in the `./plots/` directory with filenames based on the title.
### 3. `script_see_files.py`
Main script that:
- Loads **training** and **evaluation** data.
- Converts JSON data into numpy format.
- Generates and saves visualizations for training and test sets.

## How to Run the Code
Execute the main script with:
```sh
python script_see_files.py
```
This will:
- Load and process data from `./data/training`.
- Generate and save visualizations in `./plots/`.
- The plots will be saved as `example_train_<index>.png` and `example_test_<index>.png`.

