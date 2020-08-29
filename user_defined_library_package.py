from tamil import utf8   
    
uyir_letters = [u"அ",u"ஆ",u"இ",u"ஈ",u"உ",u"ஊ",u"எ",u"ஏ",u"ஐ",u"ஒ",u"ஓ",u"ஔ"]
aytham_letter = u"ஃ"
mei_letters = [u"க்",u"ச்",u"ட்",u"த்",u"ப்",u"ற்",
           u"ஞ்",u"ங்",u"ண்",u"ந்",u"ம்",u"ன்",
           u"ய்",u"ர்",u"ல்",u"வ்",u"ழ்",u"ள்" ]

vallinam_letters = [u"க்", u"ச்", u"ட்", u"த்", u"ப்", u"ற்"]
mellinam_letters = [u"ங்", u"ஞ்", u"ண்", u"ந்", u"ம்", u"ன்"]
idayinam_letters = [u"ய்", u"ர்", u"ல்", u"வ்", u"ழ்", u"ள்"]

uyirmei_letters = [
u"க"  ,u"கா"  ,u"கி"  ,u"கீ"  ,u"கு"  ,u"கூ"  ,u"கெ"  ,u"கே"  ,u"கை"  ,u"கொ"  ,u"கோ"  ,u"கௌ"  ,
u"ச"  ,u"சா"  ,u"சி"  ,u"சீ"  ,u"சு"  ,u"சூ"  ,u"செ"  ,u"சே"  ,u"சை"  ,u"சொ"  ,u"சோ"  ,u"சௌ" ,
u"ட"  ,u"டா"  ,u"டி"  ,u"டீ"  ,u"டு"  ,u"டூ"  ,u"டெ"  ,u"டே"  ,u"டை"  ,u"டொ"  ,u"டோ"  ,u"டௌ",
u"த"  ,u"தா"  ,u"தி"  ,u"தீ"  ,u"து"  ,u"தூ"  ,u"தெ"  ,u"தே"  ,u"தை"  ,u"தொ"  ,u"தோ"  ,u"தௌ",
u"ப"  ,u"பா"  ,u"பி"  ,u"பீ"  ,u"பு"  ,u"பூ"  ,u"பெ"  ,u"பே"  ,u"பை"  ,u"பொ"  ,u"போ"  ,u"பௌ" ,
u"ற"  ,u"றா"  ,u"றி"  ,u"றீ"  ,u"று"  ,u"றூ"  ,u"றெ"  ,u"றே"  ,u"றை"  ,u"றொ"  ,u"றோ"  ,u"றௌ",
u"ஞ"  ,u"ஞா"  ,u"ஞி"  ,u"ஞீ"  ,u"ஞு"  ,u"ஞூ"  ,u"ஞெ"  ,u"ஞே"  ,u"ஞை"  ,u"ஞொ"  ,u"ஞோ"  ,u"ஞௌ"  ,
u"ங"  ,u"ஙா"  ,u"ஙி"  ,u"ஙீ"  ,u"ஙு"  ,u"ஙூ"  ,u"ஙெ"  ,u"ஙே"  ,u"ஙை"  ,u"ஙொ"  ,u"ஙோ"  ,u"ஙௌ"  ,
u"ண"  ,u"ணா"  ,u"ணி"  ,u"ணீ"  ,u"ணு"  ,u"ணூ"  ,u"ணெ"  ,u"ணே"  ,u"ணை"  ,u"ணொ"  ,u"ணோ"  ,u"ணௌ"  ,
u"ந"  ,u"நா"  ,u"நி"  ,u"நீ"  ,u"நு"  ,u"நூ"  ,u"நெ"  ,u"நே"  ,u"நை"  ,u"நொ"  ,u"நோ"  ,u"நௌ"  ,
u"ம"  ,u"மா"  ,u"மி"  ,u"மீ"  ,u"மு"  ,u"மூ"  ,u"மெ"  ,u"மே"  ,u"மை"  ,u"மொ"  ,u"மோ"  ,u"மௌ" ,
u"ன"  ,u"னா"  ,u"னி"  ,u"னீ"  ,u"னு"  ,u"னூ"  ,u"னெ"  ,u"னே"  ,u"னை"  ,u"னொ"  ,u"னோ"  ,u"னௌ",
u"ய"  ,u"யா"  ,u"யி"  ,u"யீ"  ,u"யு"  ,u"யூ"  ,u"யெ"  ,u"யே"  ,u"யை"  ,u"யொ"  ,u"யோ"  ,u"யௌ",
u"ர"  ,u"ரா"  ,u"ரி"  ,u"ரீ"  ,u"ரு"  ,u"ரூ"  ,u"ரெ"  ,u"ரே"  ,u"ரை"  ,u"ரொ"  ,u"ரோ"  ,u"ரௌ",
u"ல"  ,u"லா"  ,u"லி"  ,u"லீ"  ,u"லு"  ,u"லூ"  ,u"லெ"  ,u"லே"  ,u"லை"  ,u"லொ"  ,u"லோ"  ,u"லௌ" ,
u"வ"  ,u"வா"  ,u"வி"  ,u"வீ"  ,u"வு"  ,u"வூ"  ,u"வெ"  ,u"வே"  ,u"வை"  ,u"வொ"  ,u"வோ"  ,u"வௌ" ,
u"ழ"  ,u"ழா"  ,u"ழி"  ,u"ழீ"  ,u"ழு"  ,u"ழூ"  ,u"ழெ"  ,u"ழே"  ,u"ழை"  ,u"ழொ"  ,u"ழோ"  ,u"ழௌ" ,
u"ள"  ,u"ளா"  ,u"ளி"  ,u"ளீ"  ,u"ளு"  ,u"ளூ"  ,u"ளெ"  ,u"ளே"  ,u"ளை"  ,u"ளொ"  ,u"ளோ"  ,u"ளௌ" ]


def classify_words(word):
    uyir=mei=uyirmei=ayutham=vada_mozhi=0
    
    vallinam=mellinam=idayinam=0
    
    letters=utf8.get_letters(word)
        
    for letter in letters:
        
        if letter in uyir_letters:
            uyir+=1
        elif letter in mei_letters:
            mei+=1
        elif letter in aytham_letter:
            ayutham+=1
        elif letter in uyirmei_letters:
            uyirmei+=1
        else:
            vada_mozhi+=1
        
            
            
        if letter in vallinam_letters:
            vallinam+=1
        elif letter in mellinam_letters:
            mellinam+=1
        elif letter in idayinam_letters:
            idayinam+=1
            
    return uyir,mei,uyirmei,ayutham,vada_mozhi,vallinam,mellinam,idayinam
            
            
    #print("Uyir:",uyir,"mei:",mei,"uyirmei:",uyirmei,"ayutham:",ayutham," Vada_mozhi:",vada_mozhi)
    #print("vallinam:",vallinam,"mellinam",mellinam,"idaiyinam:",idayinam)
#classify_words("ஸ்ரீஜய")