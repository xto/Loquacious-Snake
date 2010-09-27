from loquacious_snake.expectations.SharedSeleniumExecutionContextExpectations import SharedSeleniumExecutionContextExpectations

from loquacious_snake.expectations.SeleniumDrivenUserActionsExpectations import \
    SeleniumDrivenUserActionsExpectations
from loquacious_snake.expectations.SeleniumDrivenUserExpectations import \
    SeleniumDriverUserExpectations
from loquacious_snake.expectations.SeleniumDrivenUserExpectationsExpectations import \
    SeleniumDrivenUserExpectationsExpectations
import unittest


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(SeleniumDrivenUserExpectationsExpectations,prefix="SeleniumDrivenUserExpectationsShould"))
    suite.addTests(unittest.makeSuite(SeleniumDrivenUserActionsExpectations,prefix="SeleniumDrivenUser"))
    suite.addTests(unittest.makeSuite(SeleniumDriverUserExpectations,prefix="SeleniumDrivenUser"))
    suite.addTests(unittest.makeSuite(SharedSeleniumExecutionContextExpectations,prefix="SharedSeleniumExecutionContext"))
    unittest.TextTestRunner(verbosity=2).run(suite)