# Essential Python Packages

## Pandas
- Pandas DataFrame returns a view by default when selecting a subset, meaning changes to the view will change the original.
- Pandas 2.0 offers the option to return a copy instead of a view by default, preventing changes to the copy from affecting the original.


## MLEM
The metadata of a machine learning model provides important information about the model such as:

✅ Hash value
✅ Model methods
✅ Input data schema
✅ Python requirements used to train the model.

This information enables others to reproduce the model and its results.

With MLEM, you can save both the model and its metadata in a single line of code.

![image](https://user-images.githubusercontent.com/50066797/234052663-49fac8d9-52d8-4c51-b6a0-7fd5cefe37ae.png)

## Numpy - Unyt
Working with NumPy arrays that have units can be difficult, as it is not immediately clear what the units are, which can lead to errors. 

The unyt package solves this by providing a subclass of NumPy's ndarray class that knows units.

unyt arrays support standard NumPy array operations and functions while preserving the units associated with the data.
