# Tamil_asai

Asai process is the important play role in the Tamil literature classification. Yaappilakkanam defined the rule for the literature like  
ADI - Lines  
SEER - WORD  
**ASAI - (NERASAI and NIRAYASAI) can be classified from the time duration taken to pronounce a letter.**   

As time consideration is clasified  

KURIL - This letters will take natural eye blinking time to pronounce  
NEDIL - This letters will take more than the natural eye blinking time to pronounce  
OTRU -  This letters will take less than the natural eye blinking time to pronounce.  
```python
Kuril = ["அ", "இ", "உ", "எ", "ஒ", "க", "ங", "ச", "ஞ", "ட", "ண", "த", "ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன", "கி", "ஙி", "சி", "ஞி", "டி", "ணி", "தி", "நி", "பி", "மி", "யி", "ரி", "லி", "வி", "ழி", "ளி", "றி", "னி", "கு", "ஙு", "சு", "ஞு", "டு", "ணு", "து", "நு",
             "பு", "மு", "யு", "ரு", "லு", "வு", "ழு", "ளு", "று", "னு", "கெ", "ஙெ", "செ", "ஞெ", "டெ", "ணெ", "தெ", "நெ", "பெ", "மெ", "யெ", "ரெ", "லெ", "வெ", "ழெ", "ளெ", "றெ", "னெ", "கொ", "ஙொ", "சொ", "ஞொ", "டொ", "ணொ", "தொ", "நொ", "பொ", "மொ", "யொ", "ரொ", "லொ", "வொ", "ழொ", "ளொ", "றொ", "னொ"]
             
 Nedil = ["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ", "ஔ", "கா", "ஙா", "சா", "ஞா", "டா", "ணா", "தா", "நா", "பா", "மா", "யா", "ரா", "லா", "வா", "ழா", "ளா", "றா", "னா", "கீ", "ஙீ", "சீ", "ஞீ", "டீ", "ணீ", "தீ", "நீ", "பீ", "மீ", "யீ", "ரீ", "லீ", "வீ", "ழீ", "ளீ", "றீ", "னீ", "கூ", "ஙூ", "சூ", "ஞூ", "டூ", "ணூ", "தூ", "நூ", "பூ", "மூ", "யூ", "ரூ", "லூ", "வூ", "ழூ", "ளூ", "றூ", "னூ", "கே", "ஙே", "சே", "ஞே", "டே",
             "ணே", "தே", "நே", "பே", "மே", "யே", "ரே", "லே", "வே", "ழே", "ளே", "றே", "னே", "கை", "ஙை", "சை", "ஞை", "டை", "ணை", "தை", "நை", "பை", "மை", "யை", "ரை", "லை", "வை", "ழை", "ளை", "றை", "னை", "கோ", "ஙோ", "சோ", "ஞோ", "டோ", "ணோ", "தோ", "நோ", "போ", "மோ", "யோ", "ரோ", "லோ", "வோ", "ழோ", "ளோ", "றோ", "னோ", "கௌ", "ஙௌ", "சௌ", "ஞௌ", "டௌ", "ணௌ", "தௌ", "நௌ", "பௌ", "மௌ", "யௌ", "ரௌ", "லௌ", "வௌ", "ழௌ", "ளௌ", "றௌ", "னௌ"]
             
             Otru = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்",
            "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்", "ஃ"]
 ```

**Rule for NIRAYASI - #NIRAI** 

**RULE 1:** TWO Kuril letters can come together or along with one or two OTRU letters  
**RULE 2:** ONE KURIL and ONE NEDIL letter can come together or along with one or two OTRU letters  

**Rule for NERASAI** - #NER  

**RULE 1:** Single KURIL letter can come alone or along with one or two OTRU letters  
**RULE 2:** Single NEDIL letter can come alone or along with one or two OTRU letters  

**Example**
```python
string = "அடுக்குகளை"
```
while parse the string into character. It will be
```python
['அ', 'டு','க்', 'கு', 'க', 'ளை']
```
அ - KURIL
டு - KURIL
க் - OTRU
கு - KURIL
க - KURIL
ளை - NEDIL


