

class Tennis:
    
    def __init__(self, Jugador1, Jugador2):
        self.__Jugador1=""
        self.__Jugador2=""
        self.__Puntaje1=0
        self.__Puntaje2=0
    
    def get_Jugador1(self):
        return self.__Jugador1
    
    def get_Jugador2(self):
        return self.__Jugador2
    
    def get_Marcador(self):
        if self.__hayGanador():
            return self.__Jugador_Con_Mayor_Puntaje()+ " Gana"
        if self.__Ventaja():
            j=self.__Jugador_Con_Mayor_Puntaje()
            return"Tiene ventaja "+ j
        if self.__isDeuce():
            return "Deuce"
        if self.__Puntaje1==self.__Puntaje2:
            return self.__Equivalencia_puntaje(self.__Puntaje1)+ " all"
        return self.__Equivalencia_puntaje(self.__Puntaje1) + "," + self.__Equivalencia_puntaje(self.__Puntaje2)
    
    def __Jugador_Con_Mayor_Puntaje(self):
        if self.__Puntaje1>self.__Puntaje2:
            return self.__Jugador1
        else:
            return self.__Jugador2
    
    def __hayGanador(self):
        if self.__Puntaje2>=4 and self.__Puntaje2>= self.__Puntaje1+2:
            return True 
        if self.__Puntaje1>=4 and self.__Puntaje1>= self.__Puntaje2+2:
            return True
        return False
    
    def __Ventaja(self):
        if self.__Puntaje2>=4 and self.__Puntaje2>= self.__Puntaje1+1:
            return True
        pass
        if self.__Puntaje1>=4 and self.__Puntaje1>= self.__Puntaje2+1:
            return True
        pass
        return False

    def __isDeuce(self):
        return self.__Puntaje1 >=3 and self.__Puntaje2== self.__Puntaje1

    def PuntosJ1(self):
        self.__Puntaje1+=1
        
    def PuntosJ2(self):
        self.__Puntaje2+=1 
    
    def __Equivalencia_puntaje(self, puntos):
        if puntos==0:
            return"love"
            pass
        elif puntos==1:
            return"Quince"
            pass	
        elif puntos==2:
            return "Treinta"
        elif puntos==3:
            return "Cuarenta"
        else:
            return"Puntaje no valido"