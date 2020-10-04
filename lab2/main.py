from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow


def main():
    print("Торжков Максим ИУ5-51Б")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))
    r = Rectangle("синего", 19, 19)
    c = Circle("зеленого", 19)
    s = Square("красного", 19)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()