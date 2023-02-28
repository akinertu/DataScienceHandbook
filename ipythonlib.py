# IPYTHON
    len? = help(len) # documentation of len function
    square?? #accessing source code
    L.<TAB> #exploration of the contents of objects, modules, and namespaces
    import <TAB> #third-party scripts and modules are visible to your Python
    *Warning? # to list every object in the namespace that ends with Warning
    str.*find*? #looking for a string method that contains the word find
    Ctrl-l #shortcut to lear terminal screen
    Ctrl-c #Interrupt current Python command
    %paste
    %cpaste #opens up an interactive multiline prompt in which you can paste one or more chunks of code
    %run myscript.py #Running External Code
    %timeit L = [n ** 2 for n in range(1000)] #to check the performance of a list comprehension 
    %%timeit #multiple line
    print(In) #keeps track of the commands in order
    print(Out[2]) #a dictionary mapping input numbers to their outputs
    print(_) # prints accessing previous output
    %history -n 1-4 #For accessing a batch of previous inputs at once
    %xmode Plain #to control the amount of information printed when the exception is raised.
    %debug #ipdb, the IPython debugger. type quit to quit the debugging session:
        ipdb> down #down through the stack
        %pdb on #Automatic pdb calling has been turned ON
    %time #Time the execution of a single statement
    %timeit #Time repeated execution of a single statement for more accuracy
        %timeit sum(range(100)) #
        %%timeit # For slower commands,
    %prun #Run code with the profiler
    %lprun #Run code with the line-by-line profiler
    %memit #Measure the memory use of a single statement
    %mprun #Run code with the line-by-line memory profiler
    
    
    