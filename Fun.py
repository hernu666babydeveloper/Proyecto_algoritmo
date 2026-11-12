import math

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

    #funciones
    def Funn(self):
        datos= self.lec_d()
        fila = datos[0]

        OD = self.IOD(fila)
        SST = self.ISST(fila)    
        DQO = self.IDQO(fila) 
        CE = self.ICE(fila)
        PH = self.IPH(fila)
        NT = self.metodo(fila)
        return self.GTVR(fila,OD,SST,DQO,CE,PH,NT)
           
    #OXIGENO DISUELTO
    def IOD(self,fila):
        if fila[0]<=100: OD=1-(1-0.01*fila[0])
        else:   OD=1-(0.01*fila[0]-1)
        return OD

    #SOLIDOS SUSPENDIDOS TOTAlES
    def ISST(self,fila):
        if fila[1]<=4.5:     SST=1
        elif fila[1]>=320:    SST=0
        else:   SST=1-(-0.02+0.003*fila[1])
        return SST

    #DEMANDA QUIMICA DE OXIGENO
    def IDQO(self,fila):
        if fila[2]>80:   DQO=0.125
        elif fila[2]<=20:   DQO=0.91
        elif 25<fila[2]<=40:    DQO=0.51   
        elif 20<fila[2]<=25:   DQO=0.71
        elif 40<fila[2]<=80:   DQO=0.26
        return DQO

    #CONDUCTIVIDAD ELECTRICA
    def ICE(self,fila):
        CE=1-10**(-3.26+1.34* math.log10(fila[3]))
        CE=max(0, min(1,CE))
        return CE

    #pH
    def IPH(self,fila):
        if fila[4]>11:
            PH=0.1
        elif fila[4]<4:
            PH=0.1
        elif 7<fila[4]<=8:
            PH=1
        elif 8<fila[4]<=11:
            PH=1*math.e**((fila[4]-8)*-0.5187742)
        elif 4<=fila[4]<=7:
            PH=0.02628419*math.e**(fila[4]*0.520025)
        return PH

        #decision de calculo
    def seis (self,fila):
        #NITROGENO TOTAL/FOSFORO TOTAL (P)
        if fila[5]<=5 or fila[5]>20:  NT = 0.15
        if 15<=fila[5]<=20:  NT = 0.8
        if 5<fila[5]<=10:  NT = 0.35
        if 10<fila[5]<15:  NT = 0.6
        return NT                

    def cinco (self):
        return 0
        
    def metodo(self,fila):
        if len(fila) == 6:
            return self.seis(fila)
        elif len(fila) == 5:
            return self.cinco()

    def GTVR (self,lista,IOD,ISST,IDQO,ICE,IPH,metodo):
        IICA = [IOD,ISST,IDQO,ICE,IPH,metodo]; V=[]; ICA=0

        if len(lista) == 6:
            for i in range(len(IICA)):
                V.append(0.17*IICA[i])
            for i in range(len(V)):
                ICA=ICA+V[i]        
        else:
            for i in range(len(IICA)-1):
                V.append(0.2*IICA[i])
            for i in range(len(V)):
                ICA=ICA+V[i]
        lista_completa = [round(x, 3) for x in IICA] + [round(ICA, 3)]
        return lista_completa
            
    #salida de datos
    def salida_datos(self,lista_resultados):
        with open(self.archivo_salida, "w", encoding="utf-8") as archivo:
            for fila in lista_resultados:
                linea_texto = ",".join(map(str,fila))
                archivo.write(linea_texto + "\n")

procesador=Funciones(); lista_completa= procesador.Funn()
#print("estoy cansao: ", lista_completa)
procesador.salida_datos([lista_completa])