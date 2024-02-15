#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <iostream>

// 2D Vector class
class Vector2 {
private:
    double x = 0;
    double y = 0;
public:
    // constructor
    Vector2(double newX, double newY) {
        x = newX;
        y = newY;
    }

    // getters
    double getX() const {
        return x;
    }

    double getY() const {
        return y;
    }

    // setters

    void setX(double newX) {
        x = newX;
    }

    void setY(double newY) {
        y = newY;
    }
};

// python method wrappers

// constructor

void Vector2_delete(PyObject* capsule) {
    Vector2* vector = static_cast<Vector2*>(PyCapsule_GetPointer(capsule, "Vector2"));
    delete vector;
}

static PyObject* Vector2_new(PyObject* self, PyObject* args) {
    // default x and y
    double x = 0;
    double y = 0;

    // get x and y parameters from args
    PyArg_ParseTuple(args, "dd", &x, &y);

    // create Vector2
    Vector2* vector = new Vector2(x, y);

    // make sure it was properly constructed
    if (!vector) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to create a new Vector2 object.");
        return NULL;
    }

    // return as pycapsule
    return PyCapsule_New(vector, "Vector2", Vector2_delete);
}

// getters

static PyObject* Vector2_getX(PyObject* self, PyObject* args) {
    // get capsule parameter
    PyObject* capsule;

    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        PyErr_SetString(PyExc_TypeError, "Invalid capsule object passed.");
        return NULL;
    }

    // convert capsule to Vector2
    Vector2* vector = static_cast<Vector2*>(PyCapsule_GetPointer(capsule, "Vector2"));

    if (!vector) {
        PyErr_SetString(PyExc_TypeError, "The passed capsule object is not a Vector2.");
        return NULL;
    }

    // return x value as python float
    return PyFloat_FromDouble(vector->getX());
}


static PyObject* Vector2_getY(PyObject* self, PyObject* args) {
    // get capsule parameter
    PyObject* capsule;

    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        PyErr_SetString(PyExc_TypeError, "Invalid capsule object passed.");
        return NULL;
    }

    // convert capsule to Vector2
    Vector2* vector = static_cast<Vector2*>(PyCapsule_GetPointer(capsule, "Vector2"));

    if (!vector) {
        PyErr_SetString(PyExc_TypeError, "The passed capsule object is not a Vector2.");
        return NULL;
    }

    // return y value as python float
    return PyFloat_FromDouble(vector->getY());
}

// setters

static PyObject* Vector2_setX(Vector2* self, PyObject* args) {
    // get parameters
    PyObject* capsule;
    double newX;

    if (!PyArg_ParseTuple(args, "Od", &capsule, &newX)) {
        PyErr_SetString(PyExc_TypeError, "Invalid parameters passed.");
        return NULL;
    }

    // convert capsule from parameter to Vector2
    Vector2* vector = static_cast<Vector2*>(PyCapsule_GetPointer(capsule, "Vector2"));

    if (!vector) {
        PyErr_SetString(PyExc_TypeError, "The passed capsule object is not a Vector2.");
        return NULL;
    }

    vector->setX(newX);
    Py_RETURN_NONE;
}


static PyObject* Vector2_setY(Vector2* self, PyObject* args) {
    // get parameters
    PyObject* capsule;
    double newY;

    if (!PyArg_ParseTuple(args, "Od", &capsule, &newY)) {
        PyErr_SetString(PyExc_TypeError, "Invalid parameters passed.");
        return NULL;
    }

    // convert capsule from parameter to Vector2
    Vector2* vector = static_cast<Vector2*>(PyCapsule_GetPointer(capsule, "Vector2"));

    if (!vector) {
        PyErr_SetString(PyExc_TypeError, "The passed capsule object is not a Vector2.");
        return NULL;
    }

    // set new y
    vector->setY(newY);

    Py_RETURN_NONE;
}

// set python methods
static PyMethodDef pythonMethods[] = {
    {"Vector2_new", (PyCFunction)Vector2_new, METH_VARARGS, "Create new Vector2"},
    {"Vector2_delete", (PyCFunction)Vector2_getX, METH_VARARGS, "Delete a Vector2"},
    {"Vector2_getX", (PyCFunction)Vector2_getX, METH_VARARGS, "Get X of Vector2 class"},
    {"Vector2_getY", (PyCFunction)Vector2_getY, METH_VARARGS, "Get Y of Vector2 class"},
    {"Vector2_setX", (PyCFunction)Vector2_setX, METH_VARARGS, "Set X of Vector2 class"},
    {"Vector2_setY", (PyCFunction)Vector2_setY, METH_VARARGS, "Set Y of Vector2 class"},
    {NULL, NULL, 0, NULL}
};

// define module initialization
static struct PyModuleDef pythonModule = {
    PyModuleDef_HEAD_INIT,
    "Vector2",
    NULL,
    -1,
    pythonMethods
};

// create module
PyMODINIT_FUNC PyInit_Vector2(void) {
    return PyModule_Create(&pythonModule);
}