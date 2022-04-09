import re 
  
def main(): 
    #--------------------------------------------------------------------------
    #vaalidacion contraseña
    passwd = input("ingrese una contraseña")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pat = re.compile(reg) 
      
    mat = re.search(pat, passwd) 
      
    if mat: 
        print("Password is valid.") 
    else: 
        print("Password invalid !!") 
  
  
if __name__ == '__main__': 
    main() 
