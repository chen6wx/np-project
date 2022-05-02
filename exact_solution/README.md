You run the test file by calling bash run_test_cases.sh

This file consists of calling this command on each txt file:
time python3 exact_solution.py < test_cases/test10nodes.txt (for exact solution) &
time python3 ../approx_solution/approx_solution.py < test_cases/test10nodes.txt (for approximate solution)
