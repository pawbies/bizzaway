#include <iostream>
#include <raylib.h>

#define WIDTH 500
#define HEIGHT 500


int main()
{
    InitWindow(WIDTH, HEIGHT, "Title");

    Vector2 position;
    float radius = 3;

    while (!WindowShouldClose())
    {
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT))
            radius *= 1.05;
        position = GetMousePosition();

        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawCircleV(position, radius, RED);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
