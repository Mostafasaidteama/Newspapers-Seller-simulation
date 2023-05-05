import random
import numpy as np
import matplotlib.pyplot as plt
buy_price = 0.5
Selling_Price = 0.7
gain = 0.2
scrap = 0.15
size_of_boundels=20
newspaper_purchased =size_of_boundels*3
cost_of_news_paper=newspaper_purchased*buy_price
type_of_newsday= []
demand= []
revenue= []
lost_profit= []
salvage_from_sale_of_scrap= []
daily_profit= []
revenue2= []
lost_profit2= []
salvage_from_sale_of_scrap2= []
boundels=[20,40,60,80,100,120]
list_revenue=[]
list_lost_profit=[]
list_salvage_from_sale_of_scrap=[]
totel_revenue2=[]
total_lost=[]
total_s=[]
total_c=[]
total_profit2=[]


def random_num():
    return random.uniform(0,100)

def get_type_of_newspaper():
  r1=random_num()
  if   r1>=1   and r1<=18:
       x='excellent'
  elif r1>=19 and r1<=60:
       x='good'                            
  elif r1>=61 and r1<=92:
       x='fair'
  else :
       x='poor'
  return x


def random_num2():
    return random.uniform(0,100)


def get_demand():
  r2=random_num2()
  #get demand if type_of_newsday is excellent
  if   get_type_of_newspaper()=='excellent' and  r2>=1   and r2<=7:
       d = 50
  elif get_type_of_newspaper()=='excellent' and  r2>=8   and r2<=15:
       d = 60
  elif get_type_of_newspaper()=='excellent' and  r2>=16  and r2<=27:
       d = 70    
  elif get_type_of_newspaper()=='excellent' and  r2>=28  and r2<=40:
       d = 80    
  elif get_type_of_newspaper()=='excellent' and  r2>=41  and r2<=62:
       d = 90
  elif get_type_of_newspaper()=='excellent' and  r2>=63  and r2<=85:
       d = 100
  elif get_type_of_newspaper()=='excellent' and  r2>=86  and r2<=93:
       d = 110
  else :
       d=120
  #get demand if type_of_newsday is good
  if   get_type_of_newspaper()=='good' and  r2>=1   and r2<=6:
       d = 40
  elif get_type_of_newspaper()=='good' and  r2>=7   and r2<=15:
       d = 50
  elif get_type_of_newspaper()=='good' and  r2>=16  and r2<=31:
       d = 60
  elif get_type_of_newspaper()=='good' and  r2>=32  and r2<=50:
       d = 70    
  elif get_type_of_newspaper()=='good' and  r2>=51  and r2<=78:
       d = 80    
  elif get_type_of_newspaper()=='good' and  r2>=79  and r2<=90:
       d = 90
  elif get_type_of_newspaper()=='good' and  r2>=92  and r2<=97:
       d = 100
  else :
       d=110

  #get demand if type_of_newsday is fair
  if   get_type_of_newspaper()=='fair' and  r2>=1  and r2<=15:
       d = 40
  elif get_type_of_newspaper()=='fair' and  r2>=16 and r2<=37:
       d = 50
  elif get_type_of_newspaper()=='fair' and  r2>=38 and r2<=65:
       d = 60
  elif get_type_of_newspaper()=='fair' and  r2>=66 and r2<=83:
       d = 70    
  elif get_type_of_newspaper()=='fair' and  r2>=84 and r2<=93:
       d = 80    
  elif get_type_of_newspaper()=='fair' and  r2>=94 and r2<=98:
       d = 90
  else :
       d=100
  

  #get demand if type_of_newsday is poor
  if   get_type_of_newspaper()=='poor' and  r2>=1  and r2<=42:
       d = 40
  elif get_type_of_newspaper()=='poor' and r2>=43  and r2<=70:
       d = 50
  elif get_type_of_newspaper()=='poor' and  r2>=71 and r2<=84:
       d = 60
  elif get_type_of_newspaper()=='poor' and  r2>=85 and r2<=94:
       d = 70    
  elif get_type_of_newspaper()=='poor' and  r2>=95 and r2<=99:
       d = 80    
 
  else :
       d=90
  return d


for i in range (20) :      
    demand.append(get_demand())
    type_of_newsday.append(get_type_of_newspaper())

for day in range (20) :
     
     if(newspaper_purchased >= demand[day]): 
          revenue.append(demand[day]*Selling_Price)
     else:
          revenue.append(newspaper_purchased*Selling_Price)

     if(demand[day] > newspaper_purchased):
          lost_profit.append((demand[day]-newspaper_purchased)*gain)
     else:
           lost_profit.append(0)  

     if(demand[day] < newspaper_purchased):    
          salvage_from_sale_of_scrap.append((newspaper_purchased-demand[day])*scrap)
     else:
          salvage_from_sale_of_scrap.append(0)

     daily_profit.append((revenue[day])-(cost_of_news_paper)-(lost_profit[day])+(salvage_from_sale_of_scrap[day])) 
     totel_revenue=sum(revenue)
     total_lost_profit=sum(lost_profit)
     total_solvage=sum(salvage_from_sale_of_scrap)
     total_profit = sum(daily_profit)

#to find the optimal number of papers the seller should purchase 
for i in range (6):
 for day in range (20) :
     
     if(boundels[i] >= demand[day]): 
         revenue2.append(demand[day]*Selling_Price)
     else:
          revenue2.append(boundels[i]*Selling_Price)

     if(demand[day] > boundels[i]):
          lost_profit2.append((demand[day]-boundels[i])*gain)
     else:
           lost_profit2.append(0)  

     
     if(demand[day] < boundels[i]):    
          salvage_from_sale_of_scrap2.append((boundels[i]-demand[day])*scrap)
     else:
         salvage_from_sale_of_scrap2.append(0)
     
#to find total revenue of each boundels
 totel_revenue2.append(sum(revenue2))
 if(i==0) :       
     list_revenue.append(totel_revenue2[i])
 else:
     list_revenue.append(totel_revenue2[i]-totel_revenue2[i-1])

#to find total lost profit of each boundels
 total_lost.append(sum(lost_profit2))
 if(i==0) :       
     list_lost_profit.append(total_lost[i])
 else:
     list_lost_profit.append(total_lost[i]-total_lost[i-1]) 

#to find total salvage from sale of scrap of each boundels
 total_s.append(sum(salvage_from_sale_of_scrap2))
 if(i==0) :       
  list_salvage_from_sale_of_scrap.append(total_s[i])
 else:
     list_salvage_from_sale_of_scrap.append(total_s[i]-total_s[i-1])
     
#to find total profit of each boundels
 total_profit2.append((list_revenue[i])-(boundels[i]*0.5*20)-(list_lost_profit[i])+(list_salvage_from_sale_of_scrap[i])) 
#to find max_profit of in all boundels
 max_profit=max(total_profit2)
#to find the optimal number of papers the seller should purchase
 if max_profit==list_revenue[i]-(boundels[i]*0.5*20)-(list_lost_profit[i])+(list_salvage_from_sale_of_scrap[i]):
     optimal=boundels[i]



d = {}
for i in range(20):
    d[i+1] = [type_of_newsday[i], demand[i], revenue[i], lost_profit[i], salvage_from_sale_of_scrap[i],daily_profit[i]]
print (" {:<5}  {:<15} {:<10} {:<10} {:<20} {:<30} {:<20}".format("day","type_of_newsday", "demand", "revenue", "lost_profit", "salvage_from_sale_of_scrap","daily_profit"))
for k, v in d.items():
    type_of_newsday,  demand, revenue, lost_profit, salvage_from_sale_of_scrap,daily_profit = v
    print (" {:<5}  {:<15} {:<10} {:<10} {:<20} {:<30} {:<20}".format(k,type_of_newsday, demand, revenue, lost_profit, salvage_from_sale_of_scrap, daily_profit ))





print("totel revenue : ",totel_revenue,"\n")
print("total lost profit : ",total_lost_profit,"\n")
print("total salvage from sale of scrap : ",total_solvage,"\n")
print("totl profit : ",total_profit,"\n")
print("average_profit : ",total_profit/20,"\n")


print("total revenue of each boundels : ",list_revenue,"\n")
print("total lost profit of each boundels : ",list_lost_profit,"\n")
print("total salvage from sale of scrap of each boundels : ",list_salvage_from_sale_of_scrap,"\n")
print("total profit of each boundels : ",total_profit2,"\n")
print("max profit is equal : ",max_profit,"\n")
print("the optimal number of papers the seller should purchase is : ",optimal,"\n")


#graphs
plt.hist(daily_profit,density = True, bins = 40)
plt.show()
plt.hist(demand,density = True, bins = 40)
plt.show()