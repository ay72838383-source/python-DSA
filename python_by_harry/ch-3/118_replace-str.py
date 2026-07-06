#before changing
letter = '''dear <|name|>
you are selected
<|date|>'''
print("before changing\n",letter)

#after changing

letter2= '''dear <|name|>
you are selected
<|date|>'''
print(letter2.replace( " <|name|>\n"," prince\n").replace("\n<|date|>","\n24th june 2028"))