#classe que terá seus métodos testados
class Alvo:
    def adicao(self, valor1, valor2):
        valorTotal = valor1 + valor2
        return valorTotal
    def subtracao(self, valor1, valor2):
        valorTotal = valor1 - valor2
        return valorTotal
    def multiplicacaoAdivinhacao(self, valor1, valor2, resultadoEsperado):
        valorTotal = valor1 * valor2
        retorno = None
        if(resultadoEsperado == valorTotal):retorno = True
        else:retorno = None
        return retorno

#classe que executará os textes
import unittest  
class Testador (unittest.TestCase):    
    objetoAlvo = Alvo()
    def testeAdicao(self):
        resultado = self.objetoAlvo.adicao(2,2)
        self.assertEqual(resultado, 4)
    def testeSubtracao(self):
        resultado = self.objetoAlvo.subtracao(2,2)
        self.assertEqual(resultado, 0)
    def testeMultiplicacao(self):
        resultado = self.objetoAlvo.multiplicacaoAdivinhacao(2,2,4)
        self.assertTrue(resultado)
        
unittest.main()