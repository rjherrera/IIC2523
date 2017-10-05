#include <stdio.h>
#include <stdlib.h>
#include "../imagelib/imagelib.h"

void img_destroy(Image* img){
    int height = img -> height;
    for (int row = 0; row < height; row++) {
        free(img -> pixels[row]);
    }
    free(img -> pixels);
    free(img);
}


int main(int argc, char *argv[]){
    if(argc != 6){
        printf("Modo de uso: %s <input.png> <kernel.txt> <output.png> <iteraciones> <n_threads>\n", argv[0]);
        printf("\t<input.png> es la imagen a filtrar\n");
        printf("\t<kernel.txt> es el filtro a usar\n");
        printf("\t<output.png> es donde se guardará la imagen resultante\n");
        printf("\t<iteraciones> es la cantidad de veces que se aplica el filtro\n");
        printf("\t<n_threads> es la cantidad de threads que se usan en la ejecución\n");
        return 1;
    }

    char* input_file = argv[1];
    Image* img = img_png_read_from_file(input_file);

    char* kernel_file = argv[2];
    FILE* file = fopen(kernel_file, "r");
    float data;
    int kernel_rows;
    int kernel_cols;
    fscanf(file, "%d", &kernel_rows);
    fscanf(file, "%d", &kernel_cols);
    float** kernel = malloc(kernel_rows * sizeof(float*));
    for (int i = 0; i < kernel_rows; i++) {
        kernel[i] = malloc(kernel_cols * sizeof(float));
        for (int j = 0; j < kernel_cols; j++) {
            fscanf(file, "%f", &data);
            kernel[i][j] = data;
        }
    }
    fclose(file);

    int n_iters = atoi(argv[4]);
    int height = img -> height;
    int width = img -> width;
    int margin_rows = kernel_rows / 2;
    int margin_cols = kernel_cols / 2;
    for (int it = 0; it < n_iters; it++){
        // generate pixels matrix for temporary placing the new rgb values
        Color** new_pixels = calloc(height, sizeof(Color*));
        for(int row = 0; row < height; row++){
            new_pixels[row] = calloc(width, sizeof(Color));
            for(int col = 0; col < width; col++){
                new_pixels[row][col].R = 0.f;
                new_pixels[row][col].G = 0.f;
                new_pixels[row][col].B = 0.f;
            }
        }
        #pragma omp parallel for num_threads(argv[5])
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                float suma[3] = {0};
                for (int i = row - margin_rows; i < row + margin_rows + 1; i++){
                    for (int j = col - margin_cols; j < col + margin_cols + 1; j++){
                        int img_i = i;
                        int img_j = j;
                        int kernel_i = i - row + margin_rows;
                        int kernel_j = j - col + margin_cols;
                        if (i < 0)          img_i = 0;
                        if (j < 0)          img_j = 0;
                        if (i >= height)    img_i = height - 1;
                        if (j >= width)     img_j = width - 1;
                        suma[0] += img -> pixels[img_i][img_j].R * kernel[kernel_i][kernel_j];
                        suma[1] += img -> pixels[img_i][img_j].G * kernel[kernel_i][kernel_j];
                        suma[2] += img -> pixels[img_i][img_j].B * kernel[kernel_i][kernel_j];
                    }
                }
                new_pixels[row][col].R = suma[0];
                new_pixels[row][col].G = suma[1];
                new_pixels[row][col].B = suma[2];
            }
        }
        img -> pixels = new_pixels;
    }

    char* output_file = argv[3];
    img_png_write_to_file (img, output_file);

    img_destroy(img);

    for (int row = 0; row < kernel_rows; row++) {
        free(kernel[row]);
    }
    free(kernel);

    return 0;
}
