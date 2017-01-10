# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime

format_a = "%m-%d-%Y"

datetime.strptime(date_start, format_a) - datetime.strptime(date_stop, format_a)
# datetime.timedelta(-937)

####b)  
date_start = '12312013'  
date_stop = '05282015' 

format_b = "%m%d%Y"

datetime.strptime(date_start, format_b) - datetime.strptime(date_stop, format_b)
# datetime.timedelta(-513)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

format_c = "%d-%b-%Y"

datetime.strptime(date_start, format_c) - datetime.strptime(date_stop, format_c)
# datetime.timedelta(-7850)

