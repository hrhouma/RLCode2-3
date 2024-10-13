import gym
import numpy as np
from qlearning_agent import QLearningAgent
import pickle

def run_experiment(alpha, n_episodes=1000):
    env = gym.make('MountainCar-v0')
    agent = QLearningAgent(env, n_states=20*20, n_actions=3, alpha=alpha, gamma=0.99, epsilon=0.1)
    rewards = agent.train(n_episodes)
    env.close()
    return rewards

if __name__ == "__main__":
    alphas = [0.1, 0.3, 0.5, 0.7, 0.9]
    results = {}

    for alpha in alphas:
        print(f"Running experiment with alpha = {alpha}")
        rewards = run_experiment(alpha)
        results[alpha] = rewards

    with open('experiment_results.pkl', 'wb') as f:
        pickle.dump(results, f)

    print("Experiments completed. Results saved in 'experiment_results.pkl'")
