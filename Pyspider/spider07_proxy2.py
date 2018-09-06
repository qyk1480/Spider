import urllib.request

user =
pwd =
# proxyserver =
webserver =

# 创建密码管理对象，保存授权信息
passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# passwdmgr.add_password(None, webserver, user, pwd)


# 授权代理处理器
proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdmgr)
opener = urllib.request.build_opener(proxyauth_handler)
request = urllib.request.Request(url)
response = opener.open(request)


opener = urllib.request.build_opener(proxyauth_handler, httpauth_handler)


passwdmgr.add_password(None, webserver, user, pwd)

# 验证web客户端的授权处理器
httpauth_handler = urllib.request.HTTPBasicAuthHandler(passwdmgr)
opener = urllib.request.build_opener(httpauth_handler)
request = urllib.request.Request(webserver)
response = opener.open(request)

print(response.read())
