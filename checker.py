import re
'''This Program accepts a username and password from the user and based on certain criteria 
    accepts or rejects the password or username or both, I have used regex to
    check the pattern(i.e username and password)'''
log={}
def validity():
  u=input()
  p=input()
  print("Input Username:",u)
  print("Input password:",len(p)*"*")
  if len(p)>=8 and len(p)<=100 and len(u)<=100:   # 8<=pwd size<=100 size and u size <=100 
    if re.search(r"^[A-Za-z]{1,}[A-Za-z0-9]{0,}[-_.]{1,}[A-Za-z0-9]{0,}$",u)!=None:      
      '''The condition for username is as follows------
         1. Must Start with Letter
         2. Must have atleast one of .-_    '''
      if re.search(r"[A-Z]",p)!=None and re.search(r"[\W_]",p)!=None and re.search(r"[0-9]",p)!=None:
        ''' The condition for username is as follows------
         1. Must have a Uppercase letter
         2. Must have atleast one special character letter
         3. Must have a digit          
         4. Must not be taken already       '''
        if u in log.keys():
          print("mail ID already exists: Try again")
        else:
          print("Valid id and password: Accepted")
          log[u]=p
      else:
        print("Invalid Password: Try again")
    else:
      if re.search(r"[A-Z]",p)!=None and re.search(r"[\W_]",p)!=None and re.search(r"[0-9]",p)!=None:
        print("Invalid mail ID: Try again")
      else:
        print("Invalid id and password: Try again")
  else:
    if len(p)<8:
      print("Password too short: Try again")
    elif len(p)>100:
      print("Password too long: Try again")
    else:
      print("Username too long: Try again")
  validity()
if __name__=="__main__":
  validity()
