#
# searcher.py (Final Project)
#
# classes for objects that perform state-space search on Eight Puzzles
#
# name: Jake Bloomfeld      
# email: jtbloom@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: N/A
# partner's email: N/A
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, init_state, depth_limit):
        """ Constructs a new Searcher object by initializing the
            following attributes:
            - an attribute states for the Searcher‘s list of untested
              states; it should be initialized to a list containing the
              state specified by the parameter init_state
            - an attribute num_tested that will keep track of how many
              states the Searcher tests; it should be initialized to 0
            - an attribute depth_limit that specifies how deep in the
              state-space search tree the Searcher will go; it should be
              initialized to the value specified by the parameter depth_limit.
             (A depth_limit of -1 indicates that the Searcher does not use a
              depth limit.)
        """
        self.states = [init_state]
        self.num_tested = 0
        self.depth_limit = depth_limit


    def should_add(self, state):
        """ Takes a State object called state and returns True if the called
            Searcher should add state to its list of untested states, and
            False otherwise.
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        if state.creates_cycle() == True:
            return False
        return True


    def add_state(self, new_state):
        """ Adds takes a single State object called new_state and adds it to
            the Searcher‘s list of untested states.
        """
        self.states += [new_state]


    def add_states(self, new_states):
        """ Takes a list State objects called new_states, and that
            processes the elements of new_states one at a time as follows:
            - if a given state s should be added to the Searcher‘s list of
            untested states (because s would not cause a cycle and is not
            beyond the Searcher‘s depth limit), the method should use the
            Searcher‘s add_state() method to add s to the list of states.
            - if a given state s should not be added to the Searcher
            object’s list of states, the method should ignore the state.
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)


    def next_state(self):
        """ Chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it.
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s


    def find_solution(self):
        """ Performs a full random state-space search, stopping when
            the goal state is found or when the Searcher runs out of
            untested states.
        """
        while self.states != 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your other class definitions below. ###

class BFSearcher(Searcher):
    """ A class for objects that perform breadth-first search on an Eight
        Puzzle.
    """

    def next_state(self):
        """ This method follows FIFO (first-in first-out) ordering –
            choosing the state that has been in the list the longest.
        """
        s = self.states[0] 
        self.states.remove(s)
        return s


class DFSearcher(Searcher):
    """ A class for objects that perform depth-first search on an Eight
        Puzzle.
    """

    def next_state(self):
        """ This method follows LIFO (last-in first-out) ordering – choosing
            the state that was most recently added to the list.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s


class GreedySearcher(Searcher):
    """ A class for objects that perform greedy search on an Eight
        Puzzle.
    """

    def priority(self, state):
        """ Takes a State object called state, and that computes
            and returns the priority of that state.
        """
        if self.heuristic == 1:
            updated_num_mis = state.board.how_misplaced()
            priority = -1 * updated_num_mis
        else:
            num_misplaced_tiles = state.board.num_misplaced()
            priority = -1 * num_misplaced_tiles
        return priority


    def __init__(self, init_state, heuristic, depth_limit):
        """ Constructor for a GreedySearcher object
            inputs:
            * init_state - a State object for the initial state
            * heuristic - an integer specifying which heuristic
              function should be used when computing the priority of a state
            * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit


    def add_state(self, state):
        """ The method adds a sublist that is a [priority, state] pair,
            where priority is the priority of state, as determined by
            calling the priority method.
        """
        self.states += [[self.priority(state), state]]


    def next_state(self):
        """ This version of next_state chooses one of the states with the
            highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]


class AStarSearcher(Searcher):
    """ A class for objects that perform A* search on an Eight Puzzle.
    """

    def priority(self, state):
        """ Takes a State object called state, and that computes
            and returns the priority of that state.
        """
        if self.heuristic == 1:
            updated_num_mis = state.board.how_misplaced()
            priority = -1 * (updated_num_mis + state.num_moves)
        else:
            num_misplaced_tiles = state.board.num_misplaced()
            priority = -1 * (num_misplaced_tiles + state.num_moves)
        return priority


    def __init__(self, init_state, heuristic, depth_limit):
        """ Constructor for a AStarSearcher object
            inputs:
            * init_state - a State object for the initial state
            * heuristic - an integer specifying which heuristic
              function should be used when computing the priority of a state
            * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit


    def add_state(self, state):
        """ The method adds a sublist that is a [priority, state] pair,
            where priority is the priority of state, as determined by
            calling the priority method.
        """
        self.states += [[self.priority(state), state]]


    def next_state(self):
        """ This version of next_state chooses one of the states with the
            highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]

    
        


        


