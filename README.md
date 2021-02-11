# Step by step

## Story

You got into an argument with your father about the number guessing
game: you claim that guessing a chosen number from `1` and `1000` takes
only a few more turns on the average than guessing a number between `1`
and `100`. Your father says that it is impossible since it has ten times
more numbers to think of.

You say that it does not matter since you can _exclude_ numbers.

He says of course, but `999` options need to be excluded instead of
`99`, so again, it needs ten times more effort.

You start to explain something about the role of _ordering_ in the range
of numbers, _halving_ the intervals, and then about something called
_binary search_, and _logarithms_, but your father just shakes his head
with disbelief.

Who is right? You decide to write some code that counts average guessing
steps and shows some fancy chart that helps to convince your father. You
plan to include the "brute force" solution as well (the so-called
_linear search_ which basically tries all numbers one-by-one).

## What are you going to learn?

- improve your algorithmic skills
- learn about the visualization of algorithmic behavior
- learn about the logarithmic function :)

## Tasks

1. Implement the `linear_search_steps` function that counts and returns the number of "guesses" made when looking for a number (`needle`) in a list (`haystack`). The list may be unordered.
    - The return value is between `1` and the size of `haystack`. If `needle` is not found, the result is the latter.
    - Running the average counter function (included) with `search_type='LINEAR'`, the averages of the guess numbers are proportional to the list size. Example: the result of `get_average_steps(100, 'LINEAR')` is around `50`, and the result of `get_average_steps(1000, 'LINEAR')` is around `500`.

2. Implement the `binary_search_steps` function that counts and returns the guesses made when looking for a number (`needle`) in an ordered list (`haystack`).
    - The return value is between `1` and the size of `haystack`. If `needle` is not found, the result is the latter.
    - Running the average counter with `search_type='BINARY'`, the averages of the guess numbers are proportional to the logarithm of the list size. Example: the result of `get_average_steps(100, 'BINARY')` is around `5`, and the result of `get_average_steps(1000, 'BINARY')` is around `9`

3. The program renders a chart plotting the two datasets. Upon calling the `plotter` function, it can be set what kind of scale the axes are measured on, linear or logarithmic. Choose which combination of the scales is the best for you in order to show the differences! You can choose between a linear/linear, linear/logarithmic, logarithmic/linear, and logarithmic/logarithmic scale combinations. Try to examine each option, choose the best one for your arguments, and save it into the file named `scale.txt`!
    - The file `scale.txt` contains one of the following scale combinations: `linear/linear`, `logarithmic/logarithmic`, `linear/logarithmic`, `logarithmic/linear`

## General requirements

None

## Hints

None

## Background materials

- <i class="far fa-exclamation"></i> [About linear search](https://www.geeksforgeeks.org/linear-search/)
- <i class="far fa-exclamation"></i> [About binary search](https://www.geeksforgeeks.org/binary-search/)
- <i class="far fa-candy-cane"></i> About [logarithmic scales](https://www.khanacademy.org/math/algebra-home/alg-exp-and-log/alg-logarithmic-scale/v/logarithmic-scale?modal=1)
