from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
dataset = pd.DataFrame({
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Patrons': ['Some', 'Full', 'Some', 'Some', 'None', 'None', 'Some', 'Full', 'None', 'Some', 'Full', 'Full', 'Some', 'Full'],
    'Price': ['$$', '$', '$', '$', '$', '$$', '$$', '$', '$', '$$', '$$', '$', '$$', '$$'],
    'Hungry': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'WaitEstimate': ['0-10', '30-60', '0-10', '0-10', '0-10', '30-60', '0-10', '0-10', '0-10', '30-60', '0-10', '30-60', '30-60', '0-10'],
    'WillWait': ['No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Convert categorical variables to numerical values
dataset['Weather'] = dataset['Weather'].astype('category').cat.codes
dataset['Patrons'] = dataset['Patrons'].astype('category').cat.codes
dataset['Price'] = dataset['Price'].astype('category').cat.codes
dataset['Hungry'] = dataset['Hungry'].astype('category').cat.codes
dataset['WaitEstimate'] = dataset['WaitEstimate'].astype('category').cat.codes
dataset['WillWait'] = dataset['WillWait'].astype('category').cat.codes

# Split the dataset into features and target
X = dataset.drop('WillWait', axis=1)
y = dataset['WillWait']

# Create the decision tree classifier
clf = DecisionTreeClassifier(criterion='entropy')

# Train the decision tree classifier
clf.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(15,10))
plot_tree(clf, filled=True, feature_names=dataset.columns[:-1], class_names=['No', 'Yes'])
plt.show()
