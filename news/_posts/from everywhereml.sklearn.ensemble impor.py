from everywhereml.sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = RandomForestClassifier(n_estimators=7, max_leaf_nodes=20)
clf.fit(X_train, y_train)

print('Score: %.2f' % clf.score(X_test, y_test))


