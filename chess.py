import os
import argparse
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import grid


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument('N', help='the size of the chess board (int), default 8', type=int, default=8)
	parser.add_argument('start', help='row and column tuple for starting position. default is upper left corner: 0 0', nargs=2, type=int, metavar=('row', 'col'), default=(0,0))
	parser.add_argument('ceiling', help='the max iteration number after which the code breaks, to prevent run-away, default=1000', nargs='?', type=int, default=1000)

	args = parser.parse_args()
	N, (row, col), ceil = args.N, args.start , args.ceiling
	valid_N = (type(N)==int) * (N>2)

	if not valid_N:
		print('N must be an integer larger or equal to 3')

	else:

		figure_dir = os.path.join(os.getcwd(), 'figures')
		fdir = 'N='+str(N)
		current_dir = os.path.join(figure_dir, fdir)

		if not os.path.isdir(current_dir):
			os.makedirs(current_dir)
	
		chess = grid.chess_board(N=N, start_position=(row, col))

		while (chess.board[chess.end_position]==0) and (chess.move_number<ceil):
			chess.move()

		figname = 'final_N'+str(N)+'.png'
		fig = plt.figure(figsize=(8,8))
		plt.imshow(chess.board, cmap=mpl.cm.binary)
		plt.savefig(os.path.join(current_dir, figname))
		plt.close()

		figname = 'cover_N'+str(N)+'.png'
		fig = plt.figure(figsize=(8,8))
		plt.imshow(chess.snapshot.sum(axis=-1), cmap=mpl.cm.binary)
		plt.savefig(os.path.join(current_dir, figname))
		plt.close()

