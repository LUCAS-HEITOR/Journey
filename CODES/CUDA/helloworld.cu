#include <stdio.h>

__global__ void helloCUDA() {
    printf("Hello from CUDA!\n");
}

int main() {
    printf("Hello, World! (from CPU)\n");
    
    // Launch the kernel
    helloCUDA<<<1, 1>>>();
    
    // Wait for GPU to finish
    cudaDeviceSynchronize();
    
    printf("CUDA execution completed.\n");
    
    return 0;
}

//PlaceHolder - AI