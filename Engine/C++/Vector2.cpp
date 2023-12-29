#include <cmath>

class Vector2 {
public:
	// static

	// static fields
	const static Vector2 zero;
	const static Vector2 one;

	const static Vector2 up;
	const static Vector2 down;
	const static Vector2 left;
	const static Vector2 right;

	// static methods

	static float Distance(Vector2 v1, Vector2 v2) {
		return static_cast<float>(sqrt(std::pow((v1.x - v2.x), 2) + std::pow((v1.y - v2.y), 2)));
	}

	// nonstatic

	// nonstatic fields

	float x = 0;
	float y = 0;

	// nonstatic methods

	// constructor
	Vector2(float x, float y) {
		this->x = x;
		this->y = y;
	}

	Vector2 Clone() const {
		return Vector2(this->x, this->y);
	}

	// operator overloads

	bool operator==(const Vector2& other) const {
		return this->x == other.x && this->y == other.y;
	}

	Vector2 operator*(const Vector2& other) const {
		return Vector2(this->x * other.x, this->y * other.y);
	}

	Vector2 operator*(const float& other) const {
		return Vector2(this->x * other, this->y * other);
	}

	Vector2 operator*(const int& other) const {
		this->operator*(static_cast<float>(other));
	}

	Vector2 operator/(const Vector2& other) const {
		return Vector2(this->x / other.x, this->y / other.y);
	}

	Vector2 operator/(const float& other) const {
		return Vector2(this->x / other, this->y / other);
	}

	Vector2 operator/(const int& other) const {
		this->operator/(static_cast<float>(other));
	}

	Vector2 operator+(const Vector2& other) const {
		return Vector2(this->x + other.x, this->y + other.y);
	}

	Vector2 operator+(const float& other) const {
		return Vector2(this->x + other, this->y + other);
	}

	Vector2 operator+(const int& other) const {
		this->operator+(static_cast<float>(other));
	}

	Vector2 operator-(const Vector2& other) const {
		return Vector2(this->x - other.x, this->y - other.y);
	}

	Vector2 operator-(const float& other) const {
		return Vector2(this->x - other, this->y - other);
	}

	Vector2 operator-(const int& other) const {
		this->operator-(static_cast<float>(other));
	}

	Vector2 pow(Vector2 other) const {
		return Vector2(std::pow(this->x, other.x), std::pow(this->y, other.y));
	}

	Vector2 pow(float other) const {
		return Vector2(std::pow(this->x, other), std::pow(this->y, other));
	}

	Vector2 pow(int other) const {
		return this->pow(static_cast<float>(other));
	}

	Vector2 abs() const {
		return Vector2(std::abs(this->x), std::abs(this->y));
	}

	Vector2 neg() const {
		return Vector2(-x, -y);
	}
};

// circular fields must be defined outside of class definition
const Vector2 Vector2::zero = Vector2(0, 0);
const Vector2 Vector2::one = Vector2(1, 1);

const Vector2 Vector2::up = Vector2(0, 1);
const Vector2 Vector2::down = Vector2(0, -1);
const Vector2 Vector2::left = Vector2(-1, 0);
const Vector2 Vector2::right = Vector2(1, 0);

// exports
extern "C" {
	// static

	// static fields

	__declspec(dllexport) const Vector2* Vector2_zero() {
		return &Vector2::zero;
	}

	__declspec(dllexport) const Vector2* Vector2_one() {
		return &Vector2::one;
	}

	__declspec(dllexport) const Vector2* Vector2_up() {
		return &Vector2::up;
	}

	__declspec(dllexport) const Vector2* Vector2_down() {
		return &Vector2::down;
	}

	__declspec(dllexport) const Vector2* Vector2_left() {
		return &Vector2::left;
	}

	__declspec(dllexport) const Vector2* Vector2_right() {
		return &Vector2::right;
	}

	// static methods

	__declspec(dllexport) float Vector2_distance(const Vector2* v1, const Vector2* v2) {
		return Vector2::Distance(*v1, *v2);
	}

	// nonstatic

	// nonstatic fields

	__declspec(dllexport) float Vector2_getX(const Vector2* self) {
		return self->x;
	}

	__declspec(dllexport) void Vector2_setX(Vector2* self, const float value) {
		self->x = value;
	}

	__declspec(dllexport) float Vector2_getY(const Vector2* self) {
		return self->y;
	}

	__declspec(dllexport) void Vector2_setY(Vector2* self, const float value) {
		self->y = value;
	}

	// nonstatic methods

	// constructor
	__declspec(dllexport) Vector2* Vector2_init(float x, float y) {
		return new Vector2(x, y);
	}

	__declspec(dllexport) Vector2* Vector2_clone(const Vector2* self) {
		return new Vector2(self->Clone());
	}

	// free memory for python garbage collector
	__declspec(dllexport) void Vector2_del(Vector2* self) {
		delete self;
	}

	// operator overloads

	__declspec(dllexport) Vector2* Vector2_mul_Vector2(const Vector2* self, const Vector2* other) {
		return new Vector2((*self) * (*other));
	}

	__declspec(dllexport) Vector2* Vector2_mul_float(const Vector2* self, const float other) {
		return new Vector2((*self) * other);
	}

	__declspec(dllexport) Vector2* Vector2_mul_int(const Vector2* self, const int other) {
		return Vector2_mul_float(self, static_cast<float>(other));
	}

	__declspec(dllexport) Vector2* Vector2_truediv_Vector2(const Vector2* self, const Vector2* other) {
		return new Vector2((*self) / (*other));
	}

	__declspec(dllexport) Vector2* Vector2_truediv_float(const Vector2* self, const float other) {
		return new Vector2((*self) / other);
	}

	__declspec(dllexport) Vector2* Vector2_truediv_int(const Vector2* self, const int other) {
		return Vector2_truediv_float(self, static_cast<float>(other));
	}

	__declspec(dllexport) Vector2* Vector2_add_Vector2(const Vector2* self, const Vector2* other) {
		return new Vector2((*self) + (*other));
	}

	__declspec(dllexport) Vector2* Vector2_add_float(const Vector2* self, const float other) {
		return new Vector2((*self) + other);
	}

	__declspec(dllexport) Vector2* Vector2_add_int(const Vector2* self, const int other) {
		return Vector2_add_float(self, static_cast<float>(other));
	}

	__declspec(dllexport) Vector2* Vector2_sub_Vector2(const Vector2* self, const Vector2* other) {
		return new Vector2((*self) - (*other));
	}

	__declspec(dllexport) Vector2* Vector2_sub_float(const Vector2* self, const float other) {
		return new Vector2((*self) - other);
	}

	__declspec(dllexport) Vector2* Vector2_sub_int(const Vector2* self, const int other) {
		return Vector2_sub_float(self, static_cast<float>(other));
	}

	__declspec(dllexport) Vector2* Vector2_pow_Vector2(const Vector2* self, const Vector2* other) {
		return new Vector2(self->pow(*other));
	}

	__declspec(dllexport) Vector2* Vector2_pow_float(const Vector2* self, const float other) {
		return new Vector2(self->pow(other));
	}

	__declspec(dllexport) Vector2* Vector2_pow_int(const Vector2* self, const int other) {
		return Vector2_pow_float(self, static_cast<float>(other));
	}

	__declspec(dllexport) Vector2* Vector2_abs(const Vector2* self) {
		return new Vector2(self->abs());
	}

	__declspec(dllexport) Vector2* Vector2_neg(const Vector2* self) {
		return new Vector2(self->neg());
	}
}