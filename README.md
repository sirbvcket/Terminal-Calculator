# Simple Calculator

A basic command-line calculator written in Python that performs fundamental arithmetic operations.

## Features

- ✅ Addition (+)
- ✅ Subtraction (-)
- ✅ Multiplication (*)
- ✅ Division (/)
- ✅ Input validation
- ✅ Error handling for division by zero
- ✅ User-friendly menu interface

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional dependencies required

## Usage

Run the calculator using Python:

```bash
python main.py
```

### How to Use

1. The program will display a menu with operation options
2. Enter a number (1-5) to select an operation:
   - `1` - Addition
   - `2` - Subtraction
   - `3` - Multiplication
   - `4` - Division
   - `5` - Exit
3. Enter two numbers when prompted
4. The result will be displayed
5. The program will return to the main menu for additional calculations
6. Select `5` to exit the program

### Example

```
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice: 1
Enter first number: 15
Enter second number: 25
15.0 + 25.0 = 40.0
```

## Error Handling

The calculator includes robust error handling for:

- **Invalid menu choices**: Shows "INVALID: CHOOSE 1-4" message
- **Non-numeric input**: Shows "ERROR: VALID NUM ONLY" message
- **Division by zero**: Shows "ERROR: DIV BY 0" message

## File Structure

```
program/
├── main.py          # Main calculator program
└── README.md        # This file
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Author

Created as a simple Python learning project.