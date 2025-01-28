# try :
#     print("File Opening Code.")
# except Exception as e:
#     print(e)
# finally:
#     print("File Closing Code")
    

# try:
#     print(10/0)
# except Exception as e:
#     print(e)
# finally:
#     print("Finally Code Executed")
    

# try:
#     print(10/0)
# except FileNotFoundError as f:
#     print(f)
# finally:
#     print("Finally Code Executed")

# try:
#     print(1)
#     print(2)
#     print("File open code")
#     print(4)
#     print(10/0)
#     print("File close code")
# except FileNotFoundError as f:
#     print(f)
# finally:
#     print("Finally Block Executed")
    

# try:
#     print(1)
#     print(2)
#     print("File open code")
#     print(4)
#     print(10/0)
    
# except FileNotFoundError as f:
#     print(f)
# finally:
#     print("File close code")


# '''  If we forcefully shutdown the PVM then finally block not executed  '''
# # If we will forcefully shutdown PVM

# import os
# try :
#     print(1)
#     print("File open code")
#     os._exit(0)
#     print(3)
# except Exception as e:
#     print(e)
# finally:
#     print("Finally Block.")


''' Finally with function return statement.  '''

def sample():
    try:
        print(1)
        return "Hellooo!!!"
        print(3)
    except Exception as e:
        print(e)
    finally:
        print("Finally block executed")
print(sample())