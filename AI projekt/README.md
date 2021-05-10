# **Pong: lätt AI vs smart AI**

<img src="https://github.com/abbindustrigymnasium/ai-dataanalys-AbbMyBjo/blob/main/AI%20projekt/Screenshot%20(13).png" alt="Pong" width="300"/>

Jag har gjort spelet pong i python. Det jag började med var att bygga upp hela miljön för spelet för att ha något att utgå från när jag skulle lära min AI att spela.
För att stänga av spelet trycker man på tangenten "Q". När AI:n inte är aktiverad styr man padeln med antingen pil upp och pil ned eller "W" och "S". Den som når 5 poäng först vinner spelet. Poäng får man om motståndaren missar bollen och den går vidare in i väggen bakom padeln.

<img src="https://github.com/abbindustrigymnasium/ai-dataanalys-AbbMyBjo/blob/main/AI%20projekt/Screenshot%20(14).png" alt="Pong" width="300"/>

Slutprodukten ska vara en AI som spelar mot en "dum AI". Den dumma AI:n följer bollens rörelser med hjälp av tre rader kod. Om bollen går uppåt gör också padeln det, samma om bollen går nedåt.

Den "smarta" AI:n lär sig spelet med hjälp av ett neuralt nätverk och 200 000 rader testdata att analysera. Det neurala nätverket ska ge en output på 1 eller 0 vilket kommer avgöra om padeln går uppåt eller nedåt.
