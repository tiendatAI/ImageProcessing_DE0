//This file combines all neccessary modules
`timescale 1ns / 1ps

`include "uart_rx.v"
`include "vga_controller.v"

//Tasks for module main:
/*
0. check port info
1. If board receive data -> blink LED
2. Add 1 button to reset status(stop receiving data, vga display)
4. Add controller to stack R, G, B in RAM
*/

module main #(
        parameter CLKS_PER_BIT = 5208 // (50MHz / 9600 baudrate) = 5208 Clocks Per Bit.
    ) 
    (
        //rx interface
        input        i_Clock_50,  //50MHz clock of DE0 -> Pin R8
        input        i_Rx_Serial, //input signal wire  -> Pin 
        input        i_Reset      //reset button       -> Pin J15
        //vga interface
    );

    wire [7:0] o_Rx_Byte;       //connect to vga module

    // uart_rx #(.CLKS_PER_BIT(CLKS_PER_BIT)) UART_RX_INST (
    //     .o_Rx_DV    (),
    //     .o_Rx_Byte  (o_Rx_Byte), 
    //     .i_Clock    (i_Clock_50),
    //     .i_Rx_Serial(i_Rx_Serial) //unavailable
    //     );
    
    
    

endmodule
