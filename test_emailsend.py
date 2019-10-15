import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import os


def removeExtensionFile(filePath, fileExtension):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(fileExtension):
                os.remove(file.path)
        return "Removed file: " + fileExtension
    else:
        return "Directory not found"

def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath);
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()
'''
def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zf.extractall(path=dest_path)
        zf.close()
'''

# 지메일 아이디,비번 입력하기
email_user = 'humaxnwsqe@gmail.com'      #<ID> 본인 계정 아이디 입력
email_password = 'humax2015@!'      #<PASSWORD> 본인 계정 암호 입력
email_send = ['hslee4@humaxdigital.com','jkoh@humaxdigital.com']         # <받는곳주소> 수신자 이메일 abc@abc.com 형태로 입력

# 제목 입력
subject = 'CVE Scan Result' 

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = ",".join(email_send)
msg['Subject'] = subject

# 본문 내용 입력
body = 'Please refer to the attached html page.'
msg.attach(MIMEText(body,'plain'))


############### ↓ 첨부파일이 없다면 삭제 가능  ↓ ########################
# 첨부파일 경로/이름 지정하기

#To get current path
cur_path = os.getcwd()
#print("\n"+ cur_path)


#To set report result path from current path
report_path = os.path.join(cur_path, "resultreport\\")

archive_path = cur_path + "\\"

filename ='resultreport.zip' 
target_zip = archive_path + filename

#To remove files except folder included
removeExtensionFile(report_path, ".PNG".lower())

#To zip a folder
zip(report_path, target_zip)

#filename='./resultreport/report.html'  
#filename='resultreport.zip'  
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
############### ↑ 첨부파일이 없다면 삭제 가능  ↑ ########################

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()
