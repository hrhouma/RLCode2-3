import pickle
import matplotlib.pyplot as plt
import numpy as np

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size), 'valid') / window_size

def visualize_results():
    with open('experiment_results.pkl', 'rb') as f:
        results = pickle.load(f)

    plt.figure(figsize=(12, 8))
    for alpha, rewards in results.items():
        smoothed_rewards = moving_average(rewards, 50)
        plt.plot(smoothed_rewards, label=f'α = {alpha}')

    plt.xlabel('Episodes')
    plt.ylabel('Average Reward (Moving Average)')
    plt.title('Impact of Learning Rate (α) on Q-Learning Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('learning_rate_impact.png')
    plt.show()

if __name__ == "__main__":
    visualize_results()
