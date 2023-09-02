#打开Windows窗口（第一界面）
import time
import platform
import random
import os
import shutil
aa=platform.release()
ab=platform.version()
ad=len(ab)

if ad==10:
	ac=float(ab[5:])
else:
	ac=float(ab[5:])	
print(ac)
print('Windows',platform.release(),platform.version(),platform.uname() )
while True:
	if ac<19045:
		b='你当前系统是'
		c='升级到Windows10 22H2以继续'
		aa='windows'+aa
		print(b+aa+c)
		time.sleep(5)
		exit(0)
	else:
		break
#判断有无skip	
while True:
	if os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes'):
		break
	else:
		exit(0)
#判断有无选择国家		
yyyy=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt')
xxxa=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\accounts name.txt')
xxxb=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\password.txt')	
while True:
	if yyyy==False and os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\start.txt'):
		print('请选择国家，目前支持20个国家')
		print('1.中国')
		print('2.俄罗斯')
		print('3.日本')
		print('4.韩国')
		print('5.英国')
		print('6.爱尔兰')
		print('7.德国')
		print('8.法国')
		print('9.奥地利')
		print('10.荷兰')
		print('11.美国')
		print('12.加拿大')
		print('13.墨西哥')
		print('14.巴西')
		print('15.印度')
		print('16.阿根廷')
		print('17.哥伦比亚')
		print('18.澳大利亚')
		print('19.新西兰')
		print('20.埃及')
		while True:
			j=input()
			#中国
			if j=='1':
				aaa=0
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=1
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('China')
				break
			#俄罗斯
			elif j=='2':
				aaa=0
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=0
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Russia')
				break
			#日本
			elif j=='3':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Jepan')
				break
			#韩国
			elif j=='4':
				aaa=0
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Korea')
				break
			#英国
			elif j=='5':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('England')
				break
			#爱尔兰
			elif j=='6':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=1
				aag=0
				aah=1
				aai=1
				with open('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Lreland')
				break
			#德国
			elif j=='7':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Germany')
				break
			#法国
			elif j=='8':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('France')
				break
			#奥地利
			elif j=='9':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=0
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Austria')
				break
			#荷兰
			elif j=='10':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Netherlands')
				break
			#美国
			elif j=='11':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('America')
				break
			#加拿大
			elif j=='12':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Canada')
				break
			#墨西哥
			elif j=='13':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Mexico')
				break
			#巴西
			elif j=='14':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Brazil')
				break
			#印度
			elif j=='15':
				aaa=0
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('India')
				break
			#阿根廷
			elif j=='16':
				aaa=1
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Argentina')
				break
			#哥伦比亚
			elif j=='17':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Colombia')
				break
			#澳大利亚
			elif j=='18':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Australia')
				
				break
			#新西兰
			elif j=='19':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=0
				aag=1
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('New Zealand')
				break
			#埃及
			elif j=='20':
				aaa=1
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Egypt')
				break
			else:
				print('无效，请重新输入')
		#判断有无widget日志		
		zzza=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt')
		zzzb=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt')
		zzzc=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt')
		zzzd=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt')
		zzze=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt')
		zzzf=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt')
		zzzg=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt')
		zzzh=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt')
		zzzi=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt')		
		if aaa==1 and zzza==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aab==1 and zzzb==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aac==1 and zzzc==False:
			with open('liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aad==1 and zzzd==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aae==1 and zzze==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aaf==1 and zzzf==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aag==1 and zzzg==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aah==1 and zzzh==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aai==1 and zzzi==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt','w',encoding='utf-8')as witt:
				witt.write('')																				
	else:
		break
#判断有无账户设置	
#widgets\\
while True:
	if xxxa==False and xxxb==False and os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\start.txt'):
		print('需要添加账户,这个账户可以验证你的身份（用于打开软件）')
		while True:
			m=input('账户名：')
			if m=='':
				print('账户名不能为空')
			else:
				break
		time.sleep(0.4)
		while True:
			n=input('密码:')
			if n=='':
				print('密码不能为空')
			else:
				break
		os.mkdir('C:\\liexee\\creak\\liexe\\accounts')
		with open ('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\accounts name','w',encoding='utf-8')as wrotea:
			wrotea.write(m)
		with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\password','w',encoding='utf-8')as wroteb:
			wroteb.write(n)		
		time.sleep(1)
	else:
		break
#判断有没有依赖文件						
while True:
	if os.path.exists('C:\\liexee\\creak\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\start.txt'):
		break
	else:			    
		print('                                 🪟  liexe')
		print('国家：请输入')
		print('功能地区：请输入')
		a=input('国家🌍🌎🌏：')
		b=input('地区🏡🗽🎌：')
		time.sleep(1)
		a='国家🌍🌎🌏：'+a
		b='地区🏡🗽🎌：'+b
		print('您的电脑需重新启动才能完成以下配置😊')
		time.sleep(2)
		for i in range(10000):
			print('')
		print('                                 🪟  liexe')
		print(a)
		print(b)
		print('下一步，请按1，退出，请按5')
		while True:
			c=input()
			if c=='1':
				break
			if c=='5':

				exit(0)
			else:
				print('无效')
		#激活Windows,密钥FHR48-HHN87-VI7FV-9GSW2-KN567,78BRY-BRRHT-23H7R-7BTYY-4756H,GYYG8-YBGJ8-YGHUY-8GBHU-NFSTK
		time.sleep(2)
		print('激活Windows')
		print('如果你是重新安装Windows，请点击“我没有产品密钥”；如果你是安装Windows副本，请输入密钥')
		print('1.查看产品密钥规则')
		print('2.我没有产品密钥')
		print('3.输入密钥')
		while True:
			e='0'
			d=input()
			if d!='1'and d!='2'and d!='3':
				print('ERROR')
			if d=='3':
				while True:
					print('Key:')
					e=input()
					if e=='FHR48-HHN87-VI7FV-9GSW2-KN567'or e=='GYYG8-YBGJ8-YGHUY-8GBHU-NFSTK' or e=='78BRY-BRRHT-23H7R-7BTYY-4756H' :
						active=1
						break
					else:
						print('error:',e)
			if e=='FHR48-HHN87-VI7FV-9GSW2-KN567'or e=='GYYG8-YBGJ8-YGHUY-8GBHU-NFSTK' or e=='78BRY-BRRHT-23H7R-7BTYY-4756H':
				break
			if d=='2':
				active=0
				break
			if d=='1':
				print('密钥由25个字母或数字组成还需在每5个字母加上-，例如XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')     
		#安装界面
		time.sleep(1)
		print('检测到有两种硬盘，你要安装到机械硬盘还是固态硬盘？')
		print('1.HHD')
		print('2.SSD')
		while True:
			f=input()
			if f!='2'and f!='1':
				print('无效')
			if f=='2':
				g=0.01
				break
			if f=='1':
				g=2
				break
		#安装Windows
		for i in range(10000):
			print('')
		time.sleep(3)
		print('📂正在安装Windows......')
		for i in range(101):
			i=str(i)
			i=i+'%'
			print(i)
			while True:
				if i == '99%':
					if os.path.exists('C:\\liexee\\widgets\\lei.exe'):
						break
					shutil.copy('C:\\liexee\\liexe\\widgets install.msi','C:\\liexee\\widgets\\SOUR')
					os.startfile('C:\\liexee\\widgets\\SOUR\\widgets install.msi')
					while True:
						ae=os.path.exists('C:\\liexee\\widgets\\lei.exe')
						if ae == False:
							continue
						else:
							break
				break				
			time.sleep(g)
		print('restarting.......')
		#安装一系列功能
		#即将进入OOBE界面
		time.sleep(2)
		g=g*27
		for i in range(10000):
			print('')
		print('🪟')
		time.sleep(g)
		for i in range(1000):
			print('')
		print('🪟')
		time.sleep(3)
		#进入OOBE国家
		print('请选择国家，目前支持20个国家')
		print('1.中国')
		print('2.俄罗斯')
		print('3.日本')
		print('4.韩国')
		print('5.英国')
		print('6.爱尔兰')
		print('7.德国')
		print('8.法国')
		print('9.奥地利')
		print('10.荷兰')
		print('11.美国')
		print('12.加拿大')
		print('13.墨西哥')
		print('14.巴西')
		print('15.印度')
		print('16.阿根廷')
		print('17.哥伦比亚')
		print('18.澳大利亚')
		print('19.新西兰')
		print('20.埃及')
		while True:
			j=input()
			#中国
			if j=='1':
				aaa=0
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=1
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('China')
				break
			#俄罗斯
			elif j=='2':
				aaa=0
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=0
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Russia')
				break
			#日本
			elif j=='3':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Jepan')
				break
			#韩国
			elif j=='4':
				aaa=0
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Korea')
				break
			#英国
			elif j=='5':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('England')
				break
			#爱尔兰
			elif j=='6':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=1
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Lreland')
				break
			#德国
			elif j=='7':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Germany')
				break
			#法国
			elif j=='8':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('France')
				break
			#奥地利
			elif j=='9':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=0
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Austria')
				break
			#荷兰
			elif j=='10':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Netherlands')
				break
			#美国
			elif j=='11':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('America')
				break
			#加拿大
			elif j=='12':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Canada')
				break
			#墨西哥
			elif j=='13':
				aaa=1
				aab=1
				aac=1
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Mexico')
				break
			#巴西
			elif j=='14':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Brazil')
				break
			#印度
			elif j=='15':
				aaa=0
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('India')
				break
			#阿根廷
			elif j=='16':
				aaa=1
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Argentina')
				break
			#哥伦比亚
			elif j=='17':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Colombia')
				break
			#澳大利亚
			elif j=='18':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=1
				aag=1
				aah=1
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Australia')
				break
			#新西兰
			elif j=='19':
				aaa=1
				aab=1
				aac=1
				aad=1
				aae=1
				aaf=0
				aag=1
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('New Zealand')
				break
			#埃及
			elif j=='20':
				aaa=1
				aab=1
				aac=0
				aad=0
				aae=0
				aaf=0
				aag=0
				aah=0
				aai=1
				with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\country.txt','w',encoding='utf-8')as writef:
					writef.write('Egypt')
				break
			else:
				print('无效，请重新输入')
		zzza=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt')
		zzzb=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt')
		zzzc=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt')
		zzzd=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt')
		zzze=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt')
		zzzf=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt')
		zzzg=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei')
		zzzh=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt')
		zzzi=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt')		
		if aaa==1 and zzza==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aab==1 and zzzb==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aac==1 and zzzc==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aad==1 and zzzd==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aae==1 and zzze==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aaf==1 and zzzf==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aag==1 and zzzg==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aah==1 and zzzh==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aai==1 and zzzi==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt','w',encoding='utf-8')as witt:
				witt.write('')		
		time.sleep(2)
		print('需要连接服务器，只有打开很多功能才会使用')
		time.sleep(1)
		print('名称:windows_desktop_server')#密钥：8768BTFBUYIhyu^&$%^&(8UJ)
		while True:
			l=input('key:')
			if l=='8768BTFBUYIhyu^&$%^&(8UJ)':
				time.sleep(1)
				break
			else:
				print('ERROR',l)
		print('需要添加账户,这个账户可以验证你的身份（用于打开软件）')
		while True:
			m=input('账户名：')
			if m=='':
				print('账户名不能为空')
			else:
				break
		time.sleep(0.4)
		while True:
			n=input('密码:')
			if n=='':
				print('密码不能为空')
			else:
				break
		with open ('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\accounts name.txt','w',encoding='utf-8')as wrotea:
			wrotea.write(m)
		with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\password.txt','w',encoding='utf-8')as wroteb:
			wroteb.write(n)		
		time.sleep(1)
		if j=='3' or j=='5' or j=='7' or j=='8' or j=='10' or j=='11' or j=='12' or j=='14' or j=='17' or j=='18':
			print('1.games')
			print('2.clock')
			print('3.clock s')
			print('4.clock pro')
			print('5.clock pro plus')
			print('6.turtle')
			print('7.lei')
			print('8.pynotepad')
			print('9.calculator')
			o=input('请选择一些功能:')
			if any(char in o for char in ['1']) :
				aaa=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt')
				aaa=0	
			if any(char in o for char in ['2']):
				aab=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt')
				aab=0	
			if any(char in o for char in ['3']):
				aac=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt')
				aac=0
			if any(char in o for char in['4']):
				aad=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt')
				aad=0	
			if any(char in o for char in['5']):
				aae=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt')
				aae=0	
			if any(char in o for char in['6']):
				aaf=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt')
				aaf=0	
			if any(char in o for char in['7']):
				aag=1
			else:	
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt')
				aag=0
			if any(char in o for char in['8']):
				aah=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt')
				aah=0	
			if any(char in o for char in['9']):
				aai=1
			else:
				os.remove('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt')
				aai=0
		print('正在为最后的设置做准备......')
		zzza=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt')
		zzzb=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt')
		zzzc=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt')
		zzzd=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt')
		zzze=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt')
		zzzf=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt')
		zzzg=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt')
		zzzh=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt')
		zzzi=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt')		
		if aaa==0 and zzza== False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aab==0 and zzzb==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aac==1 and zzzc==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aad==1 and zzzd==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aae==1 and zzze==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aaf==1 and zzzf==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aag==1 and zzzg==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aah==1 and zzzh==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt','w',encoding='utf-8')as witt:
				witt.write('')
		if aai==1 and zzzi==False:
			with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt','w',encoding='utf-8')as witt:
				witt.write('')
		a=0
		b=0
		aaaa=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\active.txt')
		while True:
			if active==1:
				break
			else:
				if aaaa==False:
					active=0
				break	
		with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\start.txt','w',encoding='utf-8')as iii:
			iii.write('')
		a=random.randint(10,50)
		time.sleep(a)
		print('已成功配置,现在你可以使用了')
with open ('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\accounts name.txt','r',encoding='utf-8') as mm:
	m=mm.read()	
with open ('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\accounts\\password.txt','r',encoding='utf-8') as mn:
	n=mn.read()	

aaaa=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\active.txt')
if aaaa==True:
	active=1
else:
	active=0	

zzza=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\games.txt')
zzzb=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock.txt')
zzzc=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock s.txt')
zzzd=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro.txt')
zzze=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\clock pro plus.txt')
zzzf=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\turtle.txt')
zzzg=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\lei.txt')
zzzh=os.path.exists('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\pynotepad.txt')
zzzi=os.path.exists('C:\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\yes\\widgets\\calculator.txt')
if zzza==True:
	aaa=1
else:
	aaa=0
if zzzb==True:
	aab=1
else:
	zzb=0
if zzzc==True:
	aac=1
else:
	aac=0
if zzzd==True:
	aad=1
else:
	aad=0
if zzze==True:
	aae=1
else:
	aae=0
if zzzf==True:
	aaf=1
else:
	aaf=0
if zzzg==True:
	aag=1
else:
	aag=0
if zzzh==True:
	aah=1
else:
	aah=0
if zzzi==True:
	aai=1
else:
	aai=0																	
while True:
	while True:
		if active==0:
			print('a.激活Windows')
		if aaa==1:
			print('1.games')
		if aab==1:
			print('2.clock')
		if aac==1:
			print('3.clock s')
		if aad==1:
			print('4.clock pro')
		if aae==1:
			print('5.clock pro plus')
		if aaf==1:
			print('6.turtle')
		if aag==1:
			print('7.lei')
		if aah==1:
			print('8.pynotepad')
		if aai==1:
			print('9.calculator')
		aaaaa=os.path.exists('C:\\liexee\\widgets\\lei.exe')
		if aaaaa==False:
			print('b.Install widgets')	
		p=input('选择功能:(+exit):')
		while True:									
			if p=='a' and active==0:
				print('输入密钥')
				while True:
					e=input('key:')
					if e=='GYYG8-YBGJ8-YGHUY-8GBHU-NFSTK' or e=='78BRY-BRRHT-23H7R-7BTYY-4756H' or e=='FHR48-HHN87-VI7FV-9GSW2-KN567':
						print('正在审核中......')
						time.sleep(10)
						active=1
						with open('C:\\liexee\\creak\\liexe\\00000-00000-00-0-000000-000-000000-0000-0000-0000-00\\active.txt','w',encoding='utf-8')as f:
							f.write('')
						print('激活成功')
						break
					else:
						print('正在审核中......')
						time.sleep(10)
						print('激活失败！！！')
				break
#1aaa=games
#2aab=clock
#3aac=clock s
#4aad=clock pro
#5aae=clock pro plus
#6aaf=turtle
#7aag=lei
#8aah=pynotepad
#9aai=calculator			
			if p=='1' and aaa==1 and os.path.exists('C:\\liexee\\widgets\\games.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.system('C:\\liexee\\widgets\\games.exe')
				break
			elif p=='2' and aab==1 and os.path.exists('C:\\liexee\\widgets\\clock.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\clock.exe')
				time.sleep(10)
				break
			elif p=='3' and aac==1 and os.path.exists('C:\\liexee\\widgets\\clock s.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\clock s.exe')
				break
			elif p=='4' and aad==1 and os.path.exists('C:\liexee\\widgets\\clock pro.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\clock pro.exe')
				break
			elif p=='5' and aae==1 and os.path.exists('C:\\liexee\\widgets\\clock pro plus.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\clock pro plus.exe')
				break
			elif p=='6' and aaf==1 and os.path.exists('C:\\liexee\\widgets\\turtle.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\turtle.exe')
				break
			elif p=='7' and aag==1 and os.path.exists('C:\\liexee\\widgets\\lei.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\lei.exe')
				break
			elif p=='8' and aah==1 and os.path.exists('C:\\liexee\\widgets\\pynotepad.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\pynotepad.exe')
				break
			#9aai=calculator
			elif p=='9' and aai==1 and os.path.exists('C:\\liexee\\widgets\\calculator.exe'):
				while True:
					checka=''
					checkb=''
					checka=input('你的账户名')
					time.sleep(1)
					checkb=input('密码')
					time.sleep(1)
					if checka==m and checkb==n:
						break
					else:
						print('账户名或密码错误')
				os.startfile('C:\\liexee\\widgets\\calculator.exe')
				break
			elif p=='b' and aaaaa==False:
				os.startfile('C:\\liexee\\widgets\\SOUR\\widgets install.msi')
				break
			elif p=='exit':
				exit(0)
			else:
				print('错误，输入可能不正确，配置也可能不正确，有可能没正确安装，请到正确路径下载(见日志)。或者你的国家不支持（这不太可能，因为国家不支持也被禁用）如果打不开turtle，那么他在一次质量更新中删除，但仍可恢复。')
				time.sleep(5)
				break	