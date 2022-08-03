print("Flanges of rolled I-shaped sections,channels, and tees=1")
print("Flanges of doubly and singly symmetric I-shaped built-up sections=2")
print("Legs of single angles=3")
print("Flanges of allI-shaped sectionsand channels in flexure about the minor axis=4")
print("Stems of tees=5")
print("Webs of doubly symmetric I-shaped sections and channels=6")
print("Webs of singlysymmetricI-shaped sections=7")
print("Flanges of rectangular HSS=8")
print("Flange cover plates and diaphragm plates between lines of fasteners orwelds=9")
print("Webs of rectangular HSS and box sections=10")
print("Round HSS=11")
print("langes of box sections=12")

E=200000


Fy=int(input ("Fy in Mpa ="))
Code=int(input("Please enter code  :"))
Code2=int(input("Please enter code  :"))
Widthf=float(input("Please enter the  width  of flange :"))
Thicknessf=float(input("Please enter the thickness of flange  :"))
Widthw=float(input("Please enter the  width of web  :"))
Thicknessw=float(input("Please enter the  thickness of web  :"))


if Code==1 and Code2==6:

     hpf =(0.38*((E/Fy)**0.5))
     hpw =(3.76*((E/Fy)**0.5))  
     hrf=(1*((E/Fy)**0.5))
     hrw=(5.70*((E/Fy)**0.5))

elif Code==2 and Code2==6:
    kc=(4/((Widthw/Thicknessw)**0.5))
    FL=0.7*Fy

    hpf =(0.38*((E/Fy)**0.5))
    hpw =(3.76*((kc*E/FL)**0.5))  
    hrf=(0.95*((E/Fy)**0.5))
    hrw=(5.70*((E/Fy)**0.5))

elif Code==3 :

     hpf =(0.54*((E/Fy)**0.5))
     hpw =(0.91*((E/Fy)**0.5))  

elif Code==4 :

     hpf =(0.38*((E/Fy)**0.5))
     hpw =(1*((E/Fy)**0.5)) 

elif Code==5 :

     hpf =(0.84*((E/Fy)**0.5))
     hpw =(1.52*((E/Fy)**0.5)) 


elif Code==8 :

     hpf =(1.12*((E/Fy)**0.5))
     hpw =(1.40*((E/Fy)**0.5)) 

elif Code==9 :

     hpf =(1.12*((E/Fy)**0.5))
     hpw =(1.40*((E/Fy)**0.5)) 

elif Code==11 :

     hpf =(0.07*((E/Fy)**1))
     hpw =(0.31*((E/Fy)**1)) 

elif Code==10 and Code2==12:

     hpf =(1.12*((E/Fy)**0.5))
     hpw =(2.42*((E/Fy)**0.5))  
     hrf=(1.49*((E/Fy)**0.5))
     hrw=(5.70*((E/Fy)**0.5))

elif Code==1 and Code2==7:

     hpf =(0.38*((E/Fy)**0.5))
     #hpw =(3.76*((E/Fy)**0.5))  
     hrf=(1*((E/Fy)**0.5))
     hrw=(5.70*((E/Fy)**0.5))

elif Code==2 and Code2==7:
    kc=(4/((Widthw/Thicknessw)**0.5))
    FL=0.7*Fy

    hpf =(0.38*((E/Fy)**0.5))
    #hpw =(3.76*((kc*E/FL)**0.5))  
    hrf=(0.95*((E/Fy)**0.5))
    hrw=(5.70*((E/Fy)**0.5))

else:
      print("Your Information is not true , please try egain")     

print("hpf=", hpf)
print("hpw=", hpw)
print("hrf=",hrf)
print("hrw=",hrw)


if (Widthf/Thicknessf)<= hpf :
        print("The flangeS  is Compact")
elif hpf<=(Widthf/Thicknessf)<=hrf:
        print("The flangeS  is not Compact")
elif (Widthf/Thicknessf) >hrf:
         print("The flangeS is slender") 
else :
      print("Your Information is not true , please try egain")

if (Widthw/Thicknessw)<= hpw :
        print("The web  is Compact")
elif hpw<=(Widthw/Thicknessw)<=hrw:
        print("The web is not Compact")
elif (Widthw/Thicknessw) >hrw:
         print("The web is slender") 
else :
      print("Your Information is not true , please try egain")





