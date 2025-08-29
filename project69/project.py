def log():
    n = input("Enter your name: ").lower()  # `str()` is redundant (input() returns a string)
    r = input("Enter your roll number: ")
    log_data = {"name": n, "roll number": r}  # Use {} for dictionaries
    return log_data  # Return the data for use in other modules
 