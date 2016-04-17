#-----Python
#x = true_value if condition else false_value
x,y = 5,8
a = "yes" if x>y else "no" if y%2 == 0 else "may be"
a = "yes" if x<y else "no" if y%2 == 0 else "may be"
a = "yes" if x == y else "no" if x%2 == 0 else "maybe"


"""
-----JavaScript
var x=5, y=8, a;
a = x>y ? "yes" : (y%2 == 0 ? "no" : "may be")
a = x<y ? "yes" : (y%2 == 0 ? "no" : "may be")
a = x==y ? "yes" : (x%2 == 0 ? "no" : "may be")

-----Java
int x=5,y=8;       
String a;  
a = x>y ? "yes" : (y%2 == 0 ? "no" : "may be");
a = x<y ? "yes" : (y%2 == 0 ? "no" : "may be");
a = x==y ? "yes" : (x%2 == 0 ? "no" : "may be");  
"""
