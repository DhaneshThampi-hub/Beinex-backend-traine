'''Create a class for creating and writing data to a text file. The class must have __enter__ and __exit__ 
defined.
__enter__ must use the built in `open` to open the file and set the file pointer to self.
__exit__ must close the file pointer on exit.
If the user entered text contains the word 'bug' then __exit__ must delete the file on exiting.
Or if any exception has occurred, then also __exit__ must delete the file.(remember to close file 
before deleting)
Use a `with` block to execute the logic.'''


class FileContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'w')
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            if exc_type is not None or 'bug' in str(exc_value).lower():
                try:
                    import os
                    os.remove(self.filename)
                    print(f"File '{self.filename}' deleted.")
                except Exception as e:
                    print(f"Error deleting file: {e}")
                    raise

try:
    with FileContextManager('my_file.txt') as file:
        file.write("Hello, world!")
        # Uncomment the line below to simulate an exception
        # raise ValueError("Something went wrong")
except Exception as e:
    print(f"Exception occurred: {e}")
