#Formulas:( 
#   descripcion:(   
#       ICA_j = Es el indice de Calidad de agua calculado a la altura de un punto de monitoreo j
#       W_i= Es el ponderado o peso relativo asignado a la variable de calidad i          
#       I_i = Es el valor calculado de la variable i, obtenido al ingresar el valor de la concentracion de la variable obtenida en el punto de monitoreo j, en la curva funcional o ecuacion correspondiente. 
#       i = Corresponde a la variable que hace parte del indicador
#       
#         
#    )
#     
#   ICA_j = (suma_total del peso relativo "W_i" * "I_ij" )
# 
# 
# 
#   
# 
#    
#  )


#class Funciones:
#    def __init__(self,):
#        self.ica =1+1

import math

I=[]
W_1=0.2
W_2=0.17

class Funciones():
    #construcctor
    def __init__(self,archivo_entrada="ejemplo.txt",archivo_salida="G_resultado.txt"):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida

    #lectura de datos
    def lec_d(self):
        todas_las_filas=[]
        with open(self.archivo_entrada, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia:
                    lista_numeros = [float(x) for x in linea_limpia.split(",")]
                    todas_las_filas.append(lista_numeros)
        return todas_las_filas

    def Funn(self):
        datos= self.lec_d()
        fila = datos[0]

        #Lista de datos
        #I_OD = fila[0]
        #I_SST = fila[1]
        #I_DQO = fila[2]
        #I_CE = fila[3]
        #I_PH = fila[4]
        #I_N = fila[5]

        #calculos
        def I_OD(self):
            if fila[0]<100: OD=1-(1-0.01*fila[0])
            else:   OD=1-(1-0.01*fila[0]-1)
            return OD

        def I_SST(self):
            if fila[1]<=4.5:     SST=1
            elif fila[1]>=320:    SST=0
            else:   SST=1-(-0.02+0.003*fila[1])
            return SST

        def I_DQO(self):
            if fila[2]>80:   DQO=0.125
            elif fila[2]<=20:   DQO=0.91
            elif 25<fila[2]<=40:    DQO=0.51   
            elif 20<fila[2]<=25:   DQO=0.71
            elif 40<fila[2]<=80:   DQO=0.26
            return DQO

        def I_CE(self):
            CE=1-10**(-3.26+1.34* math.log10(fila[3]))
            CE=max(0, min(1,CE))
            return CE

        def I_PH(self):
            if fila[3]>11:
                PH=0.1
            elif fila[3]<4:
                PH=0.1
            elif 7<fila[3]<=8:
                PH=1
            elif 8<fila[3]<=11:
                1*math.e**((PH-8)*-5187742)
            elif 4<=fila[3]<=7:
                PH=0.02628419*math.e**(PH*0.520025)
            return PH

        #decision de calculo
        def seis (self):
            if fila[5]<=5 or NT>20:  NT = 0.15
            if 15<=fila[5]<=20:  NT = 0.8
            if 5<fila[5]<=10:  NT = 0.35
            if 10<fila[5]<15:  NT = 0.6
            return NT

            #for i in range(6):
                

        def cinco (self,fila):
            fila.addend(0)
        
        def metodo(self,fila):
            if len(fila) == 5:
                return self.cinco(fila)
            elif len(fila) == 6:
                return self.seis(fila)



    #salida de datos
    def salida_datos(self,lista_resultados):
        with open(self.archivo_salida, "w", encoding="utf-8") as archivo:
            for fila in lista_resultados:
                linea_texto = ",".join(map(str,fila))
                archivo.write(linea_texto + "\n")

#procesador= Funciones("ejemplo.txt","G_resultado.txt")
#lec_d = procesador.lec_d()
#print("primera  = ", lec_d[0])





#   este indicaor de puede calcular con variables (    
#   oxigeno disuelto (OD);  
#   solidos suspendidos totales (SST);    
#   demanda quimica de oxigeno (DQO);
#   Conductividad electrica (CE);    
#   Relacion nitrogeno total/fosforo total  (N total / P total);
#   en caso de no tener disponibles datos de la relacion de nutrientes es posibl realizar el calculo unicamente con 5 variables   
#   
#   
#       unidades:(  
#           OD: % saturacion
#           SST: mg/L   
#           DQO: mg/L
#           CE: uS/cm   
#           NT/NP: mg/L  /  mg/L    
#               Peso de importancia 1(ICA 5 variables)  
#               Peso de importancia 2(ICA 6 variables)              
#           pH: unidades de pH
#           
#         )
# 
#   )


#   OD:(        
#  
#       Inicialmente se calcula el porcentaje de saturación de oxígeno disuelto 𝑃𝑆𝑂𝐷:
#       formula:        𝑃𝑆𝑂𝐷 = O𝑥 ∗ 100/CP  
#
#       Donde: 
#  
#           𝑂𝑥: Es el oxígeno disuelto medido en campo (mg/l) asociado a la elevación, caudal y capacidad de reoxigenación.
#
#           CP: Es la concentración de equilibrio de oxígeno (mg/l), a la presión no estándar, es decir, oxígeno de saturación.
#
#           Una vez calculado el porcentaje de saturación de oxígeno disuelto, el subíndice del oxígeno disuelto 𝐼𝑂𝐷 se calcula con la fórmula:
#                                       
#           𝐼𝑂𝐷 = 1 − (1 − 0,01 ⋅ 𝑃𝑆𝑂𝐷)
#   )


#   SST:(  
#       El subíndice de calidad para sólidos suspendidos se calcula como sigue: 
#  
#          𝐼_𝑆𝑆𝑇 = 1 − (−0,02 + 0,003 ⋅ 𝑆𝑆𝑇)    
#
#           Si 𝑆𝑆𝑇 ≤ 4,5, entonces 𝐼𝑆𝑆𝑇 = 1
#           Si 𝑆𝑆𝑇 ≥ 320, entonces 𝐼𝑆𝑆𝑇 = 0
#   )


#   DQO:(   
#       Si 𝐷𝑄𝑂 ≤ 20, entonces 𝐼𝐷𝑄𝑂 = 0,91   
#       Si 20 < 𝐷𝑄𝑂 ≤ 25, entonces 𝐼𝐷𝑄𝑂 = 0,71
#       Si 25 < 𝐷𝑄𝑂 ≤ 40, entonces 𝐼𝐷𝑄𝑂 = 0,51
#       Si 40 < 𝐷𝑄𝑂 ≤ 80, entonces 𝐼𝐷𝑄𝑂 = 0,26
#       Si 𝐷𝑄𝑂 > 80, entonces 𝐼𝐷𝑄𝑂 = 0,125
#   )

#   CE:(    
#       𝐼_𝐶.𝐸. = 1− 10 (−3,26+1,34_𝐿𝑜𝑔10_𝐶.𝐸.)
#       Cuando 𝐼_𝐶.𝐸. < 0, entonces 𝐼_𝐶.𝐸. = 0.    
#   )

#   pH:(    
#       Si 𝑝𝐻 < 4, entonces 𝐼𝑝𝐻 = 0,1
#       Si 4 ≤ 𝑝𝐻 ≤ 7, entonces 𝐼𝑝𝐻 = 0,02628419 ⋅ 𝑒^(𝑝𝐻⋅0,520025)
#       Si 7 < 𝑝𝐻 ≤ 8, entonces 𝐼𝑝𝐻 = 1
#       Si 8 < 𝑝𝐻 ≤ 11, entonces 𝐼𝑝𝐻 = 1 ⋅ 𝑒
#       [(𝑝𝐻−8) ∗−0,5187742]
#       Si 𝑝𝐻 > 11, entonces 𝐼𝑝𝐻 = 0,1
#  )



#   NT:(        
#       Si 15 ≤ 𝑁𝑇/𝑃𝑇 ≤ 20, entonces 𝐼𝑁𝑇/𝑃𝑇 = 0,8
#       Si 10 < 𝑁𝑇/𝑃𝑇 < 15, entonces 𝐼𝑁𝑇/𝑃𝑇 = 0,6
#       Si 5 < 𝑁𝑇/𝑃𝑇 ≤ 10, entonces 𝐼𝑁𝑇/𝑃𝑇 = 0,35
#       Si 𝑁𝑇/𝑃𝑇 ≤ 5, o 𝑁𝑇/𝑃𝑇 > 20, entonces 𝐼𝑁𝑇/𝑃𝑇 = 0,15
#   )


#"descripion" = [ "buena", "aceptable", "regular", "mala", "muy mala",]
#"colores" = ["azul", "verde", "amarillo", "naranja", "rojo",]