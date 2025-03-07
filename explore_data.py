import time
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# formating
matplotlib.rc('xtick', labelsize=5)
matplotlib.rc('ytick', labelsize=5)

def visualize_explore(examples, title=""):
    """
    :param examples: list of all pairs of arc examples. That is a list of dictionaries
        where each element is a dictionary with keys 'input' and 'output' and double array values representing
        an input and output pair int eh arc dataset
        [{'input'[[], ..., []], 'output:[[], ...[]]}, ..., {'input'[[], ..., []], 'output:[[], ...[]]}]
    :param title:
    :return: nothing is returned

    This method should save 400 plots in a plots directory. The plots should look
    like the example plot in the README file
    """
    fig, ax = plt.subplots(len(examples), 2)
    fig.set_size_inches(10, 6)
    index = 0
    for example in examples:
        input = example["input"]
        output = example["output"]

        # TODO color each of the cells in the input matrix using matshow
        # ax[index, 0].matshow(input, cmap='tab20c', vmin=0, vmax=9)

        for k, matrix in enumerate([input, output]):
            if ax.ndim == 1:
                current_ax = ax[k]
            else:
                current_ax = ax[index, k]
            current_ax.matshow(matrix, cmap='tab20c', vmin=0, vmax=9)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    current_ax.text(j, i, str(matrix[i, j]), va='center', ha='center', color='black')

        index += 1
    fig.suptitle(title)
    # TODO save plot to ./plots/<title> , where <title> is title passed to method
    fig.savefig(f'./plots/{title}.png')
    plt.close(fig)


