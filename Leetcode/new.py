# Advanced Machine Learning Lab (Cycle 1)
# Name: [Your Name]
# Note: Sample code, replace random data with actual datasets if possible :)

# 1. Regression on House Prices (TensorFlow)
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

print("==== REGRESSION MODEL FOR HOUSE PRICES ====")

# just creating some random data for demo
X = np.random.rand(100,5)
y = X[:,0]*10 + X[:,1]*3 + np.random.rand(100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=20, verbose=1)
print("Test loss:", model.evaluate(X_test, y_test))


# 2. Classification on Heart Disease (using ensemble)
from sklearn.ensemble import RandomForestClassifier

print("\n==== HEART DISEASE UCI CLASSIFICATION ====")

# replace this random data with real UCI data (pd.read_csv)
X = np.random.rand(200, 13)
y = np.random.randint(0, 2, 200)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)
print("Accuracy:", clf.score(X_test, y_test))


# 3. Q-Learning for Tic-Tac-Toe (simple ver)
print("\n==== Q-LEARNING TICTACTOE AGENT ====")

q_table = {}
alpha = 0.2
gamma = 0.95
epsilon = 0.3

def random_board():
    # Start with empty board
    return tuple([' ']*9)

def select_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(0,9)
    q = q_table.get(state, np.zeros(9))
    return np.argmax(q)

def update_q(state, action, reward, next_state):
    q = q_table.get(state, np.zeros(9))
    next_q = np.max(q_table.get(next_state, np.zeros(9)))
    q[action] += alpha * (reward + gamma * next_q - q[action])
    q_table[state] = q

def train(episodes=50):
    for i in range(episodes):
        state = random_board()
        for j in range(9):
            a = select_action(state)
            new_state = list(state)
            new_state[a] = 'X'
            reward = 0
            done = False
            update_q(state, a, reward, tuple(new_state))
            state = tuple(new_state)
            if done:
                break

train()
print("Done training simple TicTacToe agent.")

# END -- code is ready for submission, improve if needed!
