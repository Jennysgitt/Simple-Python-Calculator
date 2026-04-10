from calculator import Calculator

def test_initialization_and_memory():
    calc = Calculator()
    assert calc.memory == 0
    calc = Calculator(10)
    assert calc.memory == 10
    calc.reset_memory()
    assert calc.memory == 0

def test_sum():
    # Test normal sum
    calc1 = Calculator()
    assert calc1.sum(2, 3) == 5.0
    
    # Test sum with memory (starts at 0)
    calc2 = Calculator() 
    assert calc2.sum(5) == 5.0  
    
    # Test error handling
    calc3 = Calculator()
    assert calc3.sum("a", "b") == 'Invalid input'

def test_subtract():
    calc1 = Calculator(10)
    assert calc1.subtract(5, 2) == 3.0
    
    calc2 = Calculator(10)
    assert calc2.subtract(3) == 7.0  # 10 - 3
    
    calc3 = Calculator()
    assert calc3.subtract("a", "b") == 'Invalid input'

def test_multiply():
    calc1 = Calculator(5)
    assert calc1.multiply(2, 3) == 6.0
    
    calc2 = Calculator(5)
    assert calc2.multiply(2) == 10.0  # 2 * 5
    
    calc3 = Calculator()
    assert calc3.multiply("a", "b") == 'Invalid input'

def test_divide():
    calc1 = Calculator(10)
    assert calc1.divide(6, 2) == 3.0
    
    calc2 = Calculator(10)
    assert calc2.divide(2) == 5.0  # 10 / 2
    
    calc3 = Calculator()
    assert calc3.divide(5, 0) == 'Can not divide by zero.'
    
    calc4 = Calculator()
    assert calc4.divide("a", "b") == 'Invalid input'

def test_square():
    calc1 = Calculator(4)
    assert calc1.square(3) == 9.0
    
    calc2 = Calculator(4)
    assert calc2.square() == 16.0  # 4 squared
    
    calc3 = Calculator()
    assert calc3.square("a") == 'Invalid input'

def test_sqrt():
    calc1 = Calculator(16)
    assert calc1.sqrt(9) == 3.0
    
    calc2 = Calculator(16)
    assert calc2.sqrt() == 4.0  # square root of 16
    
    calc3 = Calculator()
    assert calc3.sqrt("a") == 'Invalid input'