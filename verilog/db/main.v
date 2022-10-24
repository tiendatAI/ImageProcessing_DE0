//This file combines all neccessary modules
`include "uart_tx.v"
`include "uart_rx.v"
`include "vga_controller"

//Tasks for module main:
/*
0. check port info
1. If board receive data -> blink LED
2. Add 1 button to reset status(stop receiving data, vga display)
4. Add controller to stack R, G, B in RAM
*/
module main();
    

endmodule
