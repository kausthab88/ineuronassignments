#print all even numbers
import logging as log

log.basicConfig(filename ='even_log.log',level = log.INFO, format = '%(asctime)s %(name)s %(levelname)s%(message)s')

def print_even(n):
    
    if n >100:
        log.error('user entered a value greater than 100')
        raise Exception('cant enter number greater than 100')
    else:
        even = [i for i in range(0,n+1) if i%2==0]
      
        return even

    
            
  
         