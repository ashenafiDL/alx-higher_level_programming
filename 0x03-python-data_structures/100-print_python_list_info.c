#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list object
 */
void print_python_list_info(PyObject *p)
{
	int s;
	int alloc;
	int i;
	PyObject *obj;

	s = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < s; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Elemen %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
