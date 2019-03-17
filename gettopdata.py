import json
import datetime
import time
import matplotlib.pyplot as plt

date=datetime.datetime.now().strftime('%G-%m-%d %H:%M:%S')
date = time.strptime(date, '%Y-%m-%d %H:%M:%S')

genres={}
performances={}
discounts={}
agecat={}
upcoming={}
files=["data_2012.txt","data_2013.txt","data_2014.txt","data_2015.txt","data_2016.txt","data_2017.txt","data_2018.txt","data_2019.txt"]
for file in files:
    print("Reading file: "+file)
    with open(file) as json_file:
        data = json.load(json_file)
        for p in data:
            if( p["genre"] in genres):
                counter= genres[p["genre"]]+1
                genres[p["genre"]]=counter
            else:
                genres[p["genre"]]=1
            i=0
            avshows={}
            for x in p["performances"]:
                if(file== "data_2019.txt"):
                    i=i+1
                    date2=time.strptime(x["start"], '%Y-%m-%d %H:%M:%S')
                    if(date2>date):
                        avshows[p["title"]+"_"+str(i)]=x
                        upcoming[p["genre"]]=avshows
                if( p["genre"] in performances):
                    counter= performances[p["genre"]]+1
                    performances[p["genre"]]=counter
                else:
                    performances[p["genre"]]=1
            discount={}
            for x in p["discounts"]:
                if( x in discount  and x== True ):
                    counter= discount[x]+1
                    discount[x]=counter
                else:
                    discount[x]=1
            discounts[p["genre"]]=discount
            if(file)== "data_2019.txt":
                agecat[p["title"]]=p["age_category"]

data={"Genres":genres,"Performances":performances,"Discounts": discounts,"Age Categories": agecat,"Upcoming": upcoming}
with open('stats.json', 'w') as f:  # writing JSON object
    json.dump(data,f)

print("Genres:")
print(genres)
print("Performances:")
print(performances)
print("Discounts:")
print(discounts)
print("Age Categories:")
print(agecat)
print("Upcoming")
print(upcoming)

# Graph for Genres - just for fun
#plt.bar(range(len(genres)), list(genres.values()), align='center')
#plt.xticks(range(len(genres)), list(genres.keys()),rotation="vertical")
#plt.show()
