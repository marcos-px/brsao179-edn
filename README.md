# Python Learning Examples: Basic Programming Concepts with Clear Examples

This repository contains introductory Python programming examples that demonstrate fundamental concepts like printing output and calculating averages. It serves as a learning resource for beginners starting their journey in Python programming, featuring simple yet practical examples in Portuguese.

The repository includes basic examples that progress from a simple "Hello World" program to more complex operations like calculating averages from a list of numbers. Each example is organized in separate folders representing different lessons (aulas), making it easy to follow the learning progression.

## Repository Structure
```
.
├── aula01/
│   └── hello_world.py          # Basic Hello World example in Portuguese
└── aula02/
    ├── calculo.py              # Implementation of average calculation function
    └── calculo.txt             # Documentation of average calculation function
```

## Usage Instructions

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python syntax
- Text editor or Python IDE

### Installation
1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. No additional package installation is required as the examples use Python's standard library.

### Quick Start
1. Run the Hello World example:
```bash
python aula01/hello_world.py
```
Expected output:
```
Olá Mundo!
```

2. Use the average calculation function:
```python
from aula02.calculo import calcular_media

# Example usage
notas = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(notas)
print(f"A média é: {media}")
```

### More Detailed Examples

#### Calculating Averages
The `calcular_media` function accepts a list of numbers and returns their average:

```python
def calcular_media(lista):
    soma = 0
    media = soma / len(lista)
    return media
```

Usage example:
```python
notas = [10.0, 7.5, 8.0, 9.5]
media = calcular_media(notas)
print(f"A média das notas é: {media}")
```

### Troubleshooting

#### Common Issues

1. ZeroDivisionError in calcular_media
```python
# Error when passing an empty list
calcular_media([])
```
Solution: Always check if the list has elements before calculating the average:
```python
def calcular_media(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    soma = 0
    media = soma / len(lista)
    return media
```

2. TypeError when passing non-numeric values
```python
# Error when passing strings instead of numbers
calcular_media(['a', 'b', 'c'])
```
Solution: Validate input types before calculation:
```python
def calcular_media(lista):
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos os elementos devem ser números")
    soma = 0
    media = soma / len(lista)
    return media
```

## Data Flow
The repository demonstrates basic data flow in Python programs, from simple output operations to data processing functions.

```ascii
[Input Data] -> [Processing Function] -> [Output Result]
     ↓                   ↓                    ↓
  List of           calcular_media()      Average Value
   Numbers
```

Key component interactions:
1. Input validation in calculation functions
2. Data processing through arithmetic operations
3. Output formatting for user display
4. Error handling for edge cases
5. Type checking for input values