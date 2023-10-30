#include "item.h"

Item::Item(const char *p_texturePath, int p_x, int p_y, int p_w, int p_h, SDL_Renderer *p_renderer)
    : m_texture(nullptr), m_dst{p_x, p_y, p_w, p_h}
{
    m_texture = IMG_LoadTexture(p_renderer, p_texturePath);
    if (m_texture == nullptr)
    {
        std::cerr << "Failed to load texture " << p_texturePath << '!' << std::endl; 
    }
}

Item::~Item()
{
}

SDL_Rect *Item::getDst()
{
    return &m_dst;
}
SDL_Texture *Item::getTexture()
{
    return m_texture;
}
void Item::setPos(int p_x, int p_y)
{
    m_dst.x = p_x;
    m_dst.y = p_y;
}