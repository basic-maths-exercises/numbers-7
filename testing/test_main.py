try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        inputs, outputs, num = [], [], ""
        for i in range(1,400) :
            if (i+10)%100==0 : num = num.replace("LXXX","IC").replace("IX","")
            elif i%100==0 : num = num.replace("IC","C").replace("IX","")
            elif (i+10)%50==0 : num = num.replace("XXX","IL").replace("IX","")
            elif i%50==0 : num = num.replace("IL","L").replace("IX","")
            elif (i+1)%10==0 : num = num.replace("VIII","IX")
            elif i%10==0 : num = num.replace("IX","X")
            elif (i+1)%5==0 : num = num.replace("III","IV")
            elif i%5==0 : num = num.replace("IV","V")
            else : num = num + "I"
            inputs.append((i,))
            outputs.append( num ) 
        assert( fc.check_func( 'romanNumeral', inputs, outputs ) ) 
