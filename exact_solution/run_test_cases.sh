#!/bin/bash

time python3 exact_solution.py < test_cases/test2nodes.txt
time python3 exact_solution.py < test_cases/test3nodes.txt
time python3 exact_solution.py < test_cases/test5nodes.txt
time python3 exact_solution.py < test_cases/test7nodes.txt
time python3 exact_solution.py < test_cases/test10nodes.txt
time python3 exact_solution.py < test_cases/test15nodes.txt
time python3 exact_solution.py < test_cases/test20nodes.txt
time python3 exact_solution.py < test_cases/test21nodes.txt
time python3 exact_solution.py < test_cases/test22nodes.txt
time python3 exact_solution.py < test_cases/test23nodes.txt
time python3 exact_solution.py < test_cases/test24nodes.txt
#time python3 exact_solution.py < test_cases/test25nodes.txt
#time python3 exact_solution.py < test_cases/test26nodes.txt
#time python3 exact_solution.py < test_cases/test27nodes.txt
#time python3 exact_solution.py < test_cases/test28nodes.txt

time python3 ../approx_solution/approx_solution.py < test_cases/test2nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test3nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test5nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test10nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test15nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test20nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test21nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test22nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test23nodes.txt
time python3 ../approx_solution/approx_solution.py < test_cases/test24nodes.txt
#time python3 ../approx_solution/approx_solution.py < test_cases/test25nodes.txt
#time python3 ../approx_solution/approx_solution.py < test_cases/test26nodes.txt
#time python3 ../approx_solution/approx_solution.py < test_cases/test27nodes.txt
#time python3 ../approx_solution/approx_solution.py < test_cases/test28nodes.txt
$SHELL
