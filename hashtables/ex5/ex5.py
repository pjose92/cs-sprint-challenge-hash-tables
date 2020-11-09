# Your code here
import os

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #need to loop files base name to see if there is a match 
    index = {}
    result = []
    for query in queries:
        index[query] = 1
    for file in files:
        if os.path.basename(file) in index:
            result.append(file)

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
