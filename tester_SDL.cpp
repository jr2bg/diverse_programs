#include <SDL2/SDL.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[]) {
  // dimensiones del screen
  const int n_rows = 40, n_cols = 256;
  int color;

  SDL_Window  * window = nullptr;
  SDL_Renderer * renderer = nullptr;
  SDL_Texture * texture = nullptr;
  SDL_Surface * surface = nullptr;


  //void * pixels;
  uint8_t * pixels;
  int pitch;
  Uint32 RGBmask = 1;

  if (SDL_Init(SDL_INIT_VIDEO < 0)) {
    printf("VIDEO NOT INITIALIZED:    %s\n", SDL_GetError());
    return -1;
  }

  window = SDL_CreateWindow( "TESTER SDL", SDL_WINDOWPOS_UNDEFINED,
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

      else if (event.button.button == SDL_BUTTON_LEFT)
      {
        printf("%d\n", event.button.x);
      }
    }

    SDL_LockTexture(texture, nullptr, (void **)&pixels, &pitch);
    for (int y = 0; y < n_rows; y++) {
      Uint32 *p = (Uint32 *)(pixels + pitch*y); // cast for a pointer increments by 4 bytes.(RGBA)
      for (int x = 0; x < n_cols; x++) {
        // n = r256^2 + g256 + b
        //*p = 0x000000FF;
        // if (x <= 85)
        //   *p = SDL_MapRGBA(surface->format, x*2, 0, 0, 255);
        // else if (x <= 170)
        //   *p = SDL_MapRGBA(surface->format, 170+(x-85),0, 0, 255);
        // else
        //   *p = SDL_MapRGBA(surface->format, 255-(x-170)/2,x*3, 0, 255);

        // color = (int )((float )x/n_cols * 255);
        // *p = SDL_MapRGBA(surface->format, color, color, color, 255);

        //*p = (RGBmask << x%28) ;
        *p = x<<1| x << 10 | x <<21;
        // printf("%f\n", 256- 256/((float) x +1));
        // *p = (Uint32) (256- 256/((float) x +1));
        p++;
      }
    }
    SDL_UnlockTexture(texture);


    SDL_RenderClear(renderer);
    SDL_RenderCopy(renderer, texture, nullptr, nullptr);

    SDL_RenderPresent(renderer);

    SDL_Delay( 1000 );
  }


  //Destroy window
  SDL_FreeSurface(surface);
  SDL_DestroyTexture( texture );
	SDL_DestroyRenderer( renderer );
	SDL_DestroyWindow( window );

	window = nullptr;
	renderer = nullptr;

  //printf("%s\n", );

  return 0;
}
