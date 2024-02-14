#include <Python.h>
#include <iostream>

// Define a simple class in C++
class Adder {
public:
    int add(int a, int b) {
        return a + b;
    }
};

// Define a function to create an instance of the Adder class
static PyObject* create_adder(PyObject* self, PyObject* args) {
    Adder* adder = new Adder();
    return PyCapsule_New(adder, "Adder", NULL);
}

// Define a function to add two numbers using the Adder class
static PyObject* add_numbers(PyObject* self, PyObject* args) {
    PyObject* capsule;
    int a, b;

    if (!PyArg_ParseTuple(args, "Oii", &capsule, &a, &b)) {
        return NULL;
    }

    Adder* adder = (Adder*)PyCapsule_GetPointer(capsule, "Adder");
    if (!adder) {
        return NULL;
    }

    int result = adder->add(a, b);
    return Py_BuildValue("i", result);
}

// Define the module methods
static PyMethodDef pythonMethods[] = {
    {"create_adder", create_adder, METH_NOARGS, "Create an instance of the Adder class"},
    {"add_numbers", add_numbers, METH_VARARGS, "Add two numbers using the Adder class"},
    {NULL, NULL, 0, NULL}
};

// Define the module initialization function
static struct PyModuleDef pythonModule = {
    PyModuleDef_HEAD_INIT,
    "example",
    NULL,
    -1,
    pythonMethods
};

// Create the module
PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&pythonModule);
}