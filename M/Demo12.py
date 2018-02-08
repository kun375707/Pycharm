'''使用Cookie'''
#ookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据
#当下次客户访问脚本时取回数据信息，从而达到身份判别的功能
print('Content-Type: text/html')
print('Set-Cookie: name="你好";expires=Wed, 8 Feb 2018 17:30:00 GMT')
print()
print("""
<html>
    <head>
        <meta charset="utf-8">
        <title>你好(nihao.com)</title>
    </head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")
#以上是Cookie的设置会在http头部单独发送