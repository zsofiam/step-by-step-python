import matplotlib.pyplot as plt
import random


def linear_search_steps(haystack, needle):
    # TODO: implement the function
    return -1


def binary_search_steps(haystack, needle):
    # TODO: implement the function
    return -1

# You do not need to edit the code below, but feel free to see what it does!

def get_average_steps(max_num, search_type, tries=100):
    haystack = range(1, max_num)
    steps = []
    for _ in range(tries):
        needle = random.randint(1, max_num)
        if search_type == "LINEAR":
            steps.append(linear_search_steps(haystack, needle))
        elif search_type == "BINARY":
            steps.append(binary_search_steps(haystack, needle))
    return sum(steps) / tries


def pretty_print_numbers(numbers, format, title, title_len):
    print(title.ljust(title_len) + ' '.join([f"{n:{format}}" for n in numbers]))


def plotter(domain, datasets, colors, labels, title, axis_labels, axis_scales):
    for i in range(len(datasets)):
        plt.plot(domain, datasets[i], color=colors[i], label=labels[i])
    plt.title(title)
    plt.xlabel(axis_labels['x'])
    plt.ylabel(axis_labels['y'])
    plt.xscale(axis_scales['x'])
    plt.yscale(axis_scales['y'])
    plt.legend()
    plt.show()


def step_by_step(points):
    range_spans = [10**n for n in range(1, points + 1)]  # create list [10, 100, 1000, ...]
    avg_steps_linear = [get_average_steps(max_num, "LINEAR") for max_num in range_spans]
    avg_steps_binary = [get_average_steps(max_num, "BINARY") for max_num in range_spans]

    pretty_print_numbers(range_spans, '9', 'Range', 20)
    pretty_print_numbers(avg_steps_linear, '9.2f', 'Avg steps (linear)', 20)
    pretty_print_numbers(avg_steps_binary, '9.2f', 'Avg steps (binary)', 20)

    plotter(range_spans,
            (avg_steps_linear, avg_steps_binary),
            ('r', 'g'),
            ('Linear search', 'Binary search'),
            title='Average steps needed in a guessing game',
            axis_labels={'x': 'Size of the numbers range', 'y': 'Average steps needed'},
            axis_scales={'x': 'linear', 'y': 'linear'})  # use 'linear' or 'log'


if __name__ == '__main__':
    step_by_step(5)
