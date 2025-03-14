class HelloWorld:
    def __init__(self):
        self.message = "Hello World"
    
    def display_message(self):
        print(self.message)

# Create an instance and call the display method
if __name__ == "__main__":
    hello = HelloWorld()
    hello.display_message()
