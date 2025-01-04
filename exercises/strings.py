frase = 'Viagem ao redor da lua.'

frase_longa = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
malesuada id neque non pellentesque. Sed sit amet massa at risus faucibus
luctus. Morbi tincidunt, nisl in dignissim vulputate, magna mi sagittis
libero, vitae luctus leo tortor ac purus. Nam mattis lectus eu massa dapibus,
ac placerat ligula sollicitudin. Maecenas scelerisque tellus a tellus
scelerisque interdum. Aliquam erat volutpat.'''

frase_longa2 = '''Lorem    ipsum dolor sit amet, consectetur adipiscing   elit. Suspendisse
malesuada id neque non   pellentesque. Sed sit amet massa at risus  faucibus
luctus. Morbi tincidunt,   nisl in dignissim vulputate,  magna       mi  sagittis
libero,  vitae  luctus leo tortor      ac purus. Nam mattis lectus eu massa dapibus,
ac placerat  ligula   sollicitudin.    Maecenas scelerisque tellus a tellus
scelerisque             interdum. Aliquam erat        volutpat.'''

print(f'{frase[:7]}')

# Imprimir um texto longo na tela.

print (frase_longa.count(' ')) # Contando os espaços vazios na string.

print (f'{frase_longa2}') # Contando os espaços vazios na string.

# frase_longa2 = "Esta   frase  tem   espaços   irregulares."
frase_ajustada = ' '.join(frase_longa2.split())
print(f"Frase ajustada: '{frase_ajustada}'")
