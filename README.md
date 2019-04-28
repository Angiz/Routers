# Routers
# Project made for cource Artifical Intelligence (Computer Science, second year, second semester)

Necessary libraries:
- environment Python 3.x
- pip
- library NumPy
- library csv for exporting a file

Instruction of installation:
If you don't have Python environment on your computer, you can download it from https://www.python.org/downloads/. The most comfortably way to execute a program is installation of PyCharm, available here: https://www.jetbrains.com/pycharm/download/#section=windows. Version Commnity is free of charge. Firstly, open a file named RoutersConnection.py. Next, Settings -> Project: <name of project> -> Project Interpreter. Then we see a list with already installed libraries. We can add more by clicking "+" and searching for particular libraries. Installation by console is also possible, however is more complicated. We run a project by clicking "run". 
  
Acting of program:
Program gets from user number of routers and stations. If user set invalid parameters, the program catches an exception. Next in loop we add stations, routers and bandwidths. If bandwidth is greater than zero, ten value is considered as correct - analogical is assigned. If bandwidth is equal zero, program assigns to it a big number, in order to exclude it from competition to the shortest path. If bandwidth is lesser than zero, the program catches ValueError exception and the program ends. Next we assign a bandwidth to station according to rules of probability - how many possibilities we have to connect routers with stations? Parameters for array "Stations" works analogical like array "Routers". Next the programf counts imaginary weight given as a vector. It connects bandwidth, time of connection with router and distance between station and router. Next two identical matrices are created. First is examined by Algorithm Dijkstra and second is created by NumPy and it used for be displayed and transposed to text file. In matrix values are assigned by rule that first value is a value between first station and first router, second value - between second station and first router etc. 
