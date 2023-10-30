#include "game.h"

#define WIDTH 1000
#define HEIGHT 750

int main()
{
    Game game(WIDTH, HEIGHT, "Get the pizza");

    game.run();
    game.cleanUp();

    return 0;
}
