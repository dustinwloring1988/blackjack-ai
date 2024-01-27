from blackjack_qlearning import BlackjackQLearning

def evaluate_agent(agent, test_games=1000000):
    wins, losses, draws = 0, 0, 0

    for _ in range(test_games):
        print("-----")
        result = agent.play()
        print(result)
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            draws += 1

    return wins, losses, draws

def main():
    # Train the agent
    agent = BlackjackQLearning()
    episodes = 5000000
    agent.train(episodes)

    # Evaluate the agent
    test_games = 1000000
    wins, losses, draws = evaluate_agent(agent, test_games)

    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
    win_rate = wins / (wins + losses) * 100 if wins + losses > 0 else 0
    print(f"Win rate: {win_rate:.2f}%")

if __name__ == "__main__":
    main()