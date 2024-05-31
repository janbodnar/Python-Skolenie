# Money

`pip install py-moneyed`

The `py-moneyed` package in Python offers several advantages over using the `Decimal` class  
for representing monetary values:

1. **Currency and Money Classes**: `py-moneyed` provides `Money` and `Currency` classes, which are more useful for  
   representing instances of money. These classes offer a higher level of abstraction than the `Decimal` class,  
   making it easier to handle money-related operations.  
3. **Avoids Floating Point Issues**: The `Decimal` class is a better choice than floating point numbers for monetary  
   calculations due to precision issues with floats⁴. However, `py-moneyed` takes this a step further by providing  
   dedicated classes for money and currency¹.
5. **Supports Exact Calculations**: `py-moneyed` allows for exact calculations with monetary values, avoiding rounding  
   errors that can occur with chained calculations.  
7. **Ease of Use**: `Money` objects in `py-moneyed` can be used as if they were numbers, providing a  
   straightforward and intuitive interface.
   
In summary, `py-moneyed` offers a more robust and user-friendly way to handle monetary values in Python   
compared to the `Decimal` class.

