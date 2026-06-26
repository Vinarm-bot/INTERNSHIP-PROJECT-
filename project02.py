
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()

X = iris.data      
y = iris.target    

print("Dataset Loaded Successfully")
print("Number of Samples:", len(X))
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report")
print(classification_report(y_test, y_pred))