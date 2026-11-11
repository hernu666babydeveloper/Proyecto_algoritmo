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


"W_" = []
"I_ij" = []



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


"descripion" = [ "buena", "aceptable", "regular", "mala", "muy mala",]
"colores" = ["azul", "verde", "amarillo", "naranja", "rojo",]
