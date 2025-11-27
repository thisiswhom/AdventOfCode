#include <iostream>
#include <set>
#include <string>

int count_houses(const std::string& instructions) {
    int x = 0, y = 0;
    std::set<std::pair<int, int>> visited;
    visited.insert({x, y});

    for (char move : instructions) {
        switch (move) {
            case '^': y += 1; break;
            case 'v': y -= 1; break;
            case '>': x += 1; break;
            case '<': x -= 1; break;
        }
        visited.insert({x, y});
    }

    return visited.size();
}

int main() {
    std::string input;

    std::cout << "Enter directions (^ v < >): ";
    std::cin >> input;

    int result = count_houses(input);
    std::cout << "Unique houses visited: " << result << std::endl;

    return 0;
}
