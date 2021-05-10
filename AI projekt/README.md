# **Pong: dum AI vs smart AI**

<img src="https://github.com/abbindustrigymnasium/ai-dataanalys-AbbMyBjo/blob/main/AI%20projekt/Screenshot%20(13).png" alt="Pong" width="300"/>

Jag har gjort spelet pong i python. Det jag började med var att bygga upp hela miljön för spelet för att ha något att utgå från när jag skulle lära min AI att spela.
För att stänga av spelet trycker man på tangenten "Q". När AI:n inte är aktiverad styr man padeln med antingen pil upp och pil ned eller "W" och "S". Den som når 5 poäng först vinner spelet. Poäng får man om motståndaren missar bollen och den går vidare in i väggen bakom padeln.
Det är tänkt att det ska finnas tre teman att välja mellan i spelet. 

<img src="https://github.com/abbindustrigymnasium/ai-dataanalys-AbbMyBjo/blob/main/AI%20projekt/Screenshot%20(14).png" alt="Pong" width="300"/>

Slutprodukten ska vara en AI som spelar mot en "dum AI". Den dumma AI:n följer bollens rörelser med hjälp av tre rader kod. Om bollen går uppåt gör också padeln det, samma om bollen går nedåt.

Den "smarta" AI:n lär sig spelet med hjälp av ett neuralt nätverk och 200 000 rader testdata att analysera. Det neurala nätverket ska ge en output på 1 eller 0 vilket kommer avgöra om padeln går uppåt eller nedåt.

För att skapa pong-miljön m.m. har jag tagit hjälp av en tutorial: https://www.101computing.net/pong-tutorial-using-pygame-getting-started/ och för själva AI:n har jag tagit hjälp av en youtube-video: https://www.youtube.com/watch?v=BSpXCRTOLJA&t=575s.

Lite mer om filerna som finns med i min github:

träningsvärden.py är till för att generera datat som det neurala nätverket ska träna med.

Pong.py är den huvudsakliga filen där den dumma AI:n och en spelare kan spela mot varandra. Där ska också den smarta AI:n spela när den är klar, istället för spelaren. Slutligen ska man kunna spela mot den smarta AI:n, när den har lärt sig tillräckligt bra om hur man spelar. 

AI_pong.py är till för att träna den smarta AI:n så att den blir bra nog. Man väver sedan ihop denna fil med pong.py.

Chopsic.ttf är en font som är tänkt att användas till ett tema av spelmiljön. 
De tre bildfilerna boll.png badboll.png och jordboll.png är också tänkta att vara olika teman, i detta fall olika utseenden på bollen i de olika temana.

De filerna som inte nämnts än är readme.md och två bildfiler. Alla dessa finns för att min README.md ska se bra ut.
