#_*_ coding:utf-8 _*_
import getpass
name = "wlf"
pwd = "123456"
count = 0
while count < 3:
	inputname = raw_input("请输入姓名：")
	inputpwd = getpass.getpass("请输入密码：")
	if inputname == name and inputpwd == pwd:
		print "欢迎！ wlf！"
		break
	else:
		print "用户名或密码错误！请重试！"
		count = count + 1
if count >=3:
	print "尝试已超过3次！"
