#include "item.h"

Item::Item(int p_x, int p_y, int p_w, int p_h, Type p_type)
    : m_dst{p_x, p_y, p_w, p_h}, m_type(p_type)
{}
Item::Item()
    : m_dst{0, 0, 0, 0}, m_type(Type::Undefined)
{}

Item::~Item()
{
}

SDL_Rect *Item::getDst()
{
    return &m_dst;
}
Type Item::getType()
{
    return m_type;
}
void Item::setPos(int p_x, int p_y)
{
    m_dst.x = p_x;
    m_dst.y = p_y;
}