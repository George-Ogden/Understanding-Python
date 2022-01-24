# codes = range(ord("A"),ord("A") + 26)
# print(dict(zip(codes,reversed(codes))))
# print("HELLO".translate(dict(zip(codes,reversed(codes)))))


from translate import Translator

translator = Translator("it")
print(translator.translate("I am hungry"))
print(translator.translate("J'ai faim"))