import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_half_adder(dut):
    """Test all four combinations of the half adder."""

    test_vectors = [
        # A, B, expected SUM, expected CARRY
        (0, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 0, 1, 0),
        (1, 1, 0, 1),
    ]

    for a, b, expected_sum, expected_carry in test_vectors:

        # Set inputs
        dut.ui_in.value = (b << 1) | a

        # Allow combinational logic to settle
        await Timer(1, units="ns")

        # Read outputs
        actual_sum = int(dut.uo_out.value) & 1
        actual_carry = (int(dut.uo_out.value) >> 1) & 1

        # Check results
        assert actual_sum == expected_sum, (
            f"A={a}, B={b}: "
            f"expected SUM={expected_sum}, got {actual_sum}"
        )

        assert actual_carry == expected_carry, (
            f"A={a}, B={b}: "
            f"expected CARRY={expected_carry}, got {actual_carry}"
        )
