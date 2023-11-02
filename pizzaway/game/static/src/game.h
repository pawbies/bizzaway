#pragma once

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

#include "item.h"

#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#endif

class Game 
{
private:
    bool m_running;
    SDL_Window *m_window;
    SDL_Renderer *m_renderer;
    bool m_mousePressed;
    SDL_Point m_mousePos;
    SDL_Point m_offset;
    Item *m_itemToMove;
    std::vector<Item> m_items;
    std::map<Type, SDL_Texture*> m_textures;
    std::vector<std::pair<std::pair<Type, Type>, Type>> m_combinations;

    Item combineItems(Item &item, Item &otherItem);

    void draw();
    void handleInput();


public:

    Game(int p_width, int p_height, const char *p_title);
    ~Game();

    void run();
    void cleanUp();
};