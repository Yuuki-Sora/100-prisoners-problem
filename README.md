# 100-Prisoners-Problem
The files here are used for my final project for the 2020 "Descrete Mathematics" course at Waseda University. 
## What these .py files are 
The file "HPP-Random.py" simulates the situation in which everyone chooses 50 boxes at random, while the file "HPP-Strategy.py" simulates the situation where everyone adopts the "loop" strategy and follows the number in the box. 
## What you'll be able to do
You will be able to change 1) the number of prisoners for each experiment, 2) the total number of experiments within 1 simulation, and 3) the output file name (and location, if you like). Please follow the instructions (added as comments) within each respective .py file for more information. 

Try changing the number of prisoners (for example, to only 1) to see the changes in tendencies for the experiments! 
## How to deal with the outputted files
As for the output files, they're formatted in such a way that they contain number of lines equal to the number of experiments, each with the following format: 

```
x:y
x:y
x:y
... 
```

In the random case, x is the *experiment #*, and y is the ***current number of succeeded experiment*** (where everyone lived). 

In the strategic case, x is the *experiment #*, and y is the ***current total survival rate*** (succeeded/total). 

You'll (hopefully) be able to import this to a spreadsheet software of your choice and plot a graph for the simulations with the outputted text files. 

**Have fun playing around with the codes! :P**
