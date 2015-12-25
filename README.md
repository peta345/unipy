# unipy
This is Python3 module to parse of daigaku-unipa.  
this module maybe rely on [BeautifulSup](http://www.crummy.com/software/BeautifulSoup/) and [MechanicalSoup](https://github.com/hickford/MechanicalSoup), so you have to install these modules. 

## Installation

	git clone https://github.com/peta345/unipy.git  

Then, you add a 'unipy.py' directory  
unip.pyのURL=""には~Com00505AのURLをいれてください
## Example

```
#module import
import unipy.py

#login
url = unipy.login('your id', 'your password')

#Return Timetable as List
table = unipy.get_time_table(url)

#Return News as List
news = unipy.get_news(url)
```


