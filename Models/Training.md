# Things

En lugar de guardar el último modelo, podemos guardar el mejor usando un checkpoint. Ejemplo en Keras:

```python
cp = ModelCheckpoint('ErrorModel/model'+model_num+'.keras', save_best_only=True)
model1.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=L_RATE), metrics=[RootMeanSquaredError()])
model1.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=EPOCHS, callbacks=[cp])
```
