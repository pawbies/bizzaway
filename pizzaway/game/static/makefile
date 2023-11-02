default:
	g++ src/*.cpp -o game -lSDL2 -lSDL2_image

wasm:
	em++ src/*.cpp -o game.js -s WASM=1 -s USE_SDL=2 -s USE_SDL_IMAGE=2 -s SDL2_IMAGE_FORMATS=["png"] --preload-file res -sSTACK_SIZE=5mb --emrun -s ASYNCIFY

clean:
	rm -rf build