''' 
1 Brawl Glove : 12 x Broze Bar (Level 3 )
                20 x Leather   (Level 3) 

1 Bronze Bar(Level 3) : 2 x Tin Ore (Level 3) 
                1 Copper Ore 

1 Leather(Level 3) : 2 x Thin Hide (Level 3) 
                      1 x Leather (Level 2) 


'''
import math      # importing math module

def Bronze_Bar_3(x) : # defining Bronze_Bar Level 3 function 
    
 # required tin ore level 3
    tin_ore_3 = 2 * x 
 # required copper ore level 2 
    copper_ore_2 = 1 * x  
 
    print (f'\'{tin_ore_3}\' Tin ore level 3',
          'and \'{copper_ore_2}\' Copper Ore Level 2 required.')
    
    

def Leather_3(x) : # defining Leather Level 3 function 
    
    thin_hide_3 = 2 * x # required thin_hide level 3
    leather_2 = 1 * x   # required leather level 2 
    
    # we can gather thin_hide level 3 from frogs 
    # from one frog we get 9 thin_hide level 3
    frog = math.ceil(thin_hide_3 / 9) # rounding upwards in case 
                                      # it's x % 9!= 0
    # we can get 9 level_2_leather from snakes. :)
    snake = math.ceil(leather_2 / 9)  # same as above
    
    print (f'\'{thin_hide_3}\' Thin hide level 3',
            'and {leather_2} Leather level 2 required.')
    print (f'You have to kill {frog} Frogs.')
    print (f'You have to kill {snake} Snakes.')
    


def Brawl_Glove_3 (x) : # This is our final function where 
                        # passing an argument will provide
                        # our desired answer. :)

    bronze_bar = x * 12 # we need 12 bronze_bar for each glove
    leather_3 = x * 20  # we need 20 level_3 leather for each glove
    
    Bronze_Bar_3(bronze_bar) # 
    Leather_3(leather_3) 
    
    pass 

required_glove = int (input ("How many gloves are required? "))
gloves_stored = int(input("How many gloves do you have ? "))        

Brawl_Glove_3(required_glove-gloves_stored)
    
    
