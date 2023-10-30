#pragma once

#include <iostream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

class Item
{
private:
    SDL_Texture *m_texture;
    SDL_Rect m_dst;

public:
    Item(const char *p_texturePath, int p_x, int p_y, int p_w, int p_h, SDL_Renderer *p_renderer);
    ~Item();

    SDL_Rect *getDst();
    SDL_Texture *getTexture();


    void setPos(int p_x, int p_y);
};