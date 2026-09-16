/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module project (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Half adder
    // ui_in[0] = A
    // ui_in[1] = B
    // uo_out[0] = SUM
    // uo_out[1] = CARRY

    assign uo_out[0] = ui_in[0] ^ ui_in[1];
    assign uo_out[1] = ui_in[0] & ui_in[1];

    // Unused outputs
    assign uo_out[7:2] = 6'b0;

    // No bidirectional I/O used
    assign uio_out = 8'b0;
    assign uio_oe   = 8'b0;

endmodule

`default_nettype wire
