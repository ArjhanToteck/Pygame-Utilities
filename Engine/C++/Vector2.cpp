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
    double x = 0, y = 0;

    if (!PyArg_ParseTuple(args, "|dd", &x, &y)) {
        return NULL; // Error parsing arguments
    }

    Vector2* vector = new Vector2(x, y);
    if (!vector) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to create Vector2 object");
        return NULL;
    }

    return PyCapsule_New(vector, "Vector2", Vector2_delete);
}

// getters

static PyObject* Vector2_getX(PyObject* self) {
    Vector2* vector = (Vector2*)PyCapsule_GetPointer(self, "Vector2");

    return Py_BuildValue("d", vector->getX());
}


static PyObject* Vector2_getY(PyObject* self) {
    Vector2* vector = (Vector2*)PyCapsule_GetPointer(self, "Vector2");

    return Py_BuildValue("d", vector->getY());
}

// setters

static PyObject* Vector2_setX(PyObject* self, PyObject* args) {
    Vector2* vector = (Vector2*)PyCapsule_GetPointer(self, "Vector2");
    double newX;

    if (!PyArg_ParseTuple(args, "d", &newX)) {
        return NULL;
    }

    vector->setX(newX);
    Py_RETURN_NONE;
}


static PyObject* Vector2_setY(PyObject* self, PyObject* args) {
    Vector2* vector = (Vector2*)PyCapsule_GetPointer(self, "Vector2");
    double newY;

    if (!PyArg_ParseTuple(args, "d", &newY)) {
        return NULL;
    }

    vector->setY(newY);
    Py_RETURN_NONE;
}

// set python methods
static PyMethodDef pythonMethods[] = {
    {"Vector2_new", (PyCFunction)Vector2_getX, METH_VARARGS, "Create new Vector2"},
    {"Vector2_delete", (PyCFunction)Vector2_getX, METH_NOARGS, "Delete a Vector2"},
    {"Vector2_getX", (PyCFunction)Vector2_getX, METH_NOARGS, "Get X of Vector2 class"},
    {"Vector2_getY", (PyCFunction)Vector2_getY, METH_NOARGS, "Get Y of Vector2 class"},
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