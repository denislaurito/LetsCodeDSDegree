class Pontos():
    
    '''
    Classe que recebe duas listas, uma sem perfis definidos e outra 
    com perfis classificados.
        
    Atributos:
    k: número de pontos a serem verificados pelo método KNN
    pto_no_class: lista com perfis de investidores não definidos
    pto_data: lista com perfis de investidores definidos
    
    '''

    def __init__(self, k, pto_no_class, pto_data):#método construtor
      
        self.k = k
        self.pto_no_class = pto_no_class
        self.pto_data = pto_data

    def calculaDistancia(self): #método de cálculo da distância euclidiana
        
        '''
        Método que calcula a distância euclidiana dos pontos da carteira de investimentos (tupla) 
        entre a lista classificada e a não classificada.
        
        Args: nenhum
        Retorno: pontos da distância euclidiana (lista)
        
        '''
        p = 0 #variável da soma dos quadrados das distâncias

        ptos = list() #lista dos pontos (resultado final) calculados

        for w in range(len(self.pto_no_class)):#iteração dos elementos da lista no_class

            dist = list() #lista dos valores das distâncias

            for x in range(len(self.pto_data)):#iteração dos valores da lista no_class
                
                for y in range(len(self.pto_no_class[w][2])):#iteração dos valores da lista data

                    p += (self.pto_no_class[w][2][y] - self.pto_data[x][2][y])**2#cálculo da distância dos pontos na posição 0
  
                raiz = p**0.5 #resultado da distância final

                dist.append((raiz,x)) #insere a distância final com o index em uma lista de tuplas

                p = 0 #reset da variável de soma dos quadrados das distâncias

            ptos.append(dist) #adiciona a lista de tuplas com os index para a lista de pontos resultantes

        return ptos

    def ordenar(self): #método de classificação do perfil de investidor através dos pontos
        
        '''
        Método que classifica o perfil de investimento da lista até então não classificada
        
        Args: nenhum
        Retorno: (dicionário) perfis classificados pelo método KNN tendo o cpf como chave.
        
        '''
      
        ptos2 = self.calculaDistancia()
        classificados = dict() #iniciando dicionário para resultados classificados

        for j in range(len(ptos2)): #percorrendo as distâncias (pontos) para classificação
            con = 0 #variável para perfil consevador
            mod = 0 #variável para perfil moderado
            agr = 0 #variável para ferfil agressivo

            for i in sorted(ptos2[j])[0:self.k]: #percorrendo a lista com o K "vizinhos" estabelecido
                if self.pto_data[i[1]][1] == "Conservador": #comparação se é conservador pela posição na tupla e na lista classificada adicionando na contagem
                    con += 1 #contador de ocorrências de perfil conservador
                
                elif self.pto_data[i[1]][1] == "Moderado": #comparando se é moderado pela posição na tupla e  na lista classificada e adicionando na contagem 
                    mod += 1 #contador de ocorrências de perfil moderado
                    
                else: #comparando se é agressivo pela posição na tupla e na lista classificada e adicionando na contagem 
                    agr +=1 #contador de ocorrências de perfil agressivo
                    
            #determiniando os perfis pelo número de ocorrências
            if con >= mod and con >= agr:
                resultado = "Conservador"

            elif mod >= con and mod >= agr:
                resultado = "Moderado"

            else:
                resultado = "Agressivo"
                
            classificados[self.pto_no_class[j][0]] = resultado #adicionando os perfis ao dicionário usando o cpf como chave
            
        return classificados