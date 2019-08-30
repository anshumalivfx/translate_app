from textblob import TextBlob as Tx

Text = input("Enter Text Here: ")
trans = Tx(Text)
lang = trans.detect_language()

des = input("Enter Language To Translate: ")

if des == "Hindi":
    tran = trans.translate(from_lang = lang, to ='hi')
    print("Translation:- ",tran)
elif des == "French":
    tran = trans.translate(from_lang = lang, to ='fr')
    print("Translation:- ",tran)
elif des == "Urdu":
    tran = trans.translate(from_lang = lang, to ='ur')
    print("Translation:- ",tran)
elif des == "Arabic":
    tran = trans.translate(from_lang = lang, to ='ar')
    print("Translation:- ",tran)
elif des == "Chinese":
    tran = trans.translate(from_lang = lang, to ='zh-CN')
    print("Translation:- ",tran)
elif des == "Punjabi":
    tran = trans.translate(from_lang = lang, to ='pa')
    print("Translation:- ",tran)
elif des == "Nepali":
    tran = trans.translate(from_lang = lang, to ='ne')
    print("Translation:- ",tran)
elif des == "Bengali":
    tran = trans.translate(from_lang = lang, to ='bn')
    print("Translation:- ",tran)
elif des == "Gujarati":
    tran = trans.translate(from_lang = lang, to ='gu')
    print("Translation:- ",tran)
elif des == "German":
    tran = trans.translate(from_lang = lang, to ='ge')
    print("Translation:- ",tran)
elif des == "Sindhi":
    tran = trans.translate(from_lang = lang, to ='sd')
    print("Translation:- ",tran)
elif des == "Persian":
    tran = trans.translate(from_lang = lang, to ='fa')
    print("Translation:- ",tran)
