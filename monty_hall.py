import random
from typing import Literal

Strategy = Literal["switch", "stay"]


def simulate_monty_hall(strategy: Strategy) -> bool:
    """
    モンティホール問題のシミュレーションを1回実行する

    Args:
        strategy: "switch" (ドアを変更) または "stay" (ドアを変更しない)

    Returns:
        bool: 勝利した場合True、敗北した場合False
    """
    # 3つのドアのうち、1つに車がある（0, 1, 2のいずれか）
    car_door = random.randint(0, 2)

    # プレイヤーが最初に選ぶドア
    player_choice = random.randint(0, 2)

    # モンティが開けるドア（車がないドアで、プレイヤーが選んでいないドア）
    available_doors = [door for door in range(3)
                      if door != player_choice and door != car_door]
    monty_opens = random.choice(available_doors)

    # 戦略に応じて最終的な選択を決定
    if strategy == "switch":
        # ドアを変更：プレイヤーの選択でもモンティが開けたドアでもないドア
        final_choice = [door for door in range(3)
                       if door != player_choice and door != monty_opens][0]
    else:  # strategy == "stay"
        # ドアを変更しない：最初の選択のまま
        final_choice = player_choice

    # 最終的な選択が車のドアと一致すれば勝利
    return final_choice == car_door


def run_simulation(strategy: Strategy, num_trials: int = 10000) -> dict:
    """
    モンティホール問題のシミュレーションを複数回実行する

    Args:
        strategy: "switch" または "stay"
        num_trials: シミュレーション回数

    Returns:
        dict: 結果の統計情報
    """
    wins = sum(simulate_monty_hall(strategy) for _ in range(num_trials))
    win_rate = wins / num_trials

    return {
        "strategy": strategy,
        "trials": num_trials,
        "wins": wins,
        "losses": num_trials - wins,
        "win_rate": win_rate
    }


def main():
    """メイン関数：両方の戦略でシミュレーションを実行して結果を表示"""
    print("=" * 60)
    print("モンティホール問題シミュレーション")
    print("=" * 60)
    print()

    num_trials = 100

    # ドアを変更しない戦略
    print(f"シミュレーション回数: {num_trials:,}回\n")

    stay_results = run_simulation("stay", num_trials)
    print("【戦略1: ドアを変更しない（STAY）】")
    print(f"  勝利: {stay_results['wins']:,}回")
    print(f"  敗北: {stay_results['losses']:,}回")
    print(f"  勝率: {stay_results['win_rate']:.2%}")
    print()

    # ドアを変更する戦略
    switch_results = run_simulation("switch", num_trials)
    print("【戦略2: ドアを変更する（SWITCH）】")
    print(f"  勝利: {switch_results['wins']:,}回")
    print(f"  敗北: {switch_results['losses']:,}回")
    print(f"  勝率: {switch_results['win_rate']:.2%}")
    print()

    # 結論
    print("=" * 60)
    print("結論:")
    print(f"  ドアを変更する戦略の方が約 {switch_results['win_rate'] / stay_results['win_rate']:.2f}倍 勝ちやすい！")
    print("  理論値: 変更しない=33.3%, 変更する=66.7%")
    print("=" * 60)


if __name__ == "__main__":
    main()
