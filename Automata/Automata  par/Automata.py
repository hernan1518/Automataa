import pila

class Autopi:
    def __init__(self,palab):
        self.pila = pila.Pila()
        self.resultado=[]
        self.transiciones=[]
        self.estado_1 = True
        self.estado_2 = False
        self.estado_final = False
        self.palabra=palab

    def getEstado_1(self):
        return self.estado_1
    def getEstado_2(self):
        return self.estado_2
    def getEstado_final(self):
        return self.estado_final

    def activaEstado_1(self):
        self.estado_1=True
        self.estado_2=False
        self.estado_final=False

    def activaEstado_2(self):
        self.estado_2=True
        self.estado_1=False
        self.estado_final=False

    def activaEstado_final(self):
        self.estado_final=True
        self.estado_1=False
        self.estado_2=False

    #transiciones con b
    def b_b_bb(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('b')
        self.activaEstado_1()

    def b_a_ab(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('b')
        self.activaEstado_1()
    def b_n_nb(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('b')
        self.activaEstado_1()
        
    #transiciones con a
    def a_b_ba(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('a')
        self.activaEstado_1()
    def a_n_na(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('a')
        self.activaEstado_1()
    def a_a_aa(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('a')
        self.activaEstado_1()
        
    #transiciones que llevan a estado 2
    def b_b_y(self):
        self.pila.quitar()
        self.activaEstado_2()

    def a_a_y(self):
        self.pila.quitar()
        self.activaEstado_2()

    def y_n_n(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.activaEstado_final()

    def encabezados(self, palab):
        head = '|Estado 1 - Estado 2 - Estado final - Caracter -  Cima |'
        div=      '|----------------------------------------------------------------------------|'
        self.resultado.append('Palabra: '+palab)
        self.resultado.append(head)
        self.resultado.append(div)
        
        self.transiciones.append('Palabra: '+palab)
        self.transiciones.append('****** Transiciones ******')
        self.transiciones.append('-----------------------------------------------------')
        

    def validar(self):
        n=len(self.palabra)
        i=1
        palabra=self.palabra+' '
        self.encabezados(self.palabra)

        for caracter in palabra:
            paso = "{:6}   -  {:6}   -  {:6}      -   {:4} -   {:4} ".format(str(self.getEstado_1()), str(self.getEstado_2()),
                                                                                                             str(self.getEstado_final()),str(caracter),str(self.pila.cima()))
            self.resultado.append(paso)

            if (caracter != 'a' and caracter != 'b' and caracter != ' '):
                invali='El caracter es invalido en el lenguaje !!!'
                self.resultado.append(invali)
                break
            elif (self.getEstado_1()):
                if (caracter=='b'):
                    if (self.pila.cima()== 'b'):
                        if(i<(n/2)+1):
                            self.b_b_bb()
                            trans='b/b/bb'
                            self.transiciones.append('      '+trans)
                        elif(i==(n/2)+1):
                            self.b_b_y()
                            trans='b/b/y'
                            self.transiciones.append('      '+trans)   
                    elif (self.pila.cima()== 'a'):
                        self.b_a_ab()
                        trans='b/a/ab'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.cima() == '#'):
                        self.b_n_nb()
                        trans='b/#/#b'
                        self.transiciones.append('      '+trans)
                        
                elif (caracter ==  'a'):
                    if (self.pila.cima()== 'b'):
                        self.a_b_ba()
                        trans='a/b/ba'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.cima()== 'a'):
                        if(i<(n/2)+1):
                            self.a_a_aa()
                            trans='a/a/aa'
                            self.transiciones.append('      '+trans)
                        elif(i==(n/2)+1):
                            self.a_a_y()
                            trans='a/a/y'
                            self.transiciones.append('      '+trans)  
                    elif (self.pila.cima() == '#'):
                        self.a_n_na()
                        trans='a/#/#a'
                        self.transiciones.append('      '+trans)
                        
            elif (self.getEstado_2()):
                if (caracter == 'b'):
                    if (self.pila.cima() == 'b'):
                        self.b_b_y()
                        trans='b/b/y'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif (caracter == 'a'):
                    if (self.pila.cima() == 'a'):
                        self.a_a_y()
                        trans='a/a/y'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif(caracter == ' '):
                    print('palabra terminada')
                    if (self.pila.cima() == '#' and self.getEstado_2()):
                        self.y_n_n()
                        trans='y/#/#'
                        self.transiciones.append('      '+trans)
            i=i+1


        nega='* La palabra no es palondrime*'
        if (self.getEstado_final()):
            acept='*La palabra es palindrome*'
            self.resultado.append(acept)
        elif(self.getEstado_1()):
            self.resultado.append(nega)
        else:
            self.resultado.append(nega)
  




    				


		





