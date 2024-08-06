def print_function(arg):
    def do_generator():
        ind = 1
        for i in range(arg):
            for x in range(i+1):
                if ind <= arg:
                    yield str(i+1)
                    ind += 1
                else:
                    break
    print("".join(do_generator()))

print_function(10)