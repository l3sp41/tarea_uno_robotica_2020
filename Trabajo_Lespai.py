# --------------------------------------------------------------------------
#                             Impotación de modulos                         #
# --------------------------------------------------------------------------#
import numpy as np                  # Modulo numpy
from scipy.integrate import quad    # Modulo scipy
import matplotlib.pyplot as plt     # importar matplotlib
# --------------------------------------------------------------------------#
#             Ecuacion elipse : [(x-x0)^2/a^2]+[(y-y0)^2/b^2] = 1           #
#             Parametros:                                                   #
#                        a : Semieje Mayo                                   #
#                        b : Semieje Menor                                  #
#                        (u,v) : Centro                                     #
#                        t: Angulo de rotación                              #
# --------------------------------------------------------------------------#
PI=3.1415926535
u= np.random.ranf() * 5.4 + 0.3     #x-position of the center
v= np.random.ranf() * 5.4 + 0.3     #y-position of the center
a= np.random.ranf() * 100 + 10      #radius on the x-axis
b= np.random.ranf() * 100 + 10    #radius on the y-axis
t = np.linspace(0, 2*PI,5000)                  

# --------------------------------------------------------------------------#                                   
#Generar aleatoreamente los parámetros de la ecuación general de la elipse #
print("--------------------------------------------------------------------")                          
print("------------------Parametros Generados Aleatoriamente---------------")
print("--------------------------------------------------------------------") 
print("a =",a)
print("b =",b)
print("u =",u)
print("v =",v)
print("t =",t,"\n")
#------------------------------Grafica de la Elipse------------------------#
x = u+a*np.cos(t)
y = v+b*np.sin(t)
p = np.array([x,y])


print("---------------------------------------------------------------------")  
print("         Puntos generados sin perturbación aditiva gausian           ")
print("---------------------------------------------------------------------")                         
print(p)
print("Tamaño de matriz de puntos", p.shape)
print("--------------------------------------------------------------------")                                                    

#--------------- Agregar una perturbación aditiva gausiana  ----------------#
#                    Media: 0 , Desviacion estandar: a*0.05                 #
#---------------------------------------------------------------------------#
n_x = np.random.normal(0,a*0.05,5000) + x
n_y = np.random.normal(0,a*0.05,5000) + y                 
#-----Generar aleatoreamente 5000 puntos pertenecientes a la elipse---------# 
q = np.array([n_x,n_y])

#-Generar aleatoreamente los parámetros de la ecuación general de la elipse-#
print("---------------------------------------------------------------------")  
print("         Puntos generados con perturbación aditiva gausian           ")
print("---------------------------------------------------------------------") 
print(q)
print("Tamaño de matriz de puntos ", q.shape)
print("---------------------------------------------------------------------")  
# ---------------------------------------------------------------------------#
#                                     Grafico                                #
# ---------------------------------------------------------------------------#
plt.figure(figsize=(9,5.5), dpi=100)
Ell = np.array([a*np.cos(t) , b*np.sin(t)])  
plt.plot( u+Ell[0,:] , v+Ell[1,:],'r' ,label='Elip. Original')     #initial ellipse
plt.plot( u+q[0,:] , v+q[1,:] ,'b',label='Elip. Con Ruido')     #initial ellipse
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Grafico elipses')
plt.grid(color='lightgray',linestyle='--')
plt.legend()
plt.savefig('Trabajo_Lespai.png')
plt.show()
np.savez('Trabajo_Lespai.npz', u_i=u, v_i=v,a_i=a,b_i=b,t_i=t,Ell_i=Ell,p_i=p,q_i=q )
