# Each function returns a string — just the code content, nothing else.
# main.py handles creating folders and writing files.

def generate_go():
    return """package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
"""

def generate_python():
    # Fixed: was missing opening parenthesis on print
    return """def main():
    print("Program started!")
    # Your code here

if __name__ == "__main__":
    main()
"""

def generate_java():
    # Fixed: the return and the string were on separate lines, so it was returning None
    return """public class Main {
    public static void main(String[] args) {
        // Your code here
        System.out.println("Hello, world!");
    }
}
"""

def generate_typescript():
    return """function main() {
    console.log("Program started");
    // Your code here
}

main();
"""
