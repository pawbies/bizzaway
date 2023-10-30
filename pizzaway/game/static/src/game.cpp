#include "game.h"

Game::Game(int p_width, int p_height, const char *p_title)
    : m_running(true), m_window(nullptr), m_renderer(nullptr), m_mousePressed(false), m_mousePos(), m_offset(), m_itemToMove(nullptr), m_items()
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

    m_items.push_back(Item("res/pizza.png", 200, 200, 100, 100, Type::Pizza, m_renderer));
    m_items.push_back(Item("res/pizza.png", 100, 200, 100, 100, Type::Pizza, m_renderer));
}

Game::~Game() {}



Item Game::combineItems(Item &item, Item &otherItem)
{
    return Item();
}


void Game::draw()
{
    //std::cout << m_items[0].getDst()->y << std::endl;
    SDL_RenderClear(m_renderer);
    for (Item &i : m_items)
        SDL_RenderCopy(m_renderer, i.getTexture(), nullptr, i.getDst());

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
Cow + Gras = Milk
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
