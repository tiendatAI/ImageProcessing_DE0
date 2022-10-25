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
        input        i_Clock_50,  //50MHz clock of DE0 -> Pin R8
        input        i_Rx_Serial, //input signal wire  -> Pin 
        input        i_Reset      //reset button       -> Pin J15
        //vga interface

    );

    wire [7:0] o_Rx_Byte;       //connect to vga module
    reg        r_Rx_Serial = 1;

    // Use a 50 MHz clock
    // Want to interface to 9600 baud UART
    // 50_000_000 / 9600 = 5208 Clocks Per Bit.
    parameter c_CLKS_PER_BIT = 5308;
    
    uart_rx #(.CLKS_PER_BIT(c_CLKS_PER_BIT)) UART_RX_INST (
        .o_Rx_DV(),
        .o_Rx_Byte(o_Rx_Byte), 
        .i_Clock(i_Clock_50),       
        .i_Rx_Serial(r_Rx_Serial) //unavailable
        );
    
    

endmodule
