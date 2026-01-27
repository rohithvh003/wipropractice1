# Test Runner
# Test runner is responsible for executing and managing test cases in an automation framework
# Example is Pytest

# Test Reports
# provides a detailed summary of test execution results and help analyze failures



# 5. Sample Test Case to Validate a Simple Function
def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5