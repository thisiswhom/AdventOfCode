#include <iostream>
#include <set>
#include <string>

int count_houses_with_robo(const std::string& instructions) {
    // Position tracking for Santa and Robo-Santa
    int santa_x = 0, santa_y = 0;
    int robo_x = 0, robo_y = 0;

    // Shared set of visited locations
    std::set<std::pair<int, int>> visited;
    visited.insert({0, 0}); // Starting house gets a present

    // Iterate through instructions, alternating between Santa and Robo-Santa
    for (size_t i = 0; i < instructions.size(); ++i) {
        char move = instructions[i];

        // Determine who's moving: Santa on even, Robo on odd
        int& x = (i % 2 == 0) ? santa_x : robo_x;
        int& y = (i % 2 == 0) ? santa_y : robo_y;

        switch (move) {
            case '^': y += 1; break;
            case 'v': y -= 1; break;
            case '>': x += 1; break;
            case '<': x -= 1; break;
            default:
                // Invalid character – ignore or handle error
                std::cerr << "Warning: Invalid direction '" << move << "' ignored.\n";
                continue;
        }

        visited.insert({x, y});
    }

    return visited.size();
}

int main() {
    std::string input;

    std::cout << "Enter directions (^ v < >): ";
    std::cin >> input;

    int result = count_houses_with_robo(input);
    std::cout << "Unique houses visited (with Robo-Santa): " << result << std::endl;

    return 0;
}
