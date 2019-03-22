import numpy as np
import scipy as sp
from scipy.signal import convolve2d
from knight import knight_moves_builder


class chess_board(object):


	def __init__(self, N, start_position):
		"""
		the N x N chess board
		"""
		
		# --- initiation
		self.board_size = N
		self.board = np.zeros((self.board_size, self.board_size), dtype=int)
		
		# --- populate starting position
		row, col = start_position
		self.board[row, col] = 1

		self.end_position = (self.board_size-1, self.board_size-1)

		self.valid_moves = knight_moves_builder()
		self.move_number = 0
		self.snapshot = self.board.copy()

		return



	def move(self):

		self.board = convolve2d(in1=self.board, in2=self.valid_moves, mode='same')
		
		# --- save a snapshot of current board
		current_snapshot = self.board.copy()
		current_snapshot[current_snapshot>0]=1
		self.snapshot = np.dstack((self.snapshot, current_snapshot))

		self.move_number += 1
		
		print('move {}'.format(self.snapshot.shape[-1]-1))
		
		return

