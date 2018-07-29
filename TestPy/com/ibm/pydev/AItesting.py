from sklearn import svm

X = [[0, 0], [1, 1], [1, 0]]  # training samples     
y = [0, 1, 1]  # training target    
clf = svm.SVC()  # class     
clf.fit(X, y)  # training the svc model    
result = clf.predict([2, 2]) # predict the target of testing samples
tred = clf.predict([2, 0])     
print result  # target 
print tred 

import matplotlib.pyplot as plt    
labels='frogs','hogs','dogs','logs'    
sizes=15,20,45,10    
colors='yellowgreen','gold','lightskyblue','lightcoral'    
explode=0,0.1,0,0    
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)    
plt.axis('equal')    
plt.show() 

#import jieba  
#seg_list = jieba.cut("北京野生动物园轿车遭黑熊围堵")  
#print "Default Mode:", ' '.join(seg_list) 