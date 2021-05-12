import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

parser = argparse.ArgumentParser(description='Game of Life Parameter')

parser.add_argument('--game-size',
                    default=100,
                    type=int,
                    help='the size of working field of game of life')
parser.add_argument('--initize-method',
                    default=1,
                    help='define the initial method of game of life')
parser.add_argument('--seed',
                    default=17,
                    help='define the random seed of initial matrix')
parser.add_argument('--generation-num',
                    default=200,
                    help='define how many generation you want')
parser.add_argument('--gen-interval',
                    default=50,
                    help='define hiow frequency you update')
# parser.add_argument('--critic',
#                     default=3,
#                     help='define bound of life exits')

args = parser.parse_args()

on = 255
off = 0


def life_judge(data, row, col):
    life_sum = 0
    for r in range(max(row-1, 0), min(row+2, args.game_size)):
        for c in range(max(col-1, 0), min(col+2, args.game_size)):
            if r == row and c == col:
                continue
            # print(r, c)
            if data[r, c] == on:
                life_sum += 1
    # print(life_sum)
    if life_sum > 3 or life_sum < 2:
        return off
    if life_sum == 3:
        return on
    if life_sum == 2 and data[row, col] == on:
        return on
    else:
        return off


def life_decay(frame_num, data, img, plt):
    plt.title(f'{frame_num} generation')
    data_next = data.copy()
    rows, cols = data.shape
    for row in range(rows):
        for col in range(cols):
            data_next[row, col] = life_judge(data, row, col)
    img.set_data(data_next)
    data[:] = data_next[:]
    return img


def game_update(data):
    update_interval = 50
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    img = ax.imshow(data, cmap='autumn', interpolation='nearest')
    ani = animation.FuncAnimation(fig, life_decay, fargs=(data, img, plt),
                                  frames=args.generation_num,
                                  interval=update_interval
                                  )
    plt.show()
    # return


def random_method(size=args.game_size, seed=args.seed):
    return np.random.choice([on, off], size=(size, size))


def main():
    start = random_method()
    # start = np.random.choice([on], size=(args.game_size, args.game_size))

    game_update(start)


if __name__ == '__main__':
    main()