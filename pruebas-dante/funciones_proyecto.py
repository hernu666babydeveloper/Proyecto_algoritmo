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


class Funciones:
    def __init__(self,):
        self.ica = 


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
"descripion" = [ "buena", "aceptable", "regular", "mala", "muy mala",]
"colores" = ["azul", "verde", "amarillo", "naranja", "rojo",]
 
#    

