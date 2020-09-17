# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..tensors import TensorMode


def test_TensorMode_inputs():
    input_map = dict(
        b0_thres=dict(
            usedefault=True,
        ),
        in_bval=dict(
            extensions=None,
            mandatory=True,
        ),
        in_bvec=dict(
            extensions=None,
            mandatory=True,
        ),
        in_file=dict(
            extensions=None,
            mandatory=True,
        ),
        mask_file=dict(
            extensions=None,
        ),
        out_prefix=dict(),
    )
    inputs = TensorMode.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TensorMode_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = TensorMode.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
