//This file combines all neccessary modules
`include "uart_rx.v"
`include "vga_controller.v"


//Tasks for module main:
/*
0. check port info
1. If board receive data -> blink LED
2. Add 1 button to reset status(stop receiving data, vga display)
4. Add controller to stack R, G, B in RAM
*/
module main
    (
        //rx interface
        output       o_Rx_DV,
        output [7:0] o_Rx_Byte,  
        input        i_Clock, //another clock wire ?
        input        i_Rx_Serial //infor of serial ?
    );
    // Use a 10 MHz clock
    // Want to interface to 115200 baud UART
    // 10000000 / 115200 = 87 Clocks Per Bit.
    parameter c_CLKS_PER_BIT = 87;
    
    uart_rx #(.CLKS_PER_BIT(c_CLKS_PER_BIT)) UART_RX_INST
        (.i_Clock(r_Clock), //unavailable
        .i_Rx_Serial(r_Rx_Serial), //unavailable
        .o_Rx_DV(),
        .o_Rx_Byte(w_Rx_Byte) //unavailable
        );
    
    

endmodule
