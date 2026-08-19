def uppercase(fuc):
    def wrapper(*args,**kwargs):
        result=fuc(*args,**kwargs)
        return result.upper()
    return wrapper
@uppercase
def get_message():
    return 'hello python'

if __name__=='__main__':
    print(get_message())
