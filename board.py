#
# board.py (Final Project)
#
# A Board class for the Eight Puzzle
#
# name: Jake Bloomfeld  
# email: jtbloom@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: N/A
# partner's email: N/A
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.


    ### Add your other method definitions below. ###

        for i in digitstr:
            if i == digitstr[0]:
                self.tiles[0][0] = int(i)
            elif i == digitstr[1]:
                self.tiles[0][1] = int(i)
            elif i == digitstr[2]:
                self.tiles[0][2] = int(i)
            elif i == digitstr[3]:
                self.tiles[1][0] = int(i)
            elif i == digitstr[4]:
                self.tiles[1][1] = int(i)
            elif i == digitstr[5]:
                self.tiles[1][2] = int(i)
            elif i == digitstr[6]:
                self.tiles[2][0] = int(i)
            elif i == digitstr[7]:
                self.tiles[2][1] = int(i)
            else:
                self.tiles[2][2] = int(i)
           
        if 0 == self.tiles[0][0]:
            self.blank_r = 0
            self.blank_c = 0
        elif 0 == self.tiles[0][1]:
            self.blank_r = 0
            self.blank_c = 1
        elif 0 == self.tiles[0][2]:
            self.blank_r = 0
            self.blank_c = 2
        elif 0 == self.tiles[1][0]:
            self.blank_r = 1
            self.blank_c = 0
        elif 0 == self.tiles[1][1]:
            self.blank_r = 1
            self.blank_c = 1
        elif 0 == self.tiles[1][2]:
            self.blank_r = 1
            self.blank_c = 2
        elif 0 == self.tiles[2][0]:
            self.blank_r = 2
            self.blank_c = 0
        elif 0 == self.tiles[2][1]:
            self.blank_r = 2
            self.blank_c = 1
        else:
            self.blank_r = 2
            self.blank_c = 2


    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[i][j])+' '
            s += '\n'
        return s
        

    def move_blank(self, direction):
        """ Takes as input a string direction that specifies the direction
            in which the blank should move, and that attempts to modify the
            contents of the called Board object accordingly.
        """
        if direction not in 'up down left right':
            print ('unknown direction:', direction)
            return False

        up_coord = self.blank_r - 1
        down_coord = self.blank_r + 1
        left_coord = self.blank_c - 1
        right_coord = self.blank_c + 1
   
        if direction == 'up':
            if up_coord < 0 or up_coord > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[up_coord][self.blank_c]
                self.tiles[up_coord][self.blank_c] = 0
                self.blank_r = up_coord
                return True
        if direction == 'down':
            if down_coord < 0 or down_coord > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[down_coord][self.blank_c]
                self.tiles[down_coord][self.blank_c] = 0
                self.blank_r = down_coord
                return True
        if direction == 'left':
            if left_coord < 0 or left_coord > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][left_coord]
                self.tiles[self.blank_r][left_coord] = 0
                self.blank_c = left_coord
                return True
        if direction == 'right':
            if right_coord < 0 or right_coord > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][right_coord]
                self.tiles[self.blank_r][right_coord] = 0
                self.blank_c = right_coord
                return True
        

    def digit_string(self):
        """ Creates and returns a string of digits that corresponds to the
            current contents of the called Board object’s tiles attribute.
        """
        first = self.tiles[0][0]
        second = self.tiles[0][1]
        third = self.tiles[0][2]
        fourth = self.tiles[1][0]
        fifth = self.tiles[1][1]
        sixth = self.tiles[1][2]
        seventh = self.tiles[2][0]
        eighth = self.tiles[2][1]
        ninth = self.tiles[2][2]

        return str(first)+str(second)+str(third)+str(fourth)+str(fifth)\
               +str(sixth)+str(seventh)+str(eighth)+str(ninth)


    def copy(self):
        """ Returns a newly-constructed Board object that is a deep copy of
            the called object.
        """
        digits = self.digit_string()
        b = Board(digits)
        return b


    def num_misplaced(self):
        """ Counts and returns the number of tiles in the called Board
            object that are not where they should be in the goal state.
        """
        num_mis = 0

        if self.tiles[0][1] != 1:
            num_mis += 1
        if self.tiles[0][2] != 2:
            num_mis += 1
        if self.tiles[1][0] != 3:
            num_mis += 1
        if self.tiles[1][1] != 4:
            num_mis += 1
        if self.tiles[1][2] != 5:
            num_mis += 1
        if self.tiles[2][0] != 6:
            num_mis += 1
        if self.tiles[2][1] != 7:
            num_mis += 1
        if self.tiles[2][2] != 8:
            num_mis += 1

        return num_mis


    def __eq__(self, other):
        """ Overloads the == operator – creating a version of the operator
           that works for Board objects. The method should return True if
           the called object (self) and the argument (other) have the same
           values for the tiles attribute, and False otherwise.
        """
        if self.tiles == other.tiles:
            return True
        return False
        
    
    def how_misplaced(self):
        """ A new method for my own heuristic. It checks to see how many tiles
           are misplaced and if they are, check to see if they are at least
           in the correct row. If the tile is in the wrong spot, 1 gets added.
           If it is in at least the correct row, 1 gets subtracted.
       """
       
        updated_num_mis = 0

        if self.tiles[0][1] != 1:
            updated_num_mis += 1
        if self.tiles[0][2] == 1:
            updated_num_mis -= 1
        if self.tiles[0][2] != 2:
            updated_num_mis += 1
        if self.tiles[0][1] == 2:
            updated_num_mis -= 1
        if self.tiles[1][0] != 3:
            updated_num_mis += 1
        if self.tiles[1][1] == 3:
            updated_num_mis -= 1
        if self.tiles[1][2] == 3:
            updated_num_mis -= 1
        if self.tiles[1][1] != 4:
            updated_num_mis += 1
        if self.tiles[1][0] == 4:
            updated_num_mis -= 1
        if self.tiles[1][2] == 4:
            updated_num_mis -= 1
        if self.tiles[1][2] != 5:
            updated_num_mis += 1
        if self.tiles[1][0] == 5:
            updated_num_mis -= 1
        if self.tiles[1][1] == 5:
            updated_num_mis -= 1
        if self.tiles[2][0] != 6:
            updated_num_mis += 1
        if self.tiles[2][1] == 6:
            updated_num_mis -= 1
        if self.tiles[2][2] == 6:
            updated_num_mis -= 1
        if self.tiles[2][1] != 7:
            updated_num_mis += 1
        if self.tiles[2][0] == 7:
            updated_num_mis -= 1
        if self.tiles[2][2] == 7:
            updated_num_mis = -1
        if self.tiles[2][2] != 8:
            updated_num_mis += 1
        if self.tiles[2][0] == 8:
            updated_num_mis -= 1
        if self.tiles[2][1] == 8:
            updated_num_mis -= 1

        return updated_num_mis

        
           
    
            
        

        

