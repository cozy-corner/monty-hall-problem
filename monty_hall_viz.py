import matplotlib.pyplot as plt
import matplotlib
from monty_hall import run_simulation

# 日本語フォント設定（macOS用）
matplotlib.rcParams['font.family'] = ['Hiragino Sans', 'Arial Unicode MS']


def visualize_results():
    """シミュレーション結果をグラフで視覚化"""
    num_trials = 100

    # 両方の戦略でシミュレーション実行
    stay_results = run_simulation("stay", num_trials)
    switch_results = run_simulation("switch", num_trials)

    # グラフの作成
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # グラフ1: 勝率の比較（棒グラフ）
    strategies = ['変更しない\n(STAY)', '変更する\n(SWITCH)']
    win_rates = [stay_results['win_rate'] * 100, switch_results['win_rate'] * 100]
    theoretical_rates = [33.3, 66.7]

    x = range(len(strategies))
    width = 0.35

    bars1 = ax1.bar([i - width/2 for i in x], win_rates, width,
                    label='シミュレーション結果', color='#3498db', alpha=0.8)
    bars2 = ax1.bar([i + width/2 for i in x], theoretical_rates, width,
                    label='理論値', color='#e74c3c', alpha=0.8)

    ax1.set_ylabel('勝率 (%)', fontsize=12)
    ax1.set_title('モンティホール問題：戦略別の勝率', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(strategies)
    ax1.legend()
    ax1.set_ylim(0, 100)
    ax1.grid(axis='y', alpha=0.3)

    # 棒グラフの上に数値を表示
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=10)

    # グラフ2: 勝敗の内訳（円グラフ）
    fig2, (ax2_1, ax2_2) = plt.subplots(1, 2, figsize=(14, 6))

    # STAY戦略の円グラフ
    colors_stay = ['#e74c3c', '#95a5a6']
    ax2_1.pie([stay_results['wins'], stay_results['losses']],
              labels=['勝利', '敗北'],
              autopct='%1.1f%%',
              colors=colors_stay,
              startangle=90,
              textprops={'fontsize': 12})
    ax2_1.set_title(f'変更しない戦略\n({num_trials:,}回試行)',
                    fontsize=14, fontweight='bold')

    # SWITCH戦略の円グラフ
    colors_switch = ['#2ecc71', '#95a5a6']
    ax2_2.pie([switch_results['wins'], switch_results['losses']],
              labels=['勝利', '敗北'],
              autopct='%1.1f%%',
              colors=colors_switch,
              startangle=90,
              textprops={'fontsize': 12})
    ax2_2.set_title(f'変更する戦略\n({num_trials:,}回試行)',
                    fontsize=14, fontweight='bold')

    plt.tight_layout()

    # 画像として保存
    plt.savefig('monty_hall_results.png', dpi=150, bbox_inches='tight')
    print("グラフを 'monty_hall_results.png' として保存しました")

    plt.show()


if __name__ == "__main__":
    visualize_results()
