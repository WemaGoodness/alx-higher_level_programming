#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes;
	char *str;

	printf("[*] Python bytes\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	size = Py_SIZE(p);
	printf("  Size of the Python Bytes = %ld\n", size);
	printf("  Trying string: %s\n", str);
	size = size > 9 ? 10 : size + 1;
	printf("  First %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", str[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[*] Python float\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  Value: %0.15g\n", value);
}
