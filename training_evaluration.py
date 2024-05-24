# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')

# Predict using the model
y_pred = model.predict(X_test)

# Optionally, compare predicted vs actual values
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Years')
plt.ylabel('Predicted Years')
plt.title('Actual vs Predicted Years in Prison')
plt.show()
