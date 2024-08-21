#.where and .select
import numpy as np
x=np.array([i for i in range(1,11)])
print(x)
print(np.where(x%2==0,'even','odd'))#np.where(condition,true,false)
condlist=[x<5,x>5]
choicelist=[x**2,x**3]
print(np.select(condlist,choicelist,default=[x]))#np.select(condlist=[....],choicelist[....],default[....])

