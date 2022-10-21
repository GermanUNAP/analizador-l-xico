import ply.lex as lex
import sys

reserved = {
'while': 'WHILE',
'cin':'identificador',
'cout':'identificador',
'if': 'IF',
'else': 'ELSE',
'false': 'FALSE',
'true': 'TRUE',
'auto': 'auto',
'float': 'float',
'Alignof': 'align',
'Asm': 'asm',
'based': 'based',
'box 2': 'object',
'cdecl': 'convention',
'declspec': 'instace',
'delegate': 'delegation',
'event': 'event',
'except': 'exception',
'fastcall': 'callingconvention',
'finally':'Finally',
'identifier': 'identify',
'if_exists': 'identifier',
'if_not_exists': 'identifier',
'inline': 'inline',
'interface': 'interface',
'leave': 'leave',
'int':'int',
'main':'identificador'

}

tokens = list(reserved.values()) + [
    # Simbologia
    'ASIGNACION','MODULO','MAS','MASMAS','MAS_IGUAL',
    'MENOS','MENOSMENOS','MENOS_IGUAL','MULTIPLICACION',
    'DIVISION','MENOR','MENOR_IGUAL','MAYOR','MAYOR_IGUAL',
    'IGUAL','DESIGUAL','DISTINTO','IGUALIGUAL','PUNTO_COMA',
    'COMA','PARENTESIS_IZQUIERDO','PARENTESIS_DERECHO','CORCHETE_IZQUIERDO',
    'CORCHETE_DERECHO','LLAVE_IZQUIERDA','LLAVE_DERECHA','DOBLE_PUNTO',
    'AMPERSANT','PUNTO','SIGNO_PREGUNTA','COMILLASIMPLE','COMILLASDOBLES',
    'EXPONENTE','VARIABLE','VARIABLE2','NUMERO','CADENA_COMILLAS_DOBLES',
    'CADENA_COMILLAS_SIMPLES','ID','OPERADOR_ENTRADA', 'OPERADOR_SALIDA'
]
# Reglas de expresiones regulares para tokens simples
t_OPERADOR_ENTRADA = r'>>'
t_OPERADOR_SALIDA = r'<<'
t_MODULO = r'%'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_DISTINTO = r'!'

t_MENOR = r'<'
t_MAYOR = r'>'
t_PUNTO_COMA = ';'
t_COMA = r','
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_CORCHETE_IZQUIERDO = r'\['
t_CORCHETE_DERECHO = r'\]'
t_LLAVE_IZQUIERDA = r'{'
t_LLAVE_DERECHA = r'}'
t_DOBLE_PUNTO = r':'
t_AMPERSANT = r'\&'
t_PUNTO = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_SIGNO_PREGUNTA = r'\?'

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t
def t_VARIABLE(t):
    r'[a-z]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]  # comprueba si hay palabras reservadas
        return t
    else:
        return t

# Comprueba las palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Comprueba si hay palabras reservadas
        return t
    else:
        t_error(t)
def t_CADENA_COMILLAS_DOBLES(t):
    r'"((?:[^"\\]|\\.)*)"'
    return t
def t_CADENA_COMILLAS_SIMPLES(t):
    r'\'((?:[^\'\\]|\\.)*)\''
    return t
def t_MENOR_IGUAL(t):
    r'<='
    return t
def t_MAYOR_IGUAL(t):
    r'>='
    return t
def t_ASIGNACION(t):
    r'=>'
    return t
def t_MASMAS(t):
    r'\+\+'
    return t
def t_SALTO_LINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_ESPACIO(t):
    r'\s+'
    t.lexer.lineno += len(t.value)
def t_MENOSMENOS(t):
    r'--'
    return t
def t_EXPONENTE(t):
    r'\*\*'
    return t
def t_DESIGUAL(t):
    r'!='
    return t
def t_IGUALIGUAL(t):
    r'=='
    return t

t_ignore = ' \t'

def t_COMENTARIO_VARIAS_LINEAS(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += t.value.count('\n')
def t_COMENTARIO_UNA_LINEA(t):
    r'\//(.)*?\n'
    t.lexer.lineno += 1
def t_error(t):
    print("Lexical error: " + str(t.value))
    t.lexer.skip(1)
def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t" + str(i) + " - " + "Linea: " + str(tok.lineno) + "\t" + str(tok.type) + "\t-->  " + str(tok.value))
        i += 1
   # Imprime los tok
lexer: lex.Lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'CodigoC.cpp'
    f = open(fin, 'r')
    data = f.read()
    # Imprimir datos
    # lexer.input(data)
    test(data, lexer)