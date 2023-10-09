#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Function that prints some basic info about python list
 * @p: the python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int a = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	while (a < size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		a++;
	}
}
