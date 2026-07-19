#include "raylib.h"
#include <stdio.h>

int main(void)
{
    // Инициализация окна
    InitWindow(1280, 720, "Homeless Simulator - Bench Test");
    SetTargetFPS(60);

    // Загрузка модели лавочки
    Model bench = LoadModel("assets/models/bench.glb");
    
    // Настройка позиции лавочки (x, y, z)
    Vector3 benchPosition = { 0.0f, 0.0f, 0.0f };

    // Настройка камеры от 3-го лица
    Camera camera = { 0 };
    camera.position = (Vector3){ 3.0f, 2.5f, 3.0f }; // Позиция камеры
    camera.target = (Vector3){ 0.0f, 1.0f, 0.0f };   // Куда смотрит камера (центр лавочки)
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };       // Верхний вектор
    camera.fovy = 45.0f;                              // Угол обзора
    camera.projection = CAMERA_PERSPECTIVE;

    while (!WindowShouldClose())
    {
        // Обновление камеры (можно крутить мышкой)
        UpdateCamera(&camera, CAMERA_ORBITAL);

        BeginDrawing();
            ClearBackground(RAYWHITE);

            BeginMode3D(camera);
                // Рисуем сетку пола для ориентира
                DrawGrid(10, 1.0f);
                
                // Рисуем лавочку
                DrawModel(bench, benchPosition, 1.0f, WHITE);
            EndMode3D();

            // Текст подсказки
            DrawText("Лавочка загружена!", 10, 10, 20, BLACK);
            DrawText("Крути камеру мышкой", 10, 40, 20, DARKGRAY);
        EndDrawing();
    }

    // Очистка памяти
    UnloadModel(bench);
    CloseWindow();

    return 0;
}