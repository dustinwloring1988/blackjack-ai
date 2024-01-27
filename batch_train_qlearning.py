import threading
import csv
import pickle
from blackjack_qlearning import BlackjackQLearning

def train_and_evaluate(agent_params, save_path, lock):
    episodes = agent_params.pop('episodes')  # Remove 'episodes' from agent_params
    test_games = agent_params.pop('test_games')  # Remove 'test_games' from agent_params
    
    agent = BlackjackQLearning(**agent_params)
    agent.train(episodes)
    
    wins, losses, draws = evaluate_agent(agent, test_games)
    
    model_info = {
        'wins': wins,
        'losses': losses,
        'draws': draws,
        'model_file_name': save_path,
        'number_of_episodes': episodes,
        'number_of_test_games': test_games,
        **agent_params  # Include the rest of the agent_params
    }

    # Save the trained model
    with open(save_path, 'wb') as model_file:
        pickle.dump(agent, model_file)

    with lock:
        results.append(model_info)

def evaluate_agent(agent, test_games=1000000):
    wins, losses, draws = 0, 0, 0

    for _ in range(test_games):
        result = agent.play()
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            draws += 1

    return wins, losses, draws

def main():
    agents_params = [
        {'episodes': 50000, 'test_games': 10000, 'alpha': 0.1, 'gamma': 0.9, 'epsilon': 0.1},
        {'episodes': 10000, 'test_games': 20000, 'alpha': 0.2, 'gamma': 0.8, 'epsilon': 0.2},
        {'episodes': 120000, 'test_games': 15000, 'alpha': 0.2, 'gamma': 0.8, 'epsilon': 0.2},
        {'episodes': 120000, 'test_games': 15000, 'alpha': 0.3, 'gamma': 0.7, 'epsilon': 0.3},
        {'episodes': 120000, 'test_games': 15000, 'alpha': 0.25, 'gamma': 0.6, 'epsilon': 0.25},
        {'episodes': 120000, 'test_games': 150000, 'alpha': 0.25, 'gamma': 0.75, 'epsilon': 0.25},
        {'episodes': 600000, 'test_games': 150000, 'alpha': 0.25, 'gamma': 0.75, 'epsilon': 0.25},
        {'episodes': 800000, 'test_games': 150000, 'alpha': 0.25, 'gamma': 0.75, 'epsilon': 0.25},
        {'episodes': 1000000, 'test_games': 150000, 'alpha': 0.25, 'gamma': 0.75, 'epsilon': 0.25},
        {'episodes': 1500000, 'test_games': 150000, 'alpha': 0.25, 'gamma': 0.75, 'epsilon': 0.25},
        # Add more sets of parameters as needed
    ]

    lock = threading.Lock()
    threads = []

    for idx, agent_params in enumerate(agents_params):
        save_path = f'model_{idx}.pkl'
        thread = threading.Thread(target=train_and_evaluate, args=(agent_params, save_path, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Save results to CSV
    csv_columns = results[0].keys()
    csv_file_path = 'training_results.csv'

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(results)

if __name__ == '__main__':
    results = []  # Results list shared by threads
    main()
