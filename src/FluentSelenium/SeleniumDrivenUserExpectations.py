from FluentSelenium.helpers.Decorators import chainable,\
    requiresPresenceOfLocator, requiresAPreviouslyVisitedLocator

class SeleniumDrivenUserExpectationsException(Exception):
    pass

class SeleniumDrivenUserExpectations:
      
    def __init__(self, seleniumExecutionContext):
        self.seleniumExecutionContext = seleniumExecutionContext
        self.seleniumExecutionContext.initialize()
        self.chainingElement = self
        
    def getSeleniumInstance(self):        
        return self.seleniumExecutionContext.seleniumInstance
    
    @chainable
    def shouldBeOnPage(self, page):
        currentLocation = self.getSeleniumInstance().get_location()
        if currentLocation != page:
            raise SeleniumDrivenUserExpectationsException("Expected page " + page + "did not match current location " + currentLocation)
    
    @chainable
    @requiresPresenceOfLocator
    def shouldSee(self, locator):        
        self.seleniumExecutionContext.setLastVisitedLocation(locator)
    
    @chainable
    def shouldNotSee(self, locator):
        if self.getSeleniumInstance().is_element_present(locator):
            raise SeleniumDrivenUserExpectationsException(locator + " was found on the current page.")
        self.seleniumExecutionContext.setLastVisitedLocation(None)
    
    @chainable
    @requiresAPreviouslyVisitedLocator
    def withValue(self, expectedValue): 
        currentValue = self.getSeleniumInstance().get_value(self.seleniumExecutionContext.lastVisitedLocation)
        if expectedValue != currentValue:
            raise SeleniumDrivenUserExpectationsException("Expected value " + expectedValue + "did not match current value " + currentValue)