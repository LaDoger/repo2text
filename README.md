# repo2text
Converts an entire repository into a single text file.

Read the descriptions in the repo2text.py file!

This repo itself is converted as such:
```


-------- START OF FILE: README.md --------

# repo2text
Converts an entire repository into a single text file.

Read the descriptions in the repo2text.py file!

This repo itself is converted as such:
```


/* ====== START OF FILE: README.md ====== */

# repo2text
Converts an entire repository into a single text file.

Read the descriptions in the repo2text.py file!

/* ====== END OF FILE: README.md ====== */



/* ====== START OF FILE: demo/contracts/demo.sol ====== */

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Demo {
    string public greeting;

    constructor(string memory _greeting) {
        greeting = _greeting;
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function getGreeting() public view returns(string memory) {
        return greeting;
    }
}


/* ====== END OF FILE: demo/contracts/demo.sol ====== */



/* ====== START OF FILE: demo/contracts/demo.vy ====== */

greeting: public(string)

@public
def __init__(_greeting: string):
    self.greeting = _greeting

@public
def setGreeting(_greeting: string):
    self.greeting = _greeting

@public
@view
def getGreeting() -> string:
    return self.greeting


/* ====== END OF FILE: demo/contracts/demo.vy ====== */



/* ====== START OF FILE: demo/data/demo.csv ====== */

Company Name,Street,City,Country,First Name,Last Name,Email,Age,Department,Skills
Tech Corp,123 Tech Road,Techville,USA,John,Doe,john@example.com,30,HR,"communication,organization"
Tech Corp,123 Tech Road,Techville,USA,Anna,Smith,anna@example.com,31,Sales,"sales,marketing"
Tech Corp,123 Tech Road,Techville,USA,Peter,Jones,peter@example.com,24,Development,"programming,testing"

/* ====== END OF FILE: demo/data/demo.csv ====== */



/* ====== START OF FILE: demo/data/demo.json ====== */

{
    "company": {
        "name": "Tech Corp",
        "address": {
            "street": "123 Tech Road",
            "city": "Techville",
            "country": "USA"
        },
        "employees": [
            {
                "firstName": "John",
                "lastName": "Doe",
                "email": "john@example.com",
                "age": 30,
                "department": "HR",
                "skills": ["communication", "organization"]
            },
            {
                "firstName": "Anna",
                "lastName": "Smith",
                "email": "anna@example.com",
                "age": 31,
                "department": "Sales",
                "skills": ["sales", "marketing"]
            },
            {
                "firstName": "Peter",
                "lastName": "Jones",
                "email": "peter@example.com",
                "age": 24,
                "department": "Development",
                "skills": ["programming", "testing"]
            }
        ]
    }
}

/* ====== END OF FILE: demo/data/demo.json ====== */



/* ====== START OF FILE: demo/data/demo.yaml ====== */

company:
  name: Tech Corp
  address:
    street: 123 Tech Road
    city: Techville
    country: USA
  employees:
    - firstName: John
      lastName: Doe
      email: john@example.com
      age: 30
      department: HR
      skills:
        - communication
        - organization
    - firstName: Anna
      lastName: Smith
      email: anna@example.com
      age: 31
      department: Sales
      skills:
        - sales
        - marketing
    - firstName: Peter
      lastName: Jones
      email: peter@example.com
      age: 24
      department: Development
      skills:
        - programming
        - testing

/* ====== END OF FILE: demo/data/demo.yaml ====== */



/* ====== START OF FILE: demo/demo.c ====== */

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

/* ====== END OF FILE: demo/demo.c ====== */



/* ====== START OF FILE: demo/demo.cpp ====== */

#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

/* ====== END OF FILE: demo/demo.cpp ====== */



/* ====== START OF FILE: demo/demo.cs ====== */

using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}

/* ====== END OF FILE: demo/demo.cs ====== */



/* ====== START OF FILE: demo/demo.py ====== */

print("Hello, World!")

/* ====== END OF FILE: demo/demo.py ====== */



/* ====== START OF FILE: demo/demo.rb ====== */

puts "Hello, World!"

/* ====== END OF FILE: demo/demo.rb ====== */



/* ====== START OF FILE: demo/main.go ====== */

package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

/* ====== END OF FILE: demo/main.go ====== */



/* ====== START OF FILE: demo/Main.java ====== */

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

/* ====== END OF FILE: demo/Main.java ====== */



/* ====== START OF FILE: demo/main.rs ====== */

fn main() {
    println!("Hello, World!");
}

/* ====== END OF FILE: demo/main.rs ====== */



/* ====== START OF FILE: demo/main.swift ====== */

import Swift
print("Hello, World!")

/* ====== END OF FILE: demo/main.swift ====== */



/* ====== START OF FILE: demo/website/index.html ====== */

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Website</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <header>
        <h1>Welcome to the Demo Website</h1>
        <p>This is just a demo website.</p>
    </header>
    <main>
        <button id="demo-button">Click me!</button>
    </main>
    <footer>
        <p>This is a demo website. © 2023</p>
    </footer>
    <script src="main.js"></script>
</body>
</html>

/* ====== END OF FILE: demo/website/index.html ====== */



/* ====== START OF FILE: demo/website/main.css ====== */

body {
    font-family: Arial, sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

header {
    background-color: #0080ff;
    color: #fff;
    padding: 20px;
    text-align: center;
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #0080ff;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 18px;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
}

/* ====== END OF FILE: demo/website/main.css ====== */



/* ====== START OF FILE: demo/website/main.js ====== */

document.getElementById('demo-button').addEventListener('click', function() {
    alert('You clicked the button on the Demo Website!');
});

/* ====== END OF FILE: demo/website/main.js ====== */


```

-------- END OF FILE: README.md --------



-------- START OF FILE: demo/contracts/demo.sol --------

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Demo {
    string public greeting;

    constructor(string memory _greeting) {
        greeting = _greeting;
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function getGreeting() public view returns(string memory) {
        return greeting;
    }
}


-------- END OF FILE: demo/contracts/demo.sol --------



-------- START OF FILE: demo/contracts/demo.vy --------

greeting: public(string)

@public
def __init__(_greeting: string):
    self.greeting = _greeting

@public
def setGreeting(_greeting: string):
    self.greeting = _greeting

@public
@view
def getGreeting() -> string:
    return self.greeting


-------- END OF FILE: demo/contracts/demo.vy --------



-------- START OF FILE: demo/data/demo.csv --------

Company Name,Street,City,Country,First Name,Last Name,Email,Age,Department,Skills
Tech Corp,123 Tech Road,Techville,USA,John,Doe,john@example.com,30,HR,"communication,organization"
Tech Corp,123 Tech Road,Techville,USA,Anna,Smith,anna@example.com,31,Sales,"sales,marketing"
Tech Corp,123 Tech Road,Techville,USA,Peter,Jones,peter@example.com,24,Development,"programming,testing"

-------- END OF FILE: demo/data/demo.csv --------



-------- START OF FILE: demo/data/demo.json --------

{
    "company": {
        "name": "Tech Corp",
        "address": {
            "street": "123 Tech Road",
            "city": "Techville",
            "country": "USA"
        },
        "employees": [
            {
                "firstName": "John",
                "lastName": "Doe",
                "email": "john@example.com",
                "age": 30,
                "department": "HR",
                "skills": ["communication", "organization"]
            },
            {
                "firstName": "Anna",
                "lastName": "Smith",
                "email": "anna@example.com",
                "age": 31,
                "department": "Sales",
                "skills": ["sales", "marketing"]
            },
            {
                "firstName": "Peter",
                "lastName": "Jones",
                "email": "peter@example.com",
                "age": 24,
                "department": "Development",
                "skills": ["programming", "testing"]
            }
        ]
    }
}

-------- END OF FILE: demo/data/demo.json --------



-------- START OF FILE: demo/data/demo.yaml --------

company:
  name: Tech Corp
  address:
    street: 123 Tech Road
    city: Techville
    country: USA
  employees:
    - firstName: John
      lastName: Doe
      email: john@example.com
      age: 30
      department: HR
      skills:
        - communication
        - organization
    - firstName: Anna
      lastName: Smith
      email: anna@example.com
      age: 31
      department: Sales
      skills:
        - sales
        - marketing
    - firstName: Peter
      lastName: Jones
      email: peter@example.com
      age: 24
      department: Development
      skills:
        - programming
        - testing

-------- END OF FILE: demo/data/demo.yaml --------



-------- START OF FILE: demo/demo.c --------

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

-------- END OF FILE: demo/demo.c --------



-------- START OF FILE: demo/demo.cpp --------

#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

-------- END OF FILE: demo/demo.cpp --------



-------- START OF FILE: demo/demo.cs --------

using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}

-------- END OF FILE: demo/demo.cs --------



-------- START OF FILE: demo/demo.py --------

print("Hello, World!")

-------- END OF FILE: demo/demo.py --------



-------- START OF FILE: demo/demo.rb --------

puts "Hello, World!"

-------- END OF FILE: demo/demo.rb --------



-------- START OF FILE: demo/main.go --------

package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

-------- END OF FILE: demo/main.go --------



-------- START OF FILE: demo/Main.java --------

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

-------- END OF FILE: demo/Main.java --------



-------- START OF FILE: demo/main.rs --------

fn main() {
    println!("Hello, World!");
}

-------- END OF FILE: demo/main.rs --------



-------- START OF FILE: demo/main.swift --------

import Swift
print("Hello, World!")

-------- END OF FILE: demo/main.swift --------



-------- START OF FILE: demo/website/index.html --------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Website</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <header>
        <h1>Welcome to the Demo Website</h1>
        <p>This is just a demo website.</p>
    </header>
    <main>
        <button id="demo-button">Click me!</button>
    </main>
    <footer>
        <p>This is a demo website. © 2023</p>
    </footer>
    <script src="main.js"></script>
</body>
</html>

-------- END OF FILE: demo/website/index.html --------



-------- START OF FILE: demo/website/main.css --------

body {
    font-family: Arial, sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

header {
    background-color: #0080ff;
    color: #fff;
    padding: 20px;
    text-align: center;
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #0080ff;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 18px;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
}

-------- END OF FILE: demo/website/main.css --------



-------- START OF FILE: demo/website/main.js --------

document.getElementById('demo-button').addEventListener('click', function() {
    alert('You clicked the button on the Demo Website!');
});

-------- END OF FILE: demo/website/main.js --------

```