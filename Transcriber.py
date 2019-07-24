#
#  Transcriber.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#

import copy


def RealMovesOnly(history):
    """Converts a relative move history to an absolute move history

    When the history is initially written, each move is relative to the face
        currently facing "forward". This function takes the cube rotations out
        and re-writes the moves to be relative to one face.

    Args:
        history (:obj:`list` of str): History of moves

    Returns:
        (:obj:`list` of str): History of moves without cube rotations
    """

    # relative move : absolute move
    dicXC = {'UC': 'FC', 'UCC': 'FCC', 'DC': 'BC',
             'DCC': 'BCC', 'LC': 'LC', 'LCC': 'LCC',
             'RC': 'RC', 'RCC': 'RCC', 'FC': 'DC',
             'FCC': 'DCC', 'BC': 'UC', 'BCC': 'UCC',
             'XC': 'XC', 'XCC': 'XCC', 'YC': 'ZC',
             'YCC': 'ZCC', 'ZC': 'YCC', 'ZCC': 'YC'
             }

    dicXCC = {'UC': 'BC', 'UCC': 'BCC', 'DC': 'FC',
              'DCC': 'FCC', 'LC': 'LC', 'LCC': 'LCC',
              'RC': 'RC', 'RCC': 'RCC', 'FC': 'UC',
              'FCC': 'UCC', 'BC': 'DC', 'BCC': 'DCC',
              'XC': 'XC', 'XCC': 'XCC', 'YC': 'ZCC',
              'YCC': 'ZC', 'ZC': 'YC', 'ZCC': 'YCC'
              }

    dicYC = {'UC': 'UC', 'UCC': 'UCC', 'DC': 'DC',
             'DCC': 'DCC', 'LC': 'FC', 'LCC': 'FCC',
             'RC': 'BC', 'RCC': 'BCC', 'FC': 'RC',
             'FCC': 'RCC', 'BC': 'LC', 'BCC': 'LCC',
             'XC': 'ZCC', 'XCC': 'ZC', 'YC': 'YC',
             'YCC': 'YCC', 'ZC': 'XC', 'ZCC': 'XCC'
             }

    dicYCC = {'UC': 'UC', 'UCC': 'UCC', 'DC': 'DC',
              'DCC': 'DCC', 'LC': 'BC', 'LCC': 'BCC',
              'RC': 'FC', 'RCC': 'FCC', 'FC': 'LC',
              'FCC': 'LCC', 'BC': 'RC', 'BCC': 'RCC',
              'XC': 'ZC', 'XCC': 'ZCC', 'YC': 'YC',
              'YCC': 'YCC', 'ZC': 'XCC', 'ZCC': 'XC'
              }

    dicZC = {'UC': 'LC', 'UCC': 'LCC', 'DC': 'RC',
             'DCC': 'RCC', 'LC': 'DC', 'LCC': 'DCC',
             'RC': 'UC', 'RCC': 'UCC', 'FC': 'FC',
             'FCC': 'FCC', 'BC': 'BC', 'BCC': 'BCC',
             'XC': 'YC', 'XCC': 'YCC', 'YC': 'XCC',
             'YCC': 'XC', 'ZC': 'ZC', 'ZCC': 'ZCC'
             }

    dicZCC = {'UC': 'RC', 'UCC': 'RCC', 'DC': 'LC',
              'DCC': 'LCC', 'LC': 'UC', 'LCC': 'UCC',
              'RC': 'DC', 'RCC': 'DCC', 'FC': 'FC',
              'FCC': 'FCC', 'BC': 'BC', 'BCC': 'BCC',
              'XC': 'YCC', 'XCC': 'YC', 'YC': 'XC',
              'YCC': 'XCC', 'ZC': 'ZC', 'ZCC': 'ZCC'
              }

    hisCopy = copy.deepcopy(history)
    size = len(hisCopy)
    for i in range(size):			# upon finding a cube rotation, every move
        if hisCopy[i] == 'XC':		# or rotation afterwards is transcribed
            for x in range(i+1, size):
                hisCopy[x] = dicXC[hisCopy[x]]
        elif hisCopy[i] == 'XCC':
            for x in range(i+1, size):
                hisCopy[x] = dicXCC[hisCopy[x]]
        elif hisCopy[i] == 'YC':
            for x in range(i+1, size):
                hisCopy[x] = dicYC[hisCopy[x]]
        elif hisCopy[i] == 'YCC':
            for x in range(i+1, size):
                hisCopy[x] = dicYCC[hisCopy[x]]
        elif hisCopy[i] == 'ZC':
            for x in range(i+1, size):
                hisCopy[x] = dicZC[hisCopy[x]]
        elif hisCopy[i] == 'ZCC':
            for x in range(i+1, size):
                hisCopy[x] = dicZCC[hisCopy[x]]

    undesireables = ['XC', 'XCC', 'YC', 'YCC', 'ZC', 'ZCC']
    movesOnly = []
    for i in hisCopy:				# write every move in hisCopy to movesOnly except for cube rotations,
        if i in undesireables:		# thereby making a list of absolute moves only
            pass
        else:
            movesOnly.append(i)
    return movesOnly


def Compress(history):
    """Compresses redundant moves to be more efficient

    Args:
        history (:obj:`list` of str): History of moves with redundancies

    Returns:
        (:obj:`list` of str): Moves without redundancies
    """
    i = 0
    while i < len(history)-1:
        change = True
        while change and i < len(history)-1:			# allows us to assume the current element is at least 1 from the end
            equiv1 = history[i] == history[i+1]			# stores bool for if element i equals the next element in equiv1
            if len(history)-i >= 3:						# if current element is more than 1 element from the end
                equiv2 = history[i] == history[i+2]		# stores bool for if element i equals the next-next element in equiv2
            else:										# if current element is fewer than 2 elements from the end...
                equiv2 = False							# there is no equivalence for the next-next element
            if len(history)-i >= 4:						# if the current element is more than 2 elements from the end
                equiv3 = history[i] == history[i+3]		# stores bool for if current element equals next-next-next element in equiv3
            else:										# if the current element is fewer than 3...
                equiv3 = False							# there is no equivalence for the next-next-next element
            if equiv1 and equiv2 and equiv3:			# if the current element is the same as the next 3
                del history[i]							# constitutes 360 deg so all four are removed
                del history[i]
                del history[i]
                del history[i]

            elif history[i][0] == history[i+1][0] and not equiv1:	# else if the first letter of the current element equals " " " " second
                del history[i]										# 	and the elements themselves are not equal
                del history[i]										# constitutes a move and an opposite move. both are removed

            elif equiv1 and equiv2:							# otherwise, if the current element equals the next two
                if len(history[i]) == 2:					# constitutes 270 deg.
                    history[i] = history[i][0] + 'CC'		# change the current element to be opposite
                elif len(history[i]) == 3:
                    history[i] = history[i][0] + 'C'
                del history[i+1]							# delete the next two elements
                del history[i+1]

            else:									# if there are no available compressions in range
                change = False						# set change to false to move the current element by one
        i += 1

    i = 0
    while i < len(history)-1:							# second pass for 180 movements
        if history[i] == history[i+1]:				# combining like movements makes the motor movement more precise
            history[i] = history[i][0]+'180'
            del history[i+1]
        i += 1

    return history					# return the compressed history
