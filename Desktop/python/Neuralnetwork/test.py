import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(8, 8)),  # 8x8の手書き数字画像
    tf.keras.layers.Dense(128, activation='relu', name='hidden_layer'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 学習前の重み
initial_weights = model.layers[1].get_weights()[0]

# 学習実行
digits = load_digits()
model.fit(digits.data.reshape(-1,8,8), digits.target, epochs=50)

# 学習後の重み
trained_weights = model.layers[1].get_weights()[0]

# 可視化
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
ax1.imshow(initial_weights[:, :40], cmap='viridis', aspect='auto')
ax2.imshow(trained_weights[:, :40], cmap='viridis', aspect='auto')
ax1.set_title('Initial Weights')
ax2.set_title('Trained Weights')
plt.matshow(digits.images[0])
plt.show()