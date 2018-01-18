'''找到具体错误的方法如下'''
try:
    data = open('missing.txt')
    '''打开一个不存在的文件'''
    print(data.readline(),end='')
#except IOError:
except IOError as err:
    '''为异常对象给定一个名'''
    #print('File error:')
    #print('File error:'+err)
    '''更改代码将其作为错误信息的一部分，输出后会出现另一个异常'''
    print('File error:'+str(err))
    '''可能异常对象和字符串不兼容，需使用str()BIF将其强制转换为字符串。修改代码输出后会得到一个特定的错误，从而得知错误具体位置'''
finally:
    if 'data' in locals():
        '''文件不存在时就无法调用close()方法，需使用locals()BIF返回当前作用域定义的集合中查找data名是否存在'''
        data.close()
        '''此时会有File error，没有其他异常。但具体错误并不知道，需要修改except组的代码'''
