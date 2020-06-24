import textwrap

def wrap(string, max_width):
    result=''
    for i in range(0,len(string),max_width):
        result=result+string[i:i+max_width]
        result=result+'\n'
    return result
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)