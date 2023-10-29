#include <iostream>
#include <raylib.h>

int main()
{
    InitWindow(500, 500, "Title");
    while (!WindowShouldClose())
    {
        BeginDrawing();
            ClearBackground(RAYWHITE);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
