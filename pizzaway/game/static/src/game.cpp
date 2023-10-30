#include "game.h"

Game::Game(int p_width, int p_height, const char *p_title)
    : m_running(true), m_window(nullptr), m_renderer(nullptr), m_mousePressed(false), m_mousePos(), m_offset(), m_itemToMove(nullptr), m_items(), m_textures(), m_combinations()
{
    if (SDL_Init(SDL_INIT_VIDEO) != 0)
    {
        std::cerr << "Failed to init SDL" << std::endl;
        return;
    }
    if (!IMG_Init(IMG_INIT_PNG))
    {
        std::cerr << "Failed to init IMG" << std::endl;
        return;
    }

    m_window = SDL_CreateWindow(p_title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, p_width, p_height, SDL_WINDOW_SHOWN);
    m_renderer = SDL_CreateRenderer(m_window, 0, SDL_RENDERER_ACCELERATED);
    SDL_SetRenderDrawColor(m_renderer, 255, 255, 255, 255);

    SDL_GetMouseState(&m_mousePos.x, &m_mousePos.y);

    m_items.push_back(Item(200, 200, 100, 100, Type::Pot));
    m_items.push_back(Item(200, 200, 100, 100, Type::Seed));
    m_items.push_back(Item(200, 200, 100, 100, Type::Blender));
    m_items.push_back(Item(200, 200, 100, 100, Type::DNA));
    m_items.push_back(Item(200, 200, 100, 100, Type::Water));
    m_items.push_back(Item(200, 200, 100, 100, Type::Grass));
    m_items.push_back(Item(200, 200, 100, 100, Type::Wheat));
    m_items.push_back(Item(200, 200, 100, 100, Type::WashingMachine));
    m_items.push_back(Item(200, 200, 100, 100, Type::Pickaxe));
    m_items.push_back(Item(200, 200, 100, 100, Type::MetalMine));
    m_items.push_back(Item(200, 200, 100, 100, Type::Bricks));
    m_items.push_back(Item(200, 200, 100, 100, Type::Glue));
    m_items.push_back(Item(200, 200, 100, 100, Type::Chainsaw));
    m_items.push_back(Item(200, 200, 100, 100, Type::Fire));

    m_textures.insert_or_assign(Type::Undefined, nullptr);
    m_textures.insert_or_assign(Type::Failed, nullptr);
    m_textures.insert_or_assign(Type::Pot, IMG_LoadTexture(m_renderer, "res/pot.png"));
    m_textures.insert_or_assign(Type::Seed, IMG_LoadTexture(m_renderer, "res/seed.png"));
    m_textures.insert_or_assign(Type::Blender, IMG_LoadTexture(m_renderer, "res/blender.png"));
    m_textures.insert_or_assign(Type::Tomato, IMG_LoadTexture(m_renderer, "res/tomato.png"));
    m_textures.insert_or_assign(Type::Sauce, IMG_LoadTexture(m_renderer, "res/sauce.png"));
    m_textures.insert_or_assign(Type::DNA, IMG_LoadTexture(m_renderer, "res/dna.png"));
    m_textures.insert_or_assign(Type::Water, IMG_LoadTexture(m_renderer, "res/water.png"));
    m_textures.insert_or_assign(Type::Cow, IMG_LoadTexture(m_renderer, "res/cow.png"));
    m_textures.insert_or_assign(Type::Grass, IMG_LoadTexture(m_renderer, "res/grass.png"));
    m_textures.insert_or_assign(Type::Milk, IMG_LoadTexture(m_renderer, "res/milk.png"));
    m_textures.insert_or_assign(Type::WashingMachine, IMG_LoadTexture(m_renderer, "res/washingmachine.png"));
    m_textures.insert_or_assign(Type::Cheese, IMG_LoadTexture(m_renderer, "res/cheese.png"));
    m_textures.insert_or_assign(Type::Wheat, IMG_LoadTexture(m_renderer, "res/wheat.png"));
    m_textures.insert_or_assign(Type::Flour, IMG_LoadTexture(m_renderer, "res/flour.png"));
    m_textures.insert_or_assign(Type::Dough, IMG_LoadTexture(m_renderer, "res/dough.png"));
    m_textures.insert_or_assign(Type::DoughWithSauce, IMG_LoadTexture(m_renderer, "res/doughwithsauce.png"));
    m_textures.insert_or_assign(Type::Base, IMG_LoadTexture(m_renderer, "res/base.png"));
    m_textures.insert_or_assign(Type::MetalMine, IMG_LoadTexture(m_renderer, "res/metalmine.png"));
    m_textures.insert_or_assign(Type::Pickaxe, IMG_LoadTexture(m_renderer, "res/pickaxe.png"));
    m_textures.insert_or_assign(Type::Knife, IMG_LoadTexture(m_renderer, "res/knife.png"));
    m_textures.insert_or_assign(Type::Meat, IMG_LoadTexture(m_renderer, "res/meat.png"));
    m_textures.insert_or_assign(Type::RawPizza, IMG_LoadTexture(m_renderer, "res/rawpizza.png"));
    m_textures.insert_or_assign(Type::Bricks, IMG_LoadTexture(m_renderer, "res/bricks.png"));
    m_textures.insert_or_assign(Type::Glue, IMG_LoadTexture(m_renderer, "res/glue.png"));
    m_textures.insert_or_assign(Type::EmptyOven, IMG_LoadTexture(m_renderer, "res/emptyoven.png"));
    m_textures.insert_or_assign(Type::Tree, IMG_LoadTexture(m_renderer, "res/tree.png"));
    m_textures.insert_or_assign(Type::Chainsaw, IMG_LoadTexture(m_renderer, "res/chainsaw.png"));
    m_textures.insert_or_assign(Type::Wood, IMG_LoadTexture(m_renderer, "res/wood.png"));
    m_textures.insert_or_assign(Type::OvenWithWood, IMG_LoadTexture(m_renderer, "res/ovenwithpizza.png"));
    m_textures.insert_or_assign(Type::Fire, IMG_LoadTexture(m_renderer, "res/fire.png"));
    m_textures.insert_or_assign(Type::Oven, IMG_LoadTexture(m_renderer, "res/oven.png"));
    m_textures.insert_or_assign(Type::Pizza, IMG_LoadTexture(m_renderer, "res/pizza.png"));

    for (std::pair<Type, SDL_Texture*> pair : m_textures)
    {
        if (pair.second == nullptr)
            std::cerr << "Failed to load image for " << (int)pair.first << std::endl;
    }

    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Pot, Type::Seed), Type::Tomato));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Tomato, Type::Blender), Type::Sauce));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::DNA, Type::Water), Type::Cow));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Cow, Type::Grass), Type::Milk));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Milk, Type::WashingMachine), Type::Cheese));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Wheat, Type::Blender), Type::Flour));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Flour, Type::Milk), Type::Dough));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Dough, Type::Sauce), Type::DoughWithSauce));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::DoughWithSauce, Type::Cheese), Type::Base));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::MetalMine, Type::Pickaxe), Type::Knife));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Cow, Type::Knife), Type::Meat));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Base, Type::Meat), Type::RawPizza));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Bricks, Type::Glue), Type::EmptyOven));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Tree, Type::Chainsaw), Type::Wood));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::EmptyOven, Type::Wood), Type::OvenWithWood));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::OvenWithWood, Type::Fire), Type::Oven));
    m_combinations.push_back(std::make_pair<std::pair<Type, Type>, Type>(std::make_pair(Type::Oven, Type::RawPizza), Type::Pizza));

}

Game::~Game() {}

Item Game::combineItems(Item &item, Item &otherItem)
{
    Type t1 = item.getType();
    Type t2 = otherItem.getType();

    switch (t1)
    {
        case Type::Undefined: break;
    }

    return Item();
}

void Game::draw()
{
    SDL_RenderClear(m_renderer);
    for (Item &i : m_items)
        SDL_RenderCopy(m_renderer, m_textures.at(i.getType()), nullptr, i.getDst());

    SDL_RenderPresent(m_renderer);
}

void Game::handleInput()
{
    SDL_Event evt;
    while (SDL_PollEvent(&evt))
    {
        if (evt.type == SDL_QUIT)
        {
            m_running = false;
        }

        if (evt.type == SDL_MOUSEBUTTONDOWN && !m_mousePressed && evt.button.button == SDL_BUTTON_LEFT)
        {
            m_mousePressed = true;
        
            for (Item &i : m_items)
            {
                if (SDL_PointInRect(&m_mousePos, i.getDst()))
                {
                    m_itemToMove = &i;
                    m_offset.x = m_mousePos.x - i.getDst()->x;
                    m_offset.y = m_mousePos.y - i.getDst()->y;
                    break;
                }
            }
        }

        if (evt.type == SDL_MOUSEMOTION)
        {
            m_mousePos = { evt.motion.x, evt.motion.y };
            if (m_mousePressed && m_itemToMove != nullptr)
            {
                m_itemToMove->setPos(m_mousePos.x - m_offset.x, m_mousePos.y - m_offset.y);
            }
        }

        if (evt.type == SDL_MOUSEBUTTONUP && evt.button.button == SDL_BUTTON_LEFT)
        {
            m_mousePressed = false;
            m_itemToMove = nullptr;
        }
    }
}

void Game::run()
{
    while (m_running)
    {
        handleInput();
        draw();
    }
}

void Game::cleanUp()
{
    SDL_DestroyWindow(m_window);
    SDL_Quit();
}

/*
Pot + Seed = Tomato
Tomato + Blender = Sauce
DNA + Water = Cow
Cow + Grass = Milk
Milk + WashingMachine = Cheese
Wheat + Blender = Flour
Flour + Milk = Dough
Dough + Sauce = DoughWithSauce
DoughWithSauce + Cheese = Base
MetalMine + Pickaxe = Knife
Cow + Knife = Meat
Base + Meat = RawPizza
Bricks + Glue = EmptyOven
Tree + Chainsaw = Wood
EmptyOven + Wood = OvenWithWood
OvenWithWood + Fire = Oven
RawPizza + Oven = Pizza 
*/

/*
Beginning = Pot Seed Blender DNA Water Gras Wheat WashingMachine Pickaxe MetalMine Bricks Glue Tree Chainsaw Fire
*/
