#include <iostream>
#include <stack>
#include <string>

class TextEditor {
private:
    std::string text;
    std::stack<std::string> undoStack;
    std::stack<std::string> redoStack;

public:
    void type(const std::string& newText) {
        undoStack.push(text);
        text += newText;
        while (!redoStack.empty()) {
            redoStack.pop();
        }
    }

    void undo() {
        if (undoStack.empty()) {
            std::cout << "Undo stack is empty." << std::endl;
            return;
        }
        redoStack.push(text);
        text = undoStack.top();
        undoStack.pop();
    }

    void redo() {
        if (redoStack.empty()) {
            std::cout << "Redo stack is empty." << std::endl;
            return;
        }
        undoStack.push(text);
        text = redoStack.top();
        redoStack.pop();
    }

    bool isEmptyUndo() const {
        return undoStack.empty();
    }

    bool isEmptyRedo() const {
        return redoStack.empty();
    }

    void printText() const {
        std::cout << "Current text: " << text << std::endl;
    }
};

void displayMenu() {
    std::cout << "Menu:\n";
    std::cout << "1. Ketik\n";
    std::cout << "2. Undo\n";
    std::cout << "3. Redo\n";
    std::cout << "4. IsEmptyUndo\n";
    std::cout << "5. IsEmptyRedo\n";
    std::cout << "6. Exit\n";
    std::cout << "Choose an option: ";
}

int main() {
    TextEditor editor;
    int choice;
    std::string inputText;

    while (true) {
        displayMenu();
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter text: ";
                std::cin.ignore();
                std::getline(std::cin, inputText);
                editor.type(inputText);
                editor.printText();
                break;
            case 2:
                editor.undo();
                editor.printText();
                break;
            case 3:
                editor.redo();
                editor.printText();
                break;
            case 4:
                std::cout << (editor.isEmptyUndo() ? "Undo stack is empty." : "Undo stack is not empty.") << std::endl;
                break;
            case 5:
                std::cout << (editor.isEmptyRedo() ? "Redo stack is empty." : "Redo stack is not empty.") << std::endl;
                break;
            case 6:
                std::cout << "Exiting..." << std::endl;
                return 0;
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    return 0;
}
