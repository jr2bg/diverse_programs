/*************************************************

g++ julia_set.cpp -w -lSDL2 -lSDL2_image -o julia

**************************************************/

#include <SDL2/SDL.h>
#include <stdio.h>
//#define _USE_MATH_DEFINES
#include <math.h>
// #ifndef M_PI
// #define M_PI (3.14159265358979323846)
// #endif


struct ComplexNumb {
  float real, img;
};

ComplexNumb complexMult(ComplexNumb a, ComplexNumb b) {
  ComplexNumb result;
  result.real = a.real * b.real - a.img * b.img;
  result.img = a.real * b.img + a.img * b.real;
  return result;
}

ComplexNumb complexSum(ComplexNumb a, ComplexNumb b) {
  ComplexNumb result;
  result.real = a.real + b.real;
  result.img = a.img + b.img;
  return result;
}

float complexMod(ComplexNumb a) {
  return a.real * a.real + a.img * a.img;
}

// iteración  para el conjunto de Julia
ComplexNumb Julia_set_it(ComplexNumb z_n, ComplexNumb c) {
  z_n = complexSum(complexMult(z_n, z_n), c);
  return z_n;
}

ComplexNumb init_z_n(ComplexNumb z_n, int n_rows, int n_cols, int i, int j) {
  z_n.real = 1.5 *((float)j - (float)n_cols / 2) / ((float)n_cols / 2);
  z_n.img =  ((float)i - (float)n_rows / 2) / ((float)n_rows / 2);
  return z_n;
}


int it_number(ComplexNumb z_n, ComplexNumb c, int n_rows, int n_cols, int i, int j, int R) {
  int k = 0;
  float c_mod;
  z_n = init_z_n(z_n, n_rows , n_cols, i , j);
  //printf("real   %f     img   %f\n", z_n.real, z_n.img);
  c_mod = complexMod(z_n);
  while ( c_mod < R * R && k < 255) {
    z_n = Julia_set_it(z_n, c);
    c_mod = complexMod(z_n);
    //printf("it %i:\treal %f\timaginaria %f\tmod %f\n", k, z_n.real, z_n.img, c_mod);
    k++;
  }
  return k;
}




int main(int argc, char const *argv[]) {
  ComplexNumb z_n, c;
  const int n_rows = 500, n_cols = 800, R = 2;
  int k = 1; // mult  2PI

  // espacio, 400 filas x 500 columnas
  int space[n_rows][n_cols] = {};
  printf("%f\n", M_PI);
  c.real = -0.7;
  c.img = 0.27015;
  /////////
  // c.real = 0.36;
  // c.img = 0.1;
  /////////
  // c.real = -0.48;
  // c.img = -0.53;

  // c.real = 0.7885 * sin(2*M_PI * k / 40);
  // c.img = 0.7885 * cos(2*M_PI * k / 40);
  //
  // for (int i = 0; i < n_rows; i++) {
  //   for (int j = 0; j < n_cols ; j++) {
  //     space[i][j] = it_number(z_n, c, n_rows, n_cols, i, j, R);
  //   }
  // }



  SDL_Window  * window = nullptr;
  SDL_Renderer * renderer = nullptr;
  SDL_Texture * texture = nullptr;
  SDL_Surface * surface = nullptr;


  //void * pixels;
  uint8_t * pixels;
  int pitch, p_color;
  //Uint32 RGBmask;

  if (SDL_Init(SDL_INIT_VIDEO < 0)) {
    printf("VIDEO NOT INITIALIZED:    %s\n", SDL_GetError());
    return -1;
  }

  window = SDL_CreateWindow( "JULIA SET VIDEO", SDL_WINDOWPOS_UNDEFINED,
                            SDL_WINDOWPOS_UNDEFINED, n_cols, n_rows,
                            SDL_WINDOW_SHOWN );
  if (window == nullptr) {
    printf("WINDOW NOT CREATED:    %s\n", SDL_GetError());
    SDL_Quit();
    return -1;
  }

  renderer = SDL_CreateRenderer( window, -1,
                        SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC );

  if (renderer == nullptr){
	SDL_DestroyWindow(window);
  printf("RENDERER NOT CREATED:    %s\n", SDL_GetError());
	SDL_Quit();
	return -1;
  }

  texture = SDL_CreateTexture(renderer,
                            SDL_PIXELFORMAT_ARGB8888,
                            SDL_TEXTUREACCESS_STREAMING,
                            n_cols, n_rows);

  if (texture == nullptr){
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
  printf("TEXTURE NOT CREATED:    %s\n", SDL_GetError());
	SDL_Quit();
	return -1;
  }


  surface = SDL_CreateRGBSurfaceFrom(nullptr,
                                   n_cols, n_rows,
                                   32, 0,
                                   0x00FF0000,
                                   0x0000FF00,
                                   0x000000FF,
                                   0xFF000000);
 if (surface == nullptr){
 	SDL_DestroyRenderer(renderer);
 	SDL_DestroyWindow(window);
  printf("SURFACE NOT CREATED:    %s\n", SDL_GetError());
 	SDL_Quit();
 	return 1;
  }

  bool quit = false;

  SDL_Event event;

  while (!quit){

    while( SDL_PollEvent( &event ) != 0 )
    {
      //User requests quit
      if( event.type == SDL_QUIT )
      {
        quit = true;
      }
    }
    c.real = 0.7885 * sin(2*M_PI * k / 40);
    c.img = 0.7885 * cos(2*M_PI * k / 40);

    for (int i = 0; i < n_rows; i++) {
      for (int j = 0; j < n_cols ; j++) {
        space[i][j] = it_number(z_n, c, n_rows, n_cols, i, j, R);
      }
    }
    k++;

    SDL_LockTexture(texture, nullptr, (void **)&pixels, &pitch);
    for (int y = 0; y < n_rows; y++) {
      Uint32 *p = (Uint32 *)(pixels + pitch*y); // cast for a pointer increments by 4 bytes.(RGBA)
      for (int x = 0; x < n_cols; x++) {
        // color
        p_color = space[y][x];
        // colores chidoris (0-7 azul) (8-15 verde) (16-23 rojo)
        *p = p_color<<2  | p_color << 11 | p_color <<21;
        p++;
      }
    }
    SDL_UnlockTexture(texture);


    SDL_RenderClear(renderer);
    SDL_RenderCopy(renderer, texture, nullptr, nullptr);

    SDL_RenderPresent(renderer);

    SDL_Delay( 50 );
  }


  //Destroy window
  SDL_FreeSurface(surface);
  SDL_DestroyTexture( texture );
	SDL_DestroyRenderer( renderer );
	SDL_DestroyWindow( window );

	window = nullptr;
	renderer = nullptr;

  return 0;
}
