#pragma once

#include <iostream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

enum class Type
{
    Undefined = -2,
    Failed = -1,
    Pot = 0,
    Seed = 1,
    Blender = 2,
    Tomato = 3,
    Sauce = 4,
    DNA = 5,
    Water = 6,
    Cow = 7,
    Grass = 8,
    Milk = 9,
    WashingMachine = 10,
    Cheese = 11,
    Wheat = 12,
    Flour = 13,
    Dough = 14,
    DoughWithSauce = 15,
    Base = 16,
    MetalMine = 17,
    Pickaxe = 18,
    Knife = 19,
    Meat = 20,
    RawPizza = 21,
    Bricks = 22,
    Glue = 23,
    EmptyOven = 24,
    Tree = 25,
    Chainsaw = 26,
    Wood = 27,
    OvenWithWood = 28,
    Fire = 29,
    Oven = 30,
    Pizza = 31
};

class Item
{
private:
    bool m_inGame;
    SDL_Rect m_dst;
    Type m_type;
    short m_timesCombined;

public:
    Item(int p_x, int p_y, int p_w, int p_h, Type p_type);
    Item();
    ~Item();

    SDL_Rect *getDst();
    Type getType();


    void setPos(int p_x, int p_y);
    bool getInGame();
    void setInGame(bool p_inGame);
    short getTimesCombined();
    void increaseTimesCombined();
};
