import os
import sys
import time

def drawCake():
    cake = """
           ~                  ~                         
     *                   *                *       *     
                  *               *                     
  ~       *                *         ~    *             
              *       ~        *              *   ~     
                  )         (         )              *  
    *    ~     ) (_)   (   (_)   )   (_) (  *           
           *  (_) # ) (_) ) # ( (_) ( # (_)       *     
              _#.-#(_)-#-(_)#(_)-#-(_)#-.#_             
  *         .' #  # #  #  # # #  #  # #  # `.   ~     * 
           :   #    #  #  #   #  #  #    #   :          
    ~      :.       #     #   #     #       .:      *   
        *  | `-.__                     __.-' | *        
           |      `````'''''''''''`````      |         *
     *     |         | ||  |~)|~)  /         |          
   ~   *   |                                 | *        
   ~   *   |                                 | *        
           |      |~)||~)~|~| ||~\|\ \ /     |         *
   *    _.-|      |~)||~\ | |~|| /|~\ |      |-._       
      .'   '.      ~            ~           .'   `.  *  
  jgs :      `-.__                     __.-'      :     
       `.         `````'''''''''''`````         .'      
         `-.._                             _..-'        
              `````''''-----------''''`````"""
    for line in cake.split('\n'):
        print(line)
        time.sleep(0.1)

def drawTaeBo(interval):
    for i in range(10):
        print('@==(^ 0^)@   @(^0 ^)==@')
        time.sleep(interval)
        print('@=(^0^)=@    @=(^ 0 ^)=@')
        time.sleep(interval)
        print('@(^0 ^)==@   @==(^ 0^)@')
        time.sleep(interval)
        print('@=(^0^)=@    @=(^ 0 ^)=@')
        time.sleep(interval)

drawCake()
drawTaeBo(0.3)
print('========== H A P P Y B I R T H D A Y ==========')
drawTaeBo(0.1)
print('Anyway, happy birthday :)        --myself\n')
