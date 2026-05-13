import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)# Is used for creating same random numbers every time the program runs. 
N=1000
income=np.random.randint(2000, 15000, N)
savings=np.random.randint(0, 50000 , N)
expenses=np.random.randint(1000, 5000, N)
family_size=np.random.randint(1,6, N)
years_employed=np.random.randint(0, 20, N)
age=np.random.randint(21, 65, N)
rent=np.random.randint(500, 3000 , N)
debt=np.random.randint(0, 2000, N)

# target
disposable_income=income - expenses - rent - debt
#disposable_income=np.maximum(disposable_income, 0) I removed this feature because it was breaking the value if it was negative to 0 and this makes the value to have non linear relationship with outputs.
loan_amount=(
             savings * 0.3 +
             years_employed * 500 -
             family_size * 2000
             )


#loan_amount=np.maximum(loan_amount,0)
dataframe=pd.DataFrame({
    'income': income,
    'savings': savings,
    'expenses': expenses,
    'family_size': family_size,
    'years_employed': years_employed,
    'age': age,
    'rent': rent,
    'debt': debt,
    #'disposable_income':disposable_income, I removed this feature because it sometimes get negative and sometimes positive and this behavior makes a non linear relationship and model can't predict it perfectly. 
    'loan_amount': loan_amount
})
dataframe.to_csv('dataframe.csv', index=False)
# model training
X=dataframe.drop('loan_amount', axis=1) #all columns EXCEPT loan_amount
y=dataframe['loan_amount'] #only loan_amount column
X=np.array(X)
y=np.array(y)
with open('features.txt', 'w') as f:
    for feature ,output in zip(X , y):
        f.write(str(feature) + ',' + str(output) + '\n')

X_train=X[:800]
y_train=y[:800]
X_test=X[800:]
y_test=y[800:]
X_train_mean=np.mean(X_train, axis=0)# axis=0 means np should calculate the mean for each column accross all rows.[mean_income, mean_savings, mean_age]
X_train_std=np.std(X_train, axis=0) + 1e-8 # axis=0 → column-wise --- axis=1 → row-wise
X_train=(X_train - X_train_mean)/X_train_std 
X_test=(X_test - X_train_mean)/X_train_std 
y_train_mean=np.mean(y_train)
y_train_std=np.std(y_train) + 1e-8
y_train=(y_train - y_train_mean)/y_train_std 

def cost(y,y_pred):
    error=y_pred - y
    cost=np.mean(error**2)/2
    return cost

w=np.zeros(X.shape[1])
b=0
lr=0.001
prev_cost=float('inf')
for epoch in range(5000):
    y_pred_train=np.dot(X_train,w)+b
    dw=(1/len(X_train))*np.dot(X_train.T, (y_pred_train - y_train))
    db=(1/len(X_train))*np.sum(y_pred_train - y_train)
    current_cost=cost(y_train,y_pred_train)
    #if prev_cost - current_cost < 0.00001: # shows How big is the gradient update? I removed this condition because i let the model to learn perfectly .
       # break
    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Cost: {current_cost}")
    w=w-lr*dw
    b=b-lr*db

y_pred_test=np.dot(X_test,w)+b
y_pred_test=y_pred_test*y_train_std + y_train_mean #because I scaled (normalized) the target y_train before training,so now I must convert predictions back to the original scale.
y_pred_test=np.maximum(y_pred_test,0)
mae = np.mean(np.abs(y_pred_test - y_test))
print("MAE:", mae)

with open('test_predictions.txt', 'w') as f:
    for pred, actual in zip(y_pred_test, y_test):
        f.write(f'Predicted: {pred}, Actual: {actual}\n')


plt.scatter(y_test, y_pred_test, alpha=0.6)

# perfect prediction line
plt.plot([min(y_test), max(y_test)],
         [min(y_test), max(y_test)],
         linestyle='--')

plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()

# Now it's time to save the model:
import pickle # pickle is a python_builtin way to save and load objects
model_data={
    "w":w,
    "b":b,
    "X_mean":X_train_mean,
    "X_std":X_train_std,
    "Y_mean":y_train_mean,
    "Y_std":y_train_std
}
with open("model/model.pkl","wb") as f:
    pickle.dump(model_data,f)