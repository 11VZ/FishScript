# FishScript Language Documentation

FishScript is a custom programming language inspired by Java and python.
---

## Table of Contents
- [1. Getting Started](#getting-started)
- [2. Syntax Overview](#syntax-overview)
- [3. Data Types](#data-types)
- [4. Variables](#variables)
- [5. Functions](#functions)
- [6. Control Flow](#control-flow)
- [7. Classes & Objects](#classes--objects)
- [8. Modules & Imports](#modules--imports)
- [9. Comments](#comments)
- [10. Built-in Functions](#built-in-functions)
- [11. Error Handling](#error-handling)
- [12. Standard Library](#standard-library)
- [13. Examples](#examples)

---

## 1. Getting Started
Write your code in `.fish` files. To run, use:
```
fish yourfile.fish
```

---

## 2. Syntax Overview
- Java-like.
- Semicolon end statements.
- Blocks use `{ ... }`.

---

## 3. Data Types
- `int`, `float`, `string`, `boolean`, `array`, `list`

---

## 4. Variables
```fishscript
private int x = 10;
public float y = 3.14;
string name = "Fish";
```

---

## 5. Functions
```fishscript
public add(int a, int b) {
    return a + b;
}

private string greet(string name) {
    return "Hello, " + name;
}
```

---

## 6. Control Flow
### If/Else
```fishscript
if x > 0 {
    print("Positive");
} else {
    print("Non-positive");
}
```

### While
```fishscript
int i = 0;
while i < 5 {
    print(i);
    i = i + 1;
}
```

### For
```fishscript
for int i = 0; i < 5; i = i + 1 {
    print(i);
}
```

### Switch
```fishscript
switch x {
    case 1: print("One"); break;
    case 2: print("Two"); break;
    default: print("Other");
}
```

---

## 7. Classes & Objects
```fishscript
public class Counter {
    private int count = 0;
    
    public inc() {
        count = count + 1;
    }
    
    public int get() {
        return count;
    }
}

Counter c = new Counter();
c.inc();
print(c.get());
```

---

## 8. Modules & Imports
```fishscript
import math;
import mymodule;

x = math.sqrt(16);
```

---

## 9. Comments
- Single-line: `// comment` or `# comment`
- Multi-line: `# ... #`

---

## 10. Built-in Functions
- `print(value)` — Output to console
- `input(prompt)` — Read from user

---

## 11. Error Handling
```fishscript
try {
    risky();
} catch (e) {
    print("Error: " + e);
}
```

---

## 12. Standard Library
- `math` (sqrt, pow, sin, ...)
- `string` (length, toUpper, ...)

---

## 13. Examples

### Example 1: Simple Loop
```fishscript
private int x = 1;
while x <= 10 {
    print(x);
    x = x + 1;
}
```

### Example 2: Function in Another File
**function.fish**
```fishscript
public add(int a, int b) {
    return a + b;
}
```
**main.fish**
```fishscript
import function;
private int x = 1;
while x <= 10 {
    print(x);
    x = function.add(x, 1);
}
```

### Example 3: Class
```fishscript
public class Greeter {
    public string greet(string name) {
        return "Hello, " + name;
    }
}
Greeter g = new Greeter();
print(g.greet("FishScript"));
```

### Example 4: Error Handling
```fishscript
try {
    int x = 1 / 0;
} catch (e) {
    print("Caught error: " + e);
}
```

### Example 5: Arrays/Lists
```fishscript
int[] nums = [1, 2, 3, 4];
for int i = 0; i < 4; i = i + 1 {
    print(nums[i]);
}
```

---