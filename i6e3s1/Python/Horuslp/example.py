from horuslp.core.Variables import BinaryVariable # we will be using binary variables, so we will import the BinaryVariable class, which is a variant of the Variable class
from horuslp.core import Constraint, VariableManager, Problem, ObjectiveComponent # We will also need to import the constraint class, variable manager class, the main problem class, and the objective class to define the objective.
from horuslp.core.constants import MAXIMIZE  # since we're maximizing the resulting value, we want to import this constant

class KnapsackVariables(VariableManager): # define the variables
    vars = [
        BinaryVariable('camera'), # the first argument is the name of the variable
        BinaryVariable('figurine'),
        BinaryVariable('cider'),
        BinaryVariable('horn')
    ]

class SizeConstraint(Constraint): # define the size constraint
    def define(self, camera, figurine, cider, horn):
        return 2 * camera + 4 * figurine + 7 * cider + 10 * horn <= 15

class ValueObjective(ObjectiveComponent): # define the objective
    def define(self, camera, figurine, cider, horn):
        return 5 * camera + 7 * figurine + 2 * cider + 10 * horn

class KnapsackProblem(Problem): # now define the problem
    variables = KnapsackVariables
    objective = ValueObjective
    constraints = [SizeConstraint]
    sense = MAXIMIZE

# instantiate and solve!
prob = KnapsackProblem()
prob.solve()
prob.print_results()