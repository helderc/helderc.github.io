Title: Python 101: O Operador Ternário
Date:   17-01-2013
Category:   Python, Tip, Code
Tags:   python, operador, ternário, tutorial
Summary: Short version for index and feeds

> Este texto é uma tradução livre do post [Python 101: The Ternary
> Operator](http://www.blog.pythonlibrary.org/2012/08/29/python-101-the-ternary-operator/),
> escrito por **Mike Driscoll**. A licença permanece a mesma
> especificada pelo autor.

Existem várias linguagens que permitem o uso do operador ternário (ou
terciário), que, em Python, consiste basicamente de uma expressão
condicional de apenas uma linha. Se você estiver interessado, poderá ler
na [Wikipédia](http://en.wikipedia.org/wiki/?:) sobre como isso é feito
em outras linguagens. Aqui iremos dar uma olhada em vário exemplos,
também iremos discutir o porque de você querer usar esse operador na
vida real.

Eu me lembro de ter usado o operador ternário em C++, onde ele é
representado pelo simbolo de interrogação. E pesquisei um pouco e
encontrei alguns bons exemplos em uma 
[pergunta respontida no StackOverflow](http://stackoverflow.com/a/394814/393194) e que também
menciona o exemplo da [Wikipédia](http://en.wikipedia.org/wiki/?:).
Vamos ver alguns deles e como funcionam. Aqui está um dos exemplos mais
simples:

```python
x = 5
y = 10
result = True if x > y else False
```

Este código é basicamente lido da seguinte maneira: O resultado será
`True` se `x` for maior que `y`, caso contrário o resultado será
`False`. Para ser honesto, isso me lembra um pouco dos blocos
condicionais do Microsoft Excel. Algumas pessoas são contra essa forma,
mas isto é o que a [documentação oficial do
Python](http://docs.python.org/release/3.0.1/reference/expressions.html#boolean-operations)
usa. O código a seguir mostra como você escreveria a instrução acima
utilizando uma instrução normal:

```python
x = 5
y = 10

if x > y:
    print "True"
else:
    print "False"
```

Veja que você economiza 3 linhas de código por utilizar o operador
ternário. Sendo assim, você pode querer utilizar esta estrutura, a
versão ternária, quando está iterando sobre um conjunto de arquivos e
quer filtrá-los em algumas seções ou linhas. Para o nosso próximo
exemplo, iremos iterar sobre alguns número e checar se eles são pares ou
ímpares:

```python
for i in range(1, 11):
    x = i % 2
    result = "Odd" if x else "Even"
    print "%s is %s" % (i, result)
```

Você ficaria surpreso com a frequência que somos lembrados da estrutura
de divisão. Esta é uma maneira de determinar se um número é par ou
ímpar. No link do StackOverflow mencionado anteriormente, tem uma parte
interessante do código que é mostrado como exemplo pelas pessoas que
ainda usam Python 2.4 ou anteriror:

```python
# (falseValue, trueValue)[test]
>>> (0, 1)[5>6]
0

>>> (0, 1)[5<6]
1
```

Este código é bem feio, mas funciona. Ele indexa uma tupla o que
certamente é um truque, mas não deixa de ser interessante. Claro, ele
não é tão diferente do que vimos anteriormente, e ambos os valores são
avaliados. Você pode até usá-lo, mas vai ter obter uma quantidade única
de erros por fazer dessa maneira onde `True` é `False` e vice-versa,
portanto eu não a recomendaria.

Existem várias outras maneiras de usar o ternário em Python com funções
lambda. Aqui está um exemplo mostrado na Wikipédia:

```python
def true():
    print "true"
    return "truly"
def false():
    print "false"
    return "falsely"

func = lambda b,a1,a2: a1 if b else a2
func(True, true, false)()

func(False, true, false)()
```

Este é um código mais arrojado, principalmente se você não sabe como as
funções lambdas funcionam. Basicamente, uma lambda é uma função anônima.
Aqui criamos duas funções normais e uma lambda. Então podemos chamá-la
com um booleano `True` e um `False`. Na primeira chamada, ela é lida
assim: chama a função `true` se o booleano é `True`, e então chama a
função `false`. A segunda é um pouco mais confusa pois parece dizer para
chamar o método `true` se o booleano for `False`, quando na verdade está
dizendo que irá chamar o método `false` apenas se `b` é `False`. É, eu
acho isso um pouco confuso também.

Conclusão
---------

Existem vários outros exemplos de operadores ternários na seção de
*Leitura Adicional* que está abaixo, mas até aqui você já deve ter
entendido como usar e talvez quando usá-lo. Eu uso esta metodologia
quando eu sei que tenho apenas uma condicional `True/False` e preciso
economizar umas linhas de código. Entretanto, frequentemente eu uso a
maneira explicita pois sei que depois terei de fazer alguma manutenção
no código e então não quero me deparar com esse tipo de coisa estranha a
todo tempo. Mas é claro, a escolha é sua.

Leitura Adicional
-----------------

-   [Condicionais em expressões (Python Recipe)](http://code.activestate.com/recipes/52310/)
-   [O Lambda Python](http://www.blog.pythonlibrary.org/2010/07/19/the-python-lambda/)
-   [StackOverflow - Lambda no lugar do if](http://stackoverflow.com/questions/7076703/lambda-instead-of-if-statement)
-   [Truques bobos com Lambda](http://p-nand-q.com/python/stupid_lambda_tricks.html)(inclui um exemplo usando o ternário)

