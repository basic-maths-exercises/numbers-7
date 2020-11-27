# Roman numerals

You now have all the information you need to convert numbers into any base of your choosing.  You can thus throw off the chains of base ten and start the life of the mind by focussing on the Platonic ideals for the natural numbers.  In other words, you can see the numbers in all their glory rather than the shadows of these objects that are cast on the wall of the cave by the representation of them in base ten!  

My tongue was firmly in my cheek as I wrote the previous sentence.  My point with all this stuff about Plato, however, is that it is easy to forget that "simple" ideas such as the Arabic system of number that we learned in primary school were not given to us by "nature."  Arabic numerals were instead introduced to Europe through the writings of the Middle Eastern mathematicians al-Khwarizmi and al-Kindi in about the 12th century.  Furthermore, this new system represented a profound break with previous methods of counting.  Furthermore, as discussed in the video below the development of base ten numbers is far from inevitable:

https://www.youtube.com/watch?v=l4bmZ1gRqCc

Lets thus consider the Roman number system that we used in Europe before the Arabic system of number.  As you are probably aware in the Roman number system I is used to represent one, V is used to represent five, X is used to represent ten, L is used to represent fifty and C is used to represent one hundred.  The Roman numeral CCCLXXVI therefore represents:

![](https://render.githubusercontent.com/render/math?math=100+100+100+50+10+10+5+1=376)

In the Roman system of number, unlike the Arabic one, multiplication not is used when constructing the final number from the symbols that are written down.  The numbers for the various symbols that appear in a Roman numeral are instead just added together.  There is, however, one exception to this rule, which is that the pairs of symbols IV, IX, IL and IC are used to represent the numbers 4, 9, 40 and 90.  If we have the number CICIV this is:

![](https://render.githubusercontent.com/render/math?math=100+90+4=194)

__To see if you have understood this idea see if you can complete the function called `romanNumeral` in `main.py`__.  This function takes as input an integer `N` as that is less than 399.  It should return the roman numeral representation for that number.  To get you started I have written code to work out the parts of the numeral that will include the characters C, L and X.  __You will need to extend the code to generate the parts to generate any Vs and Is that are required.__
