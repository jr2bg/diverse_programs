/*This source code copyrighted by Lazy Foo' Productions (2004-2019)
and may not be redistributed without written permission.*/

// g++ 08_geometry_rendering.cpp -w -lSDL2 -lSDL2_image -o tut_SDL

//Using SDL, SDL_image, standard IO, math, and strings
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <stdio.h>
#include <string>
#include <cmath>
#include <vector>
// header de GOL
#include "GOL_header.h"

// //Screen dimension constants
// const int SCREEN_WIDTH = 640;
// const int SCREEN_HEIGHT = 480;

//Starts up SDL and creates window
bool init(int SCREEN_WIDTH, int SCREEN_HEIGHT);

//Loads media
bool loadMedia();

//Frees media and shuts down SDL
void close();

//Loads individual image as texture
SDL_Texture* loadTexture( std::string path );

//The window we'll be rendering to
SDL_Window* gWindow = NULL;

//The window renderer
SDL_Renderer* gRenderer = NULL;

bool init(int SCREEN_WIDTH, int SCREEN_HEIGHT)
{
	//Initialization flag
	bool success = true;

	//Initialize SDL
	if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
	{
		printf( "SDL could not initialize! SDL Error: %s\n", SDL_GetError() );
		success = false;
	}
	else
	{
		//Set texture filtering to linear
		if( !SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, "1" ) )
		{
			printf( "Warning: Linear texture filtering not enabled!" );
		}

		//Create window
		gWindow = SDL_CreateWindow( "GOL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN );
		if( gWindow == NULL )
		{
			printf( "Window could not be created! SDL Error: %s\n", SDL_GetError() );
			success = false;
		}
		else
		{
			//Create renderer for window
			gRenderer = SDL_CreateRenderer( gWindow, -1, SDL_RENDERER_ACCELERATED );
			if( gRenderer == NULL )
			{
				printf( "Renderer could not be created! SDL Error: %s\n", SDL_GetError() );
				success = false;
			}
			else
			{
				//Initialize renderer color
				SDL_SetRenderDrawColor( gRenderer, 165, 165, 165, 255 );

				//Initialize PNG loading
				int imgFlags = IMG_INIT_PNG;
				if( !( IMG_Init( imgFlags ) & imgFlags ) )
				{
					printf( "SDL_image could not initialize! SDL_image Error: %s\n", IMG_GetError() );
					success = false;
				}
			}
		}
	}

	return success;
}

bool loadMedia()
{
	//Loading success flag
	bool success = true;

	//Nothing to load
	return success;
}

void close()
{
	//Destroy window
	SDL_DestroyRenderer( gRenderer );
	SDL_DestroyWindow( gWindow );
	gWindow = NULL;
	gRenderer = NULL;

	//Quit SDL subsystems
	IMG_Quit();
	SDL_Quit();
}

SDL_Texture* loadTexture( std::string path )
{
	//The final texture
	SDL_Texture* newTexture = NULL;

	//Load image at specified path
	SDL_Surface* loadedSurface = IMG_Load( path.c_str() );
	if( loadedSurface == NULL )
	{
		printf( "Unable to load image %s! SDL_image Error: %s\n", path.c_str(), IMG_GetError() );
	}
	else
	{
		//Create texture from surface pixels
        newTexture = SDL_CreateTextureFromSurface( gRenderer, loadedSurface );
		if( newTexture == NULL )
		{
			printf( "Unable to create texture from %s! SDL Error: %s\n", path.c_str(), SDL_GetError() );
		}

		//Get rid of old loaded surface
		SDL_FreeSurface( loadedSurface );
	}

	return newTexture;
}





int main( int argc, char* args[] )
{ // pp_side -> pixels per side
  // n_cell -> identificar el barrido del array, para el render
  const int n_rows = 30, n_cols = 20, pp_side = 20, pp_line = 2;

	int i, j; // contadores para barrido

  // inicializando la lattice y la vecindad
  //int lattice[n_rows][n_cols], neighbourhood[3][3] = {};
  int **lattice = NULL, **n_lattice = NULL, neighbourhood[3][3] = {};

  // lista de la posición de las células vivas
  int al_cells[5][2] = {{10,11},{15,14},{24,8},{7,11},{9,1}};
  //Screen dimension constants
  const int SCREEN_WIDTH = n_cols * (pp_side + pp_line)-pp_line;
  const int SCREEN_HEIGHT = n_rows * (pp_side + pp_line)-pp_line;
  const int TOTAL_CELLS = n_rows * n_cols;

  // // INICIALIZACIÓN DE LOS ESTADOS
	std::vector<SDL_Rect> live_cells, death_cells;

	// Generación de la lattice
  lattice = new int *[n_rows];
  n_lattice = new int *[n_rows];
  for (int i = 0; i < n_rows; i++){
    lattice[i] = new int[n_cols];
    n_lattice[i] = new int[n_cols];
  }
  for (i = 0; i < n_rows; i++){
    for (j = 0; j < n_cols; j++) {
      lattice[i][j] = 0;
      n_lattice[i][j] = 0;
    }
  }
  // Término de la creación de la lattice




  // SDL_Rect *fillRect =NULL;
  // // REQUEST PARA MEMORIA DE TODAS LAS CELDAS
  // fillRect = new SDL_Rect [TOTAL_CELLS];

	//Start up SDL and create window
	if( !init(SCREEN_WIDTH, SCREEN_HEIGHT) )
	{
		printf( "Failed to initialize!\n" );
	}
	else
	{
		//Load media
		if( !loadMedia() )
		{
			printf( "Failed to load media!\n" );
		}
		else
		{
			//Main loop flag
			bool quit = false;

			//Event handler
			SDL_Event e;

			//While application is running
			while( !quit )
			{
				//Handle events on queue
				while( SDL_PollEvent( &e ) != 0 )
				{
					//User requests quit
					if( e.type == SDL_QUIT )
					{
						quit = true;
					}
					// selección de los lados negros
					else if (e.type == SDL_MOUSEBUTTONDOWN){
						if (e.button.button == SDL_BUTTON_LEFT){
							printf("--- LEFT PUSHED---\n");
							printf("x ->  %d; y -> %d\n", e.button.x, e.button.y);
							printf("c ->  %d; r -> %d\n", e.button.x / (pp_side + pp_line),
																						e.button.y/ (pp_side + pp_line));
						}
					}
				}

				//Clear screen; gray background
				SDL_SetRenderDrawColor( gRenderer, 165, 165, 165, 255 );
				SDL_RenderClear( gRenderer );

				//Render white filled quad
				SDL_SetRenderDrawColor( gRenderer, 255, 255, 255, 255 );

        // INICIALIZACIÓN DEL GRID
        // SDL_Rect *live_cells =NULL, *death_cells = NULL;
        // // REQUEST PARA MEMORIA DE TODAS LAS CELDAS
        // live_cells = new SDL_Rect [TOTAL_CELLS];
        // death_cells = new SDL_Rect [TOTAL_CELLS];
				//
        // // creación de las posiciones de los cuadros
        // for (int r = 0; r < n_rows; r++){
        //   for (int c = 0; c < n_cols ; c++){
        //     *(death_cells + n_cell[0]) = {c*(pp_side +pp_line),r * (pp_side +pp_line), pp_side, pp_side};
        //     n_cell[0]++;
        //   }
        // }
				//
        // for (n_cell[0] = 0; n_cell[0] < TOTAL_CELLS; n_cell[0]++) {
        //   SDL_RenderFillRect( gRenderer, death_cells + n_cell[0]);
        // }
				//
        // // reinicialización de la posición original
        // n_cell[0] = 0;
        // n_cell[1] = 0;




				// creación de las posiciones de los cuadros
        for (int r = 0; r < n_rows; r++){
          for (int c = 0; c < n_cols ; c++){
						if ((r == 2 || r == 15) && (c == 6 || c == 3)){
							live_cells.push_back({c*(pp_side +pp_line),r * (pp_side +pp_line), pp_side, pp_side});
						}
						else {
          		death_cells.push_back({c*(pp_side +pp_line),r * (pp_side +pp_line), pp_side, pp_side});
						}
          }
        }
				// renderización
        for (auto const &w : death_cells) {
          SDL_RenderFillRect( gRenderer, &w);
        }

				//Render black filled quad
				SDL_SetRenderDrawColor( gRenderer,0, 0, 0, 255 );
				for (auto const &w : live_cells) {
          SDL_RenderFillRect( gRenderer, &w);
        }

        // // reinicialización de la posición original
        // n_cell[0] = 0;
        // n_cell[1] = 0;




				//Update screen
				SDL_RenderPresent( gRenderer );
        // delay de 200 milisegundos
        SDL_Delay(200);
        //delete [] death_cells;
				death_cells.clear();
				live_cells.clear();
			}
		}
	}

	//Free resources and close SDL
	close();

	return 0;
}
