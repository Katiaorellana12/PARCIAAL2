from tkinter import Button, Label  , Tk, Radiobutton , IntVar , Entry
import PIL
from PIL import Image , ImageTk , ImageFilter

  #creamos la función para imprimir la factura y declarar precios  
def pago(): 
    if opcion.get()==1:
        total1=0.70
    elif opcion.get()==2:
        total1=0.65
    elif opcion.get()==3:
        total1=0.60
    if opcion2.get()==1:
         bebida1=1*0.75
    elif opcion2.get()==2:
        bebida1=1*0.50
    elif opcion2.get()==3:
         bebida1=1*0.60
    if opcion3.get()==7:
         envio1=1.50
         todo1=cantidad.get()*total1+bebida1+envio1
         print("Producto    Cantidad      Precio")
         print("Pupusas      ", "", cantidad.get(),"","", "","", "", "", "", "" , "", "", total1)
         print("Bebida  ", "","", "",  "1", "","", "","", "", "", "", "" , "", "","", "", bebida1)
         print("Costo de envio " , "--","", "","", "", "", "", "" ,  envio1)
         print("-------TOTAL-------",todo1)
    elif opcion3.get()==8:
         todo1=total1+bebida1
         print("Producto    Cantidad      Precio")
         print("Pupusas      ", "", cantidad.get(),"","", "","", "", "", "", "" , "", "", total1)
         print("Bebida   ", "","", "", "1", "","", "","", "", "", "", "" , "", "","", "", bebida1)
         print("Costo de envio " , "--","", "","", "", "", "", "Sin envio"  )
         print("-------TOTAL-------",todo1 )
   
    


#CREAMOS  INTERFAZ GRAFICA
ventana = Tk()
ventana.geometry("500x500")
ventana.title("PEDIDOS NIA MARY")
ventana.configure( bg = "#828282" )

cantidad=IntVar()
cantidad2=IntVar()
opcion = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()

#Agregamos las  imagenes 
foto2= Image.open(r"C:\Users\HP\Downloads\queso.jpg")
foto2=foto2.filter(ImageFilter.SHARPEN)
render2=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(reducida)

foto2= Image.open(r"C:\Users\HP\Downloads\fq.jpg")
foto2=foto2.filter(ImageFilter.SHARPEN)
render3=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(reducida)

foto2= Image.open(r"C:\Users\HP\Downloads\revuelta.jpg")
foto2=foto2.filter(ImageFilter.SHARPEN)
render4=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render4= ImageTk.PhotoImage(reducida) 

foto2= Image.open(r"C:\Users\HP\Downloads\gaseosas.webp")
foto2=foto2.filter(ImageFilter.SHARPEN)
render5=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render5= ImageTk.PhotoImage(reducida) 

foto2= Image.open(r"C:\Users\HP\Downloads\chocolate-caliente-3fp.jpg")
foto2=foto2.filter(ImageFilter.SHARPEN)
render6=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render6= ImageTk.PhotoImage(reducida) 

foto2= Image.open(r"C:\Users\HP\Downloads\refresccos.webp")
foto2=foto2.filter(ImageFilter.SHARPEN)
render7=ImageTk.PhotoImage(foto2)
reducida = foto2.resize((100,100), Image.Resampling.LANCZOS)
render7= ImageTk.PhotoImage(reducida) 

#Ordenamos los label , radios button etc 

label1=Label(ventana, text="OPCIONES DE PEDIDO: "  ,bg="pink")
label5=Label(ventana, text="OPCIONES DE BEBIDAS: "  ,bg="pink")
label2=Label(ventana, image=render2)
label3=Label(ventana, image=render3)
label4=Label(ventana, image=render4)
label6=Label(ventana, image=render5)
label7=Label(ventana, image=render6)
label8=Label(ventana, image=render7)



radio1=Radiobutton(ventana, text="QUESO" , value=1 , variable=opcion)
radio2=Radiobutton(ventana, text="F/Q" , value=2 , variable=opcion)
radio3=Radiobutton(ventana, text="REVUELTAS" , value=3 , variable=opcion)
radio4=Radiobutton(ventana, text="GASEOSA" , value=1, variable=opcion2)
radio5=Radiobutton(ventana, text="CHOCOLATE" , value=2 , variable=opcion2)
radio6=Radiobutton(ventana, text="REFRESCO" , value=3 , variable=opcion2)
entry1=Entry(ventana ,textvariable=cantidad)
label9=Label(ventana , text="Cantidad:")
label10=Label(ventana , text="A DOMICILIO:")
radio7=Radiobutton(ventana, text="SI" , value=7 , variable=opcion3)
radio8=Radiobutton(ventana, text="NO" , value=8 , variable=opcion3)
boton1=Button(ventana, text="IMPRIMIR FACTURA",bg="pink" , command=pago)


#mostrar en ventana 
label1.place(x=10 , y=10)
label2.place(x=10 , y=50 )
label3.place(x=200 , y=50 )
label4.place(x=375 , y=50 )
radio1.place(x=20 ,  y=160)
radio2.place(x= 230,  y=160)
radio3.place(x=390 ,  y=160)
radio4.place(x=20 ,  y=370)
radio5.place(x=220 ,  y=370)
radio6.place(x=390 ,  y=370)
entry1.place(x=200, y=210)
label5.place(x=10 ,  y=230)
label6.place(x=20 ,  y=265)
label7.place(x=210 ,  y=265)
label8.place(x=365 ,  y=265)
label9.place(x=150 , y=210)
label10.place(x=20 ,  y=400)
radio7.place(x=20 ,  y=420)
radio8.place(x=20 ,  y=440)
boton1.place(x=150,  y=420)



ventana.mainloop()
