# np-project
CS412 Final Project
This project will explore an known NP-complete problem and will consist of the following components:

    Problem presentation explaining the problem to be solved and its reduction to another accepted NP-complete problem.
    Exact Solution Code -- develop code that exactly solves the problem.
    Approximation presentation -- show an approximation algorithm for this problem and analyze it.
    Approximation code --  develop code that performs this approximation
    Evaluation of Other Projects  -- you will submit 2 reviews of other projects.   This will include submitting some questions about the project before hand and also providing a review of the project's findings/presentation.

The section below detail each of these components.  
Problem and Group Selection

This is a group project that can have up to 4 members.  You will need to select an NP-complete problem for this project.  You should do some research before just selecting one of these problems to make sure you see a way of doing the approximation, etc.  Ideally, each group would work on a different problem, so, priority will be given to earlier submissions and all problem selections are subject to instructor approval.  

    Max 3-Sat
    Max clique
    Traveling Saleman Problem (TSP) with a complete graph
    Longest Path
    Load Balancing
    Maximum Bin packing
    Min Graph Coloring
    Minimal k-cut
    Max Knapsack
    Max Cut

The section below detail each of these components.  

 
Exact Solution Code

Develop Python code that provides the optimal solution to the problem you are studying.  You must develop test cases of varying sizes and illustrate how the runtime (wall clock) of your program varies for different size input.  Your test cases must include at least one instance that causes your program to run for more than 20 minutes. 

Make sure you cite in the comments of your program ALL external sources used in the development of your code.

Submission 

Create a folder named exact_solution with the GIT repository.  Place your code in this folder including a README file that provides instructions and exact commands to run your code.  Within the exact_solution folder, create a test_cases folder that contains all test cases.  Create a shell script named run_test_cases.sh that executes your program on all test cases.
Problem Presentation

You will be present the problem you are solving in class.  This presentation must include:

            the decision problem being solved and the optimization problem
            Example inputs and outputs
            why the problem is important (some applications that use this problem)
            an explanation of the certifier process being polynomial and the reduction to a known/accepted NP-hard problem 
            explanation of the coded solution your group has created.  
            An analytical (big-O) runtime analysis of your coded solution
            A wallclock (empirical) runtime analysis of your code on your test cases

Submission 

Create a folder named presentations with the GIT repository.  This presentation should use slides in either PowerPoint, Keynote, or Google slides (other slides formats can be requested, but are subject to instructor approval).   The slides (or a file with a link to the google slides) should be placed in the git repository.  Name this presentation problem_presentation with whatever file extension is appropriate. 

 
Approximation Presentation

Present an approximation method for your problem.  You are allowed to use approximation methods developed by others as long as you cite your sources.  In other words, you do not need to design the approximation yourself (but you will need to write it yourself).  This presentation must include:

            pseudocode for the approximation
            analytical run time analysis (big-O) of your approximation algorithm
            lower bound analysis of the problem and the approximation
            plots that illustrate the run-time (wall clock) performance of your exact solution versus the approximation solution on your test cases
            plots that compare the result/solution of your exact solution versus the approximation on your test cases.

Submission 

Within the folder presentation  add a presentation/slides file constructed in PowerPoint, Keynote, or Google slides (other slides formats can be requested, but are subject to instructor approval).   The slides (or a file with a link to the google slides) should be placed in the git repository.  Name this presentation approximation_presentation with whatever file extension is appropriate. 
Approximation Solution Code

Develop Python code that provides an approximation of the solution. 

Rubrics:

    Problem presentation (5 points)
    Code solution (6 points)
    Approximation presentation (5 points)
    Approximation code (8 points)
    Approximation Analysis (6 points)
