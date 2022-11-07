# Employee-detailes
def emp_det ():
    ecode = input("Enter ecode:")
    ename = input("Enter ename:")
    dept = input("Enter dept:")
    print("Ecode {} Ename {} Dept {}".format (ecode,ename,dept))


    


# Employee salary

def emp_sal ():
        bs=int(input("Enter basic salary:"))
        bn=bs*(13.334/100)
        pf=bn*(0/100)
        net=bs+bn+pf
        print("Basic {} Bonus {} Pf {} Net {}".format (bs,bn,pf,net))


emp_det()
emp_sal()
