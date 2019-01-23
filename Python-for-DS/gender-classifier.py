from sklearn import tree

#[height, weight, shoe size]

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
     [175,64,39],[166,65,40],[190,90,47],[177,70,40],
     [171,75,42],[181,85,43],[159,54,36]]

Y = ['male', 'male', 'female','female','male','male',
    'male', 'female','male', 'male', 'female']

# construct the -Decision Tree- classifier
clf = tree.DecisionTreeClassifier()

# train it 
clf = clf.fit(X,Y)

# store the result 
prediction = clf.predict([[190,70,43]])

# print the result into terminal
print prediction