# Pre defined variables in Python
# In Python, there are several pre-defined variables that are automatically available for use   
# These variables include:
# __name__: The name of the current module. If the module is being run as the main program, this variable will be set to "__main__".
# __file__: The path to the current file.
# __doc__: The docstring of the current module, class, method, or function.
# __package__: The name of the package that the current module belongs to.
# These variables can be useful for various purposes, such as determining the context in which a module is being run or accessing documentation.
# For example, you can use the __name__ variable to check if a module is being  
# run as the main program or imported as a module:
if __name__ == "__main__":
    print("This module is being run as the main program.")  
else:
    print("This module is being imported as a module.")     

